from best_posts.last_posts_fetcher import LastPostsFetcher
from best_posts.top_posts_selector import TopPostsSelector
from best_posts.html_posts_exporter import HtmlPostsExporter


dank_memes = '-120254617'
reddit = '-150550417'


wall_id = reddit
print('Введите количество постов')
posts_fetch_count = 100
top_posts_count = 5

posts = LastPostsFetcher(wall_id, posts_fetch_count).fetch()
top_posts = TopPostsSelector(posts, top_posts_count).select_top_posts()
HtmlPostsExporter(wall_id, top_posts).export()


file = open('posts.html', 'w')
file.write(HtmlPostsExporter(wall_id, top_posts).export())
file.close()
print()