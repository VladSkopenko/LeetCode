target_name = "Rex"
target_type = "dog"

data = [
    {"id": 1, "type": "cat", "name": "Rex"},
    {"id": 1, "type": "dog", "name": "Rex"},
    {"id": 1, "type": "cat", "name": "Barsik"},
    {"id": 1, "type": "dog", "name": "Sharik"},
]

result = next(
    (item for item in data if item["name"] == target_name and item["type"] == target_type),
    None
)

print(result)