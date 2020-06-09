class TopPostsSelector:
    def __init__(self, posts, top_posts_count):
        self.posts = posts
        self.top_posts_count = top_posts_count

    def select_top_posts(self):
        sorted_posts = sorted(self.posts, key=self.extract_likes, reverse=True)
        top_posts = sorted_posts[0:self.top_posts_count]
        return top_posts

    def extract_likes(self, some_post):
        likes = some_post['likes']
        count = likes['count']

        return count
