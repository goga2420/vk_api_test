from service.last_posts_fetcher import LastPostsFetcher
from service.top_posts_selector import TopPostsSelector
from service.html_group_posts_element_former import HtmlGroupPostsElementFormer
from vk_api.groups_get_by_id import GroupsGetById


class GroupBestPosts:
    def __init__(self, group_id, posts_fetch_count, top_posts_count):
        self.group_id = group_id
        self.posts_fetch_count = posts_fetch_count
        self.top_posts_count = top_posts_count

    def start(self):
        group = GroupsGetById([str(self.group_id)]).groups_info_getter()[0]

        html_head = '<!DOCTYPE HTML>\n<meta charset="utf-8"/>\n<html>\n<head><title>Сылки на посты</title><head/>\n<body>\n'
        string_end = '</body>\n</html>'

        file = open(group['name'] + '.html', 'w')
        file.write(html_head)
        posts = LastPostsFetcher('-' + str(group['id']), self.posts_fetch_count).fetch()
        top_posts = TopPostsSelector(posts, self.top_posts_count).select_top_posts()

        file.write(HtmlGroupPostsElementFormer(group, top_posts).form())
        file.write(string_end)

        file.close()
