from vk_api.token_provider import TokenProvider
import requests

class GroupsGetById:
    def __init__(self, group_ids):
        self.group_ids = group_ids
        self.token = TokenProvider().get_token()


    def groups_info_getter(self):
        vk_api_url = 'https://api.vk.com'
        version = '5.103'
        get_groups_info_url = vk_api_url + '/method/groups.getById?group_ids=' + ','.join(self.group_ids) + '&access_token=' + self.token + '&v=' + version
        site = requests.get(get_groups_info_url)
        site = site.json()
        groups = site['response']

        return groups
