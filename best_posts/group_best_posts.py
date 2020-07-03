from best_posts.last_posts_fetcher import LastPostsFetcher
from best_posts.top_posts_selector import TopPostsSelector
from best_posts.html_group_posts_element_former import HtmlGroupPostsElementFormer
from best_posts.groups_get_by_id import GroupsGetById


class GroupBestPosts:
    def __init__(self, group_id, count_fetching, count_top):
        self.group_id = group_id
        self.count_fetching = count_fetching
        self.count_top = count_top

    def start(self):
        group = GroupsGetById([str(self.group_id)]).groups_info_getter()[0]

        html_head = '<!DOCTYPE HTML>\n<meta charset="utf-8"/>\n<html>\n<head><title>Сылки на посты</title><head/>\n<body>\n'
        string_end = '</body>\n</html>'

        file = open(group['name'] + '.html', 'w')
        file.write(html_head)
        posts = LastPostsFetcher('-' + str(group['id']), self.count_fetching).fetch()
        top_posts = TopPostsSelector(posts, self.count_top).select_top_posts()

        file.write(HtmlGroupPostsElementFormer(group, top_posts).form())
        file.write(string_end)

        file.close()
