import os
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy import text
from database import get_db
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.get("/recommend")
def recommend(query: str = "", db: Session = Depends(get_db)):
    if not query:
        return []

    try:
        # 1. 사용자의 질문을 OpenAI 1536차원 벡터로 변환
        response = client.embeddings.create(
            model="text-embedding-3-small",
            input=query
        )
        query_vector = response.data[0].embedding

        # 2. 14개 지표와 문맥 유사도 거리 추출
        search_query = text("""
            SELECT 
                name, genres, description, 
                mania_score, story_depth, originality, difficulty, art_style, 
                replay_value, indie_spirit, character_appeal, user_friendliness, 
                addictiveness, emotional_impact, atmosphere_intensity, 
                soundtrack_prominence, gem_potential,
                (embedding <=> :vector) AS distance 
            FROM games
            ORDER BY distance
            LIMIT 30
        """)
        
        result = db.execute(search_query, {"vector": str(query_vector)})
        db_results = result.fetchall()

        if not db_results:
            return []

        # 3. Min-Max Scaling을 통한 거리 정규화
        distances = [float(row.distance) for row in db_results]
        min_dist, max_dist = min(distances), max(distances)
        if max_dist == min_dist:
            max_dist = min_dist + 0.0001 

        games_list = []
        for row in db_results:
            # 반환된 row 데이터를 14개 지표 매핑에 맞춰 분해
            (name, genres, desc, m_score, s_depth, orig, diff, art, 
             repl, indie, char, user_f, addict, emot, atmos, sound, g_pot, dist) = row
            current_dist = float(dist)

            # 4. 유사도 점수 (최대 80점)
            normalized_ai_score = 1.0 - ((current_dist - min_dist) / (max_dist - min_dist))
            similarity_score = 40.0 + (normalized_ai_score * 40.0)

            # 5. 숨겨진 보석 핵심 가중치 계산 (최대 20점 보너스)
            w_gem = float(g_pot or 0) * 0.30
            w_orig = float(orig or 0) * 0.15
            w_indie = float(indie or 0) * 0.15
            w_addict = float(addict or 0) * 0.10
            
            # 나머지 10개 지표의 평균 반영
            others_avg = (float(m_score or 0) + float(s_depth or 0) + float(diff or 0) + 
                          float(art or 0) + float(repl or 0) + float(char or 0) + 
                          float(user_f or 0) + float(emot or 0) + float(atmos or 0) + float(sound or 0)) / 10.0
            w_others = others_avg * 0.30
            
            bonus_score = ((w_gem + w_orig + w_indie + w_addict + w_others) / 100.0) * 20.0 
            final_score = similarity_score + bonus_score

            games_list.append({
                "name": name,
                "genres": genres,
                "description": desc[:150] + "...", 
                "ai_score": round(similarity_score, 1),
                "bonus_score": round(bonus_score, 1),
                "final_score": round(final_score, 1),
                # 프론트엔드 시각화를 위해 14개 지표 추가 전송
                "metrics": {
                    "mania_score": m_score, "story_depth": s_depth, "originality": orig,
                    "difficulty": diff, "art_style": art, "replay_value": repl,
                    "indie_spirit": indie, "character_appeal": char, "user_friendliness": user_f,
                    "addictiveness": addict, "emotional_impact": emot, 
                    "atmosphere_intensity": atmos, "soundtrack_prominence": sound,
                    "gem_potential": g_pot
                }
            })

        # 6. 최종 점수 기준 상위 정렬
        sorted_games = sorted(games_list, key=lambda x: x["final_score"], reverse=True)[:12]
        return sorted_games

    except Exception as e:
        print(f"❌ DB 검색 중 치명적 에러 발생: {e}")
        raise HTTPException(status_code=500, detail=f"DB 검색 실패: {str(e)}")

@app.get("/")
def root():
    return {"message": "Hidden-Gem Finder API is Running with OpenAI! 🚀"}