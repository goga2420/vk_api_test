from best_posts.last_posts_fetcher import LastPostsFetcher
from best_posts.top_posts_selector import TopPostsSelector
from best_posts.html_posts_exporter import HtmlPostsExporter
from user_groups_get import UserGroupsGet


dank_memes = '-120254617'
reddit = '-150550417'
api_group = '-1'
ёжики = '-148428969'


wall_id = ёжики
posts_fetch_count = 100
top_posts_count = 5
print('Выбор лучших', top_posts_count, 'постов из последних', posts_fetch_count)

posts = LastPostsFetcher(wall_id, posts_fetch_count).fetch()
top_posts = TopPostsSelector(posts, top_posts_count).select_top_posts()
HtmlPostsExporter(wall_id, top_posts).export()


file = open('posts.html', 'w')
file.write(HtmlPostsExporter(wall_id, top_posts).export())
file.close()

user_id = 184311128
user_groups = UserGroupsGet(user_id, offset=2, count=3, extended=1).get_users_group()

print()