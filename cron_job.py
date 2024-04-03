import requests
response = requests.get(
    "http://127.0.0.1:8000/get",
#     headers={
#     'Authorization': 'Token b63cf202336f472d735be566409be907bafe1eb2',
# }
    
)

print(response.status_code)

result = response.json()
print(result)