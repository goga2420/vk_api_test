from best_posts.last_posts_fetcher import LastPostsFetcher
from best_posts.top_posts_selector import TopPostsSelector

owner_id = '-120254617'
print('Введите количество постов')
posts_number = int(input())
top_posts_count = 5

posts = LastPostsFetcher(owner_id, posts_number).fetch()
top_posts = TopPostsSelector(posts, top_posts_count).select_top_posts()


print()
