import json

json_str = '{"id":235, "brand": "Nike", "qty": 84, "status": {"isForSale": true} }'
sneakers = json.loads(json_str)

print(type(sneakers))
print(sneakers['brand'])
print(sneakers['qty'])
print(sneakers['status']['isForSale'])

print(json.dumps(sneakers, indent=2))

json_array = '[{"a":1},{"b": 2},{"c": 3}]'
array = json.loads(json_array)
print(json.dumps(array, indent=2))