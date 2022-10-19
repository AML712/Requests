import requests
from pprint import pprint
import json

url = "https://akabab.github.io/superhero-api/api//all.json"
response = requests.get(url)
all_heroes = response.json()
three_heroes = filter(lambda hero: hero['name'] in ['Hulk', 'Captain America', 'Thanos'], all_heroes)
heroes_intelligence = {hero['name']: hero['powerstats']['intelligence'] for hero in three_heroes}
print(f'Самый умный супергерой: {max(heroes_intelligence, key=heroes_intelligence.get)}')



class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def upload(self, file_path, filename):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': file_path, 'overwrite': 'true'}
        source = requests.get(upload_url, headers=headers, params=params)
        s = source.json()
        href = s.get('href', '')
        result = requests.put(href, data=open(filename, 'rb'))
        return result


if __name__ == '__main__':
    path_to_file = 'test.txt'
    token = ' '
    uploader = YaUploader(token)
    uploader.upload(path_to_file, 'test.txt')



