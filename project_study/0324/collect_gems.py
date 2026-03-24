import os
import json
import requests
import time
from openai import OpenAI
from sqlalchemy import create_engine, text
from dotenv import load_dotenv, find_dotenv
from tqdm import tqdm

load_dotenv(find_dotenv())
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

DB_URL = "postgresql://juntae:0312@localhost:5432/hidden_gem_db" 
engine = create_engine(DB_URL)

def analyze_and_embed(name, genres, developer, desc):
    rich_text = f"Title: {name}\nDeveloper: {developer}\nGenres: {genres}\nDescription: {desc}"
    
    prompt = """
    You are an expert game reviewer. Read the game info and evaluate the following 14 metrics on a scale of 0 to 100.
    Output ONLY in JSON format:
    {"mania_score": 0, "story_depth": 0, "originality": 0, "difficulty": 0, "art_style": 0, "replay_value": 0, "indie_spirit": 0, "character_appeal": 0, "user_friendliness": 0, "addictiveness": 0, "emotional_impact": 0, "atmosphere_intensity": 0, "soundtrack_prominence": 0, "gem_potential": 0}
    """
    
    chat_response = client.chat.completions.create(
        model="gpt-4o",
        response_format={ "type": "json_object" },
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": rich_text}
        ]
    )
    scores = json.loads(chat_response.choices[0].message.content)

    embed_response = client.embeddings.create(
        model="text-embedding-3-small",
        input=rich_text
    )
    vector = embed_response.data[0].embedding
    
    return scores, vector

def collect_and_store():
    print("🚀 스팀 데이터 수집 및 14개 AI 지표 평가 엔진 가동...")
    chart_url = "https://api.steampowered.com/ISteamChartsService/GetGamesByConcurrentPlaytime/v1/"
    res = requests.get(chart_url).json()
    app_ids = [g['appid'] for g in res['response']['ranks']]

    for app_id in tqdm(app_ids, desc="수집 및 분석 중"):
        try:
            url = f"https://store.steampowered.com/api/appdetails?appids={app_id}&l=korean"
            detail_res = requests.get(url).json()
            
            if not detail_res or not detail_res[str(app_id)]['success']:
                time.sleep(0.5)
                continue
                
            data = detail_res[str(app_id)]['data']
            name = data['name']
            desc = data.get('short_description', "")
            
            if len(desc) < 40: continue
                
            genres = ", ".join([g['description'] for g in data.get('genres', [])])
            developer = data.get('developers', ["Unknown"])[0]
            
            scores, vector = analyze_and_embed(name, genres, developer, desc)

            with engine.connect() as conn:
                query = text("""
                    INSERT INTO games (
                        app_id, name, genres, developer, description,
                        mania_score, story_depth, originality, difficulty, art_style,
                        replay_value, indie_spirit, character_appeal, user_friendliness, addictiveness,
                        emotional_impact, atmosphere_intensity, soundtrack_prominence, gem_potential,
                        embedding
                    ) VALUES (
                        :app_id, :name, :genres, :developer, :desc,
                        :m_score, :s_depth, :orig, :diff, :art,
                        :replay, :indie, :char, :user_f, :addict,
                        :emot, :atmos, :sound, :gem_pot,
                        :vec
                    ) ON CONFLICT (app_id) DO NOTHING
                """)
                conn.execute(query, {
                    "app_id": str(app_id), "name": name, "genres": genres, 
                    "developer": developer, "desc": desc,
                    "m_score": scores.get('mania_score', 0), "s_depth": scores.get('story_depth', 0),
                    "orig": scores.get('originality', 0), "diff": scores.get('difficulty', 0),
                    "art": scores.get('art_style', 0), "replay": scores.get('replay_value', 0),
                    "indie": scores.get('indie_spirit', 0), "char": scores.get('character_appeal', 0),
                    "user_f": scores.get('user_friendliness', 0), "addict": scores.get('addictiveness', 0),
                    "emot": scores.get('emotional_impact', 0), "atmos": scores.get('atmosphere_intensity', 0),
                    "sound": scores.get('soundtrack_prominence', 0), "gem_pot": scores.get('gem_potential', 0),
                    "vec": str(vector)
                })
                conn.commit()
            
            time.sleep(0.5)
            
        except Exception as e:
            continue

if __name__ == "__main__":
    collect_and_store()