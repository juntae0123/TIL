import requests
from pprint import pprint

API_URL = 'https://jsonplaceholder.typicode.com/users'

response = requests.get(API_URL)
parsed_data = response.json()

black_list = [
    'Hoeger LLC',
    'Keebler LLC',
    'Yost and Sons',
    'Johns Group',
    'Romaguera-Crona',
]


def censorship(user):
    company = user['company']['name']
    name = user['name']

    if company in black_list:
        print(f"{company} 소속의 {name}은/는 등록할 수 없습니다.")
        return False
    else:
        print("이상 없습니다.")
        return True


def create_user(parsed_data):
    censored_user_list = {}

    for user in parsed_data:
        if censorship(user):
            company = user['company']['name']
            name = user['name']

            if company not in censored_user_list:
                censored_user_list[company] = []

            censored_user_list[company].append(name)

    return censored_user_list
result = create_user(parsed_data)
pprint(result)

     