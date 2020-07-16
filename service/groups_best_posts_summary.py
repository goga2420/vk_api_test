from vk_api.groups_get_by_id import GroupsGetById
from service.top_posts_selector import TopPostsSelector
from service.last_posts_fetcher import LastPostsFetcher
from service.html_group_posts_element_former import HtmlGroupPostsElementFormer
from vk_api.groups_friend_members_get import GroupFriendsMembersGet

# Класс GroupsBestPostsSummary создает html файл в котором получаются, отбираются и сохраняются посты


class GroupsBestPostsSummary:
    def __init__(self, group_ids, posts_fetch_count, top_posts_count):
        self.group_ids = group_ids
        self.posts_fetch_count = posts_fetch_count
        self.top_posts_count = top_posts_count


    def start(self):
        groups = GroupsGetById(self.group_ids).groups_info_getter()

        html_head = '<!DOCTYPE HTML>\n<meta charset="utf-8"/>\n<html>\n<head><title>Сылки на посты</title><head/>\n<body>\n'
        string_end = '</body>\n</html>'
        file = open('posts.html', 'w')
        file.write(html_head)
        for group in groups:
            posts = LastPostsFetcher('-' + str(group['id']), self.posts_fetch_count).fetch()
            top_posts = TopPostsSelector(posts, self.top_posts_count).select_top_posts()
            file.write(HtmlGroupPostsElementFormer(group, top_posts).form())
            file.write('\t<br>')
            file.write(', '.join(GroupFriendsMembersGet(group['id']).friend_links_maker()))
            file.write('\n<br>')
            file.write('<br>')
            file.write('<br>\n\n\n')

        file.write(string_end)
        file.close()
