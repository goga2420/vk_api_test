from best_posts.wall_get import WallGet

class LastPostsFetcher:
    def __init__(self, owner_id, posts_number):
        self.owner_id = owner_id
        self.posts_number = posts_number

    def fetch(self):
        posts = []
        offset = 0
        max_count = 100
        while offset < self.posts_number:
            posts_left = self.posts_number - offset

            if posts_left < max_count:
                count = posts_left
            else:
                count = max_count

            posts_fetcher = WallGet(self.owner_id, offset, count)
            posts.extend(posts_fetcher.fetch())
            offset = offset + count

        print('Posts fetched:', len(posts))
        return posts
