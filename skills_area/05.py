import json

json_file = """
    {
        "key1": 1,
        "key2": 2
    }
    """
# json.dumps() - преобразует объект в формате json
# json.dump() - преобразует объект в формате json и записывает в файл
#
# json.loads() - преобразует json-строку в питоновский объект
# json.load() - преобразует json-файл в питоновский объект

json_file1 = json.loads(json_file)
print(json_file1["key2"])

dct = {
    "name": "Denis",
    "age":20,
    "prof": "SQA"
}
json_file = json.dumps(dct)
print(type(dct))
print(dct)
print("=============================")
print(type(json_file))
print(json_file)
file_name = "../.venv/files/json.json"
with open(file_name, "w" ) as f:
    json.dump(dcT, f)



