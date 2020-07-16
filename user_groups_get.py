from vk_api.token_provider import TokenProvider
import requests


class UserGroupsGet:
    def __init__(self, user_id, offset, count, extended):
        self.user_id = user_id
        self.offset = offset
        self.count = count
        self.extended = extended
        self.token = TokenProvider().get_token()


    def get_users_group(self):
        vk_api_url = 'https://api.vk.com'
        version = '5.103'
        users_groups_link = vk_api_url + '/method/groups.get?user_id=' + str(self.user_id) \
                            + '&offset=' + str(self.offset) \
                            + '&count=' + str(self.count) \
                            + '&extended=' + str(self.extended) \
                            + '&access_token=' + self.token \
                            + '&v=' + version

        site = requests.get(users_groups_link)
        json = site.json()
        groups = json['response']['items']

        return groups
