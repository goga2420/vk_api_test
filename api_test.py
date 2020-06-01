import requests

vk_api_url = 'https://api.vk.com'
access_token = '06ace662f4fb65e98ed0bdca94f51cc043828f1e99aa993408d751e124e2b094b021afebbb19304b00093'
version = '5.103'

method_group = 'groups.get'


def my_groups():
    get_my_groups_url = vk_api_url + '/method/' + method_group + '?user_id=184311128&extended=1&access_token=' + access_token + '&v=' + version
    site = requests.get(get_my_groups_url)
    print("Status code:", site.status_code)
    print(site.json())

#my_groups()



dank_memes_id = '120254617'
reddit_id = '-150550417'
dailysh_id = '-128637780'


method_posts = 'wall.get'
def wall_posts():
    get_wall_posts_url = vk_api_url + '/method/' + method_posts + '?owner_id=-' + dank_memes_id + '&extended=1&access_token=' + access_token + '&v=' + version
    site = requests.get(get_wall_posts_url)
    print("Status code:", site.status_code)
    print(site.json())

#wall_posts()


method_members = 'groups.getMembers'
def group_members():
    get_group_members_url = vk_api_url + '/method/' + method_members + '?group_id=' + dank_memes_id + '&offset=990&access_token=' + access_token + '&v=' + version
    site = requests.get(get_group_members_url)
    print("Status code:", site.status_code)
    print(site.json())

group_members()


method_likes = 'likes.isLiked'
#def most_likes():
    #get_most_liked_post