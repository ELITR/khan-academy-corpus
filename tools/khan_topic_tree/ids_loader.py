import requests

file_name = 'topictree.json'

response = requests.get('https://www.khanacademy.org/api/v1/topictree')

with open(file_name, 'w') as f:
    f.write(response.text)
