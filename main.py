from service.groups_best_posts_summary import GroupsBestPostsSummary


# Главный файл в котором находится информация о названиях и требуемых аргументах и в котором запускается весь код


dank_memes = '120254617'
reddit = '150550417'
api_group = '1'
ёжики = '148428969'



group_ids = [dank_memes, reddit, api_group, ёжики]
posts_fetch_count = 100
top_posts_count = 5


GroupsBestPostsSummary(group_ids, posts_fetch_count, top_posts_count).start()
