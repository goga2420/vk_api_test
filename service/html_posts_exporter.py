# Класс HtmlPostsExporter формирует ссылки на посты, после чего скрепляет их с html строчками так, чтобы получилась готовая html страницы


class HtmlPostsExporter:
    def __init__(self, wall_id, posts):
        self.wall_id = wall_id
        self.posts = posts

    def export(self):
        head = '<!DOCTYPE HTML>\n<meta charset="utf-8"/>\n<html>\n<head><title>Сылки на посты</title><head/>\n<body>\n'
        string_end = '</body>\n</html>'
        html_string = head + self.all_posts_link_maker(self.posts) + string_end

        return html_string

    def all_posts_link_maker(self, posts):
        all_links = ''
        for i in range(0, len(posts)):
           all_links = all_links + self.one_post_link_maker(posts[i])

        return all_links

    def one_post_link_maker(self, post):
        vk_url = 'https://vk.com/wall'
        href = '\t<a href="' \
               + vk_url + str(self.wall_id) + '_' + str(post['id']) + '">' \
               + str(post['likes']['count']) + '❤, ' + post['comments']['count'] + 'comments, ' + post['text'][:50] + '</a><br/>\n'

        return href
