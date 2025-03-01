import hashlib
import requests
from datetime import datetime
import vk_api


# Получение постов из групп ВКонтакте
def get_vk_posts(group_ids, count=10):
    token = '67ed906d67ed906d67ed906dcc64c6bf27667ed67ed906d002dfc82661ea3e5dbbf665d'
    vk_session = vk_api.VkApi(token=token)
    vk = vk_session.get_api()

    all_posts = []
    for group_id in group_ids:
        posts = vk.wall.get(owner_id=-group_id, count=count, extended=1)
        all_posts.extend(posts['items'])

    # Фильтруем только посты с изображениями
    return filter_image_posts(all_posts)

# Фильтрация только постов с изображениями
def filter_image_posts(posts):
    filtered_posts = []
    for post in posts:
        if post.get('attachments'):
            has_images = any(attachment['type'] == 'photo' for attachment in post['attachments'])
            if has_images:
                filtered_posts.append({
                    "id": post['id'],
                    "date": datetime.fromtimestamp(post['date']).strftime("%Y-%m-%d"),  # Преобразуем timestamp в дату
                    "likes": post['likes']['count'],
                    "comments": post['comments']['count'],
                    "reposts": post['reposts']['count'],
                    "text": post['text'],
                    "attachments": post['attachments']
                })
    return filtered_posts

# Сортировка по количеству лайков
def sort_posts_by_likes(posts):
    return sorted(posts, key=lambda post: post['likes'], reverse=True)

# Сортировка по количеству репостов
def sort_posts_by_reposts(posts):
    return sorted(posts, key=lambda post: post['reposts'], reverse=True)

# Сортировка по количеству комментариев
def sort_posts_by_comments(posts):
    return sorted(posts, key=lambda post: post['comments'], reverse=True)