class HtmlGroupPostsElementFormer:
    def __init__(self, group, posts):
        self.group = group
        self.posts = posts


    def form(self):
        group_head = '<p>' + self.group['name'] + ' <a href="https://vk.com/public' + str(self.group['id']) + '">open</a></p>\n'
        group_html_element = group_head + self.all_posts_link_maker(self.posts)

        return group_html_element


    def all_posts_link_maker(self, posts):
        all_links = ''
        for i in range(0, len(posts)):
           all_links = all_links + self.one_post_link_maker(posts[i])

        return all_links


    def one_post_link_maker(self, post):
        vk_url = 'https://vk.com/wall'
        href = '\t<a href="' \
               + vk_url + '-' + str(self.group['id']) + '_' + str(post['id']) + '">' \
               + str(post['likes']['count']) + '❤ ' + post['text'][:50] + '</a><br/>\n'

        return href

