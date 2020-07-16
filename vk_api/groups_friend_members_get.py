from vk_api.token_provider import TokenProvider
import requests


class GroupFriendsMembersGet:
    def __init__(self, group_id):
        self.group_id = group_id
        self.token = TokenProvider().get_token()


    def friend_members_getter(self):
        vk_api_url = 'https://api.vk.com'
        version = '5.103'
        get_friend_members_link = vk_api_url + '/method/groups.getMembers?group_id=' + str(self.group_id) +\
                                  '&fields=first_name,last_name' +\
                                  '&filter=friends' + \
                                  '&access_token=' + self.token + \
                                  '&v=' + version
        site = requests.get(get_friend_members_link)
        site = site.json()
        friends = site['response']['items']

        return friends


    def friend_links_maker(self):
        list_of_html_links = []
        for user in self.friend_members_getter():
            link = 'https://vk.com/id' + str(user['id'])
            html_link = '<a href="' + link + '">' + user['first_name'] + ' ' + user['last_name'] + '</a>'
            list_of_html_links.append(html_link)

        return list_of_html_links
