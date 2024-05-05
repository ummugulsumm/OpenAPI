import requests

# Tüm öğeleri listeleme
response = requests.get("http://localhost:5000/items")
print(response.json())

# Yeni bir öğe oluşturma
new_item = {"id": 2, "name": "New Item"}
response = requests.post("http://localhost:5000/items", json=new_item)
print(response.json())

# Belirli bir öğeyi almak
response = requests.get("http://localhost:5000/items/2")
print(response.json())

# Belirli bir öğeyi güncelleme
updated_item = {"name": "Updated Item"}
response = requests.put("http://localhost:5000/items/2", json=updated_item)
print(response.json())

# Belirli bir öğeyi silme
response = requests.delete("http://localhost:5000/items/2")
print(response.status_code)  # 204
