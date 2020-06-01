from best_posts.token_provider import TokenProvider
import requests

class WallGet:
    def __init__(self, owner_id, offset, count):
        self.owner_id = owner_id
        self.offset = offset
        self.count = count
        self.token = TokenProvider().get_token()

    def fetch(self):
        vk_api_url = 'https://api.vk.com'
        version = '5.103'
        get_wall_posts_url = vk_api_url + '/method/wall.get?owner_id=' + str(self.owner_id) + '&offset=' + str(self.offset) + '&count=' + str(self.count) + '&extended=1&access_token=' + self.token + '&v=' + version
        site = requests.get(get_wall_posts_url)
        if site.status_code != 200:
            print('WallGet.status_code =', site.status_code)

        json = site.json()
        posts = json['response']['items']
        return posts
