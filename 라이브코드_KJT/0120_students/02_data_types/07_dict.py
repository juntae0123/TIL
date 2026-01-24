# 딕셔너리 표현
my_dict_1 = {}
my_dict_2 = {'key': 'value'}
my_dict_3 = {'apple': 12, 'list': [1, 2, 3]}
print(my_dict_1)  # {}
print(my_dict_2)  # {'key': 'value'}
print(my_dict_3)  # {'apple': 12, 'list': [1, 2, 3]}


# 딕셔너리는 키에 접근해 값을 얻어냄
my_dict = {'name': '홍길동', 'age': 25}
print(my_dict['name'])  # '홍길동'
print(my_dict['test'])  # KeyError: 'test'


# 딕셔너리 값 추가 및 변경
my_dict = {'apple': 12, 'list': [1, 2, 3]}
# 추가
my_dict['banana'] = 50
print(my_dict)  # {'apple': 12, 'list': [1, 2, 3], 'banana': 50}

# 변경
my_dict['apple'] = 100
print(my_dict)  # {'apple': 100, 'list': [1, 2, 3], 'banana': 50}

students ={
    {
        'name' : '김철수.',
        'age' : 25,
        'address' : '서울시 강남구',
        'phone' : '010-1234-5678'
    },

    {
        'name' : '이영희.',
        'age' : 23,
        'address' : '서울시 마포구',
        'phone' : '010-9876-5432'
    },
    {
        'name' : '박지민.',
        'age' : 27,
        'address' : '서울시 서초구',
        'phone' : '010-5555-6666'
    },
    {
        'name' : '최민수.',
        'age' : 29,
        'address' : '서울시 종로구',
        'phone' : '010-7777-8888'
    },
    
}