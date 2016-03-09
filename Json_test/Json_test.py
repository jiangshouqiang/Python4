import json
d = dict(name="bob",age=20,score=99,test_null=None)
print(json.dumps(d))

json_str = '{"test_null": null, "age": 20, "name": "bob", "score": 99}'
print(json.loads(json_str))