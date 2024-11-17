import json

def task() -> float:
    with open("input.json") as f:
        json_data = json.load(f)
    return round(sum([dict_['score'] * dict_['weight'] for dict_ in json_data]), 3)


print(task())
