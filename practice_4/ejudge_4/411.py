dict_arr = {
    "person": {
        "name": 1, 
        "age": 2, 
        "course": {
            "ttt":"ppp",
            "lll":"kkk"
        }
    }
}

def func(d):
    for key in d:
        print(key)
        if isinstance(d[key], dict):
            func(d[key]) 

func(dict_arr)


import json

first_s = input()
second_s = input()

first_d = json.loads(first_s)
second_d = json.loads(second_s)

