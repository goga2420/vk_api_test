class HtmlPostsExporter:
    def __init__(self, wall_id, posts):
        self.wall_id = wall_id
        self.posts = posts


    def export(self):
        vk_url = 'https://vk.com/wall'
        head = '<!DOCTYPE HTML>\n<meta charset="utf-8"/>\n<html>\n<head><title>Сылки на посты</title><head/>\n<body>\n'
        string_end = '</body>\n</html>'

        all_links = ''
        for i in range(0, len(self.posts)):
            href = '\t<a href="' + vk_url + str(self.wall_id) + '_' + str(self.posts[i]['id']) + '">Пост ' + str(i + 1) + '</a><br/>\n'
            all_links = all_links + href

        html_string = head + all_links + string_end

        return html_string
