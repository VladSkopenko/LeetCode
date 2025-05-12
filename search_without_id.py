target_id = 1
target_type = "dog"

data = [
    {"id": 1, "type": "cat", "name": "Rex"},
    {"id": 1, "type": "dog", "name": "Rex"},
    {"id": 1, "type": "cat", "name": "Barsik"},
    {"id": 1, "type": "dog", "name": "Sharik"},
]

result = next(
    (item for item in data if item["id"] == target_id and item["type"] == target_type),
    None
)

print(result)