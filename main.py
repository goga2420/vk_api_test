from best_posts.groups_get_by_id import GroupsGetById
from best_posts.html_group_posts_element_former import HtmlGroupPostsElementFormer
from best_posts.last_posts_fetcher import LastPostsFetcher
from best_posts.top_posts_selector import TopPostsSelector

dank_memes = '-120254617'
reddit = '-150550417'
api_group = '-1'
ёжики = '-148428969'


wall_id = ёжики
posts_fetch_count = 100
top_posts_count = 5
print('Выбор лучших', top_posts_count, 'постов из последних', posts_fetch_count)


group_ids = ['120254617', '150550417', '1', '148428969']
groups = GroupsGetById(group_ids).groups_info_getter()


html_head = '<!DOCTYPE HTML>\n<meta charset="utf-8"/>\n<html>\n<head><title>Сылки на посты</title><head/>\n<body>\n'
string_end = '</body>\n</html>'
file = open('posts.html', 'w')
file.write(html_head)
for group in groups:
    posts = LastPostsFetcher('-' + str(group['id']), posts_fetch_count).fetch()
    top_posts = TopPostsSelector(posts, top_posts_count).select_top_posts()
    file.write(HtmlGroupPostsElementFormer(group, top_posts).form())

file.write(string_end)
file.close()
print()