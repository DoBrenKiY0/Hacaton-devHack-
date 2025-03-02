import vk_api
from key import key
from vk_api.exceptions import ApiError

a, b, c, d = 1, 2 , 3, 0.1
slov_ip = {}

group_id = ['-112709585']


def the_best():
    vk_session = vk_api.VkApi(token=key)
    vk = vk_session.get_api()

    for i in group_id:
        try:
            wall_posts = vk.wall.get(domain=i, count=100, filter='owner')['items']
        except ApiError as e:
            print(f"Ошибка при получении постов: {e}")
            wall_posts = []

        # Проходим по каждому посту и собираем данные
        mati = ["пидор", "блять", "ёбанный в рот", "пиздец", "хуй", "долбаёб", "еблан", "хуепутало", "Пошёл на хуй", "пошел на хуй", "дрочильня", "ебать"]

        for post in wall_posts:
            post_id = post['id']
            text = post['text']
            if text in mati:
                continue
            likes = post['likes']['count']
            comments = post['comments']['count']
            reposts = post['reposts']['count']
            views = post.get('views', {}).get('count', 0)  # Просмотры могут быть недоступны
            indeks_popular = a * likes + b * comments + c * reposts + d * views
            post_id2 = f'{str(group_id[-1])}_{post_id}'
            slov_ip.update({indeks_popular: post_id})

        sorted_keys = sorted(slov_ip.keys())
        post__idish = slov_ip[sorted_keys[-1]]
        post_id2 = f'{str(group_id[-1])}_{post__idish}'

        try:
            post = vk.wall.getById(posts=post_id2, count=100)[0]  # Метод возвращает список постов
        except vk_api.exceptions.ApiError as e:
            print(f"Ошибка при получении поста: {e}")
            post = None

        if post and 'attachments' in post:
            # Проходим по всем вложениям
            for attachment in post['attachments']:
                # Если вложение — это фото
                if attachment['type'] == 'photo':
                    # Получаем URL фотографии с максимальным размером
                    photo_url = attachment['photo']['sizes'][-1]['url']
        else:
            return "В посте нет вложений с фотографиями."
    return photo_url


def text():
    vk_session = vk_api.VkApi(token=key)
    vk = vk_session.get_api()

    for i in group_id:
        try:
            wall_posts = vk.wall.get(domain=i, count=100, filter='owner')['items']
        except ApiError as e:
            print(f"Ошибка при получении постов: {e}")
            wall_posts = []

        # Проходим по каждому посту и собираем данные
        mati = ["пидор", "блять", "ёбанный в рот", "пиздец", "хуй", "долбаёб", "еблан", "хуепутало", "Пошёл на хуй", "пошел на хуй", "дрочильня", "ебать"]

        for post in wall_posts:
            post_id = post['id']
            text = post['text']
            if text in mati:
                continue
            likes = post['likes']['count']
            comments = post['comments']['count']
            reposts = post['reposts']['count']
            views = post.get('views', {}).get('count', 0)  # Просмотры могут быть недоступны
            indeks_popular = a * likes + b * comments + c * reposts + d * views
            post_id2 = f'{str(group_id[-1])}_{post_id}'
            slov_ip.update({indeks_popular: post_id})

        sorted_keys = sorted(slov_ip.keys())
        post__idish = slov_ip[sorted_keys[-1]]
        post_id2 = f'{str(group_id[-1])}_{post__idish}'

        try:
            post = vk.wall.getById(posts=post_id2)[0]  # Метод возвращает список постов
        except vk_api.exceptions.ApiError as e:
            print(f"Ошибка при получении поста: {e}")
            post = None
        if post and 'text' in post and post['text'].strip():

            # Извлекаем текст поста
            post_text = post['text']
            return post_text
        else:
            return 'пост без текста'
        

def the_best2():
    vk_session = vk_api.VkApi(token=key)
    vk = vk_session.get_api()


    for i in group_id:
        try:
            wall_posts = vk.wall.get(domain=i, count=100, filter='owner')['items']
        except ApiError as e:
            print(f"Ошибка при получении постов: {e}")
            wall_posts = []

        # Проходим по каждому посту и собираем данные
        mati = ["пидор", "блять", "ёбанный в рот", "пиздец", "хуй", "долбаёб", "еблан", "хуепутало", "Пошёл на хуй", "пошел на хуй", "дрочильня", "ебать"]

        for post in wall_posts:
            post_id = post['id']
            text = post['text']
            if text in mati:
                continue
            likes = post['likes']['count']
            comments = post['comments']['count']
            reposts = post['reposts']['count']
            views = post.get('views', {}).get('count', 0)  # Просмотры могут быть недоступны
            indeks_popular = a * likes + b * comments + c * reposts + d * views
            post_id2 = f'{str(group_id[-1])}_{post_id}'
            slov_ip.update({indeks_popular: post_id})

        sorted_keys = sorted(slov_ip.keys())
        post__idish = slov_ip[sorted_keys[-3]]
        print(post__idish)
        post_id2 = f'{str(group_id[-1])}_{post__idish}'

        try:
            post = vk.wall.getById(posts=post_id2)[0]  # Метод возвращает список постов
        except vk_api.exceptions.ApiError as e:
            print(f"Ошибка при получении поста: {e}")
            post = None

        if post and 'attachments' in post:
            # Проходим по всем вложениям
            for attachment in post['attachments']:
                # Если вложение — это фото
                if attachment['type'] == 'photo':
                    # Получаем URL фотографии с максимальным размером
                    photo_url = attachment['photo']['sizes'][-1]['url']
        else:
            return "В посте нет вложений с фотографиями."
    return photo_url


def text2():
    vk_session = vk_api.VkApi(token=key)
    vk = vk_session.get_api()

    for i in group_id:
        try:
            wall_posts = vk.wall.get(domain=i, count=100, filter='owner')['items']
        except ApiError as e:
            print(f"Ошибка при получении постов: {e}")
            wall_posts = []

        # Проходим по каждому посту и собираем данные
        mati = ["пидор", "блять", "ёбанный в рот", "пиздец", "хуй", "долбаёб", "еблан", "хуепутало", "Пошёл на хуй", "пошел на хуй", "дрочильня", "ебать"]

        for post in wall_posts:
            post_id = post['id']
            text = post['text']
            if text in mati:
                continue
            likes = post['likes']['count']
            comments = post['comments']['count']
            reposts = post['reposts']['count']
            views = post.get('views', {}).get('count', 0)  # Просмотры могут быть недоступны
            indeks_popular = a * likes + b * comments + c * reposts + d * views
            post_id2 = f'{str(group_id[-1])}_{post_id}'
            slov_ip.update({indeks_popular: post_id})

        sorted_keys = sorted(slov_ip.keys())
        post__idish = slov_ip[sorted_keys[-3]]
        post_id2 = f'{str(group_id[-1])}_{post__idish}'

        try:
            post = vk.wall.getById(posts=post_id2)[0]  # Метод возвращает список постов
        except vk_api.exceptions.ApiError as e:
            print(f"Ошибка при получении поста: {e}")
            post = None
        if post and 'text' in post and post['text'].strip():
            # Извлекаем текст поста
            post_text = post['text']
            return post_text
        else:
            return "пост без текста"
        

def the_best3():
    vk_session = vk_api.VkApi(token=key)
    vk = vk_session.get_api()

    for i in group_id:
        try:
            wall_posts = vk.wall.get(domain=i, count=100, filter='owner')['items']
        except ApiError as e:
            print(f"Ошибка при получении постов: {e}")
            wall_posts = []

        # Проходим по каждому посту и собираем данные
        mati = ["пидор", "блять", "ёбанный в рот", "пиздец", "хуй", "долбаёб", "еблан", "хуепутало", "Пошёл на хуй", "пошел на хуй", "дрочильня", "ебать"]

        for post in wall_posts:
            post_id = post['id']
            text = post['text']
            if text in mati:
                continue
            likes = post['likes']['count']
            comments = post['comments']['count']
            reposts = post['reposts']['count']
            views = post.get('views', {}).get('count', 0)  # Просмотры могут быть недоступны
            indeks_popular = a * likes + b * comments + c * reposts + d * views
            post_id2 = f'{str(group_id[-1])}_{post_id}'
            slov_ip.update({indeks_popular: post_id})

        sorted_keys = sorted(slov_ip.keys())
        post__idish = slov_ip[sorted_keys[-10]]
        print(post__idish)
        post_id2 = f'{str(group_id[-1])}_{post__idish}'

        try:
            post = vk.wall.getById(posts=post_id2)[0]  # Метод возвращает список постов
        except vk_api.exceptions.ApiError as e:
            print(f"Ошибка при получении поста: {e}")
            post = None

        if post and 'attachments' in post:
            # Проходим по всем вложениям
            for attachment in post['attachments']:
                # Если вложение — это фото
                if attachment['type'] == 'photo':
                    # Получаем URL фотографии с максимальным размером
                    photo_url = attachment['photo']['sizes'][-1]['url']
        else:
            return "В посте нет вложений с фотографиями."
    return photo_url


def text3():
    vk_session = vk_api.VkApi(token=key)
    vk = vk_session.get_api()

    for i in group_id:
        try:
            wall_posts = vk.wall.get(domain=i, count=100, filter='owner')['items']
        except ApiError as e:
            print(f"Ошибка при получении постов: {e}")
            wall_posts = []

        # Проходим по каждому посту и собираем данные
        mati = ["пидор", "блять", "ёбанный в рот", "пиздец", "хуй", "долбаёб", "еблан", "хуепутало", "Пошёл на хуй", "пошел на хуй", "дрочильня", "ебать"]

        for post in wall_posts:
            post_id = post['id']
            text = post['text']
            if text in mati:
                continue
            likes = post['likes']['count']
            comments = post['comments']['count']
            reposts = post['reposts']['count']
            views = post.get('views', {}).get('count', 0)  # Просмотры могут быть недоступны
            indeks_popular = a * likes + b * comments + c * reposts + d * views
            post_id2 = f'{str(group_id[-1])}_{post_id}'
            slov_ip.update({indeks_popular: post_id})

        sorted_keys = sorted(slov_ip.keys())
        post__idish = slov_ip[sorted_keys[-10]]
        post_id2 = f'{str(group_id[-1])}_{post__idish}'
        print(post__idish)

        try:
            post = vk.wall.getById(posts=post_id2)[0]  # Метод возвращает список постов
        except vk_api.exceptions.ApiError as e:
            print(f"Ошибка при получении поста: {e}")
            post = None
        if post and 'text' in post and post['text'].strip():
            # Извлекаем текст поста
            post_text = post['text']
            return post_text
        else:
            return "пост без текста"
        

def the_likes():
    vk_session = vk_api.VkApi(token=key)
    vk = vk_session.get_api()


    for i in group_id:
        try:
            wall_posts = vk.wall.get(domain=i, count=100, filter='owner')['items']
        except ApiError as e:
            print(f"Ошибка при получении постов: {e}")
            wall_posts = []

        for post in wall_posts:
            post_id = post['id']
            likes = post['likes']['count']
            post_id2 = f'{str(group_id[-1])}_{post_id}'
            slov_ip.update({likes: post_id})

        sorted_keys = sorted(slov_ip.keys())
        post__idish = slov_ip[sorted_keys[-1]]
        post_id2 = f'{str(group_id[-1])}_{post__idish}'

        try:
            post = vk.wall.getById(posts=post_id2)[0]  # Метод возвращает список постов
        except vk_api.exceptions.ApiError as e:
            print(f"Ошибка при получении поста: {e}")
            post = None

        if post and 'attachments' in post:
            # Проходим по всем вложениям
            for attachment in post['attachments']:
                # Если вложение — это фото
                if attachment['type'] == 'photo':
                    # Получаем URL фотографии с максимальным размером
                    photo_url = attachment['photo']['sizes'][-1]['url']
        else:
            return "В посте нет вложений с фотографиями."
    return photo_url


def text_likes():
    vk_session = vk_api.VkApi(token=key)
    vk = vk_session.get_api()

    for i in group_id:
        try:
            wall_posts = vk.wall.get(domain=i, count=100, filter='owner')['items']
        except ApiError as e:
            print(f"Ошибка при получении постов: {e}")
            wall_posts = []

        for post in wall_posts:
            post_id = post['id']
            likes = post['likes']['count']
            slov_ip.update({likes: post_id})

        sorted_keys = sorted(slov_ip.keys())
        post__idish = slov_ip[sorted_keys[-1]]
        post_id2 = f'{str(group_id[-1])}_{post__idish}'

        
        try:
            # Получаем информацию о посте
            post = vk.wall.getById(posts=post_id2)[0]  # Метод возвращает список постов
            # Возвращаем количество репостов
            f =  post['likes']['count']
        except vk_api.exceptions.ApiError as e:
            print(f"Ошибка при получении поста: {e}")
            return None
        except KeyError:
            print("Пост не содержит информации о лайках.")
            return None

        try:
            post = vk.wall.getById(posts=post_id2)[0]  # Метод возвращает список постов
        except vk_api.exceptions.ApiError as e:
            print(f"Ошибка при получении поста: {e}")
            post = None
        if post and 'text' in post and post['text'].strip():
            # Извлекаем текст поста
            post_text = post['text']
            return post_text, f'количество лайков {f}'
        else:
            return f"пост без текста, количество лайков: {f}"
        

def reposts():
    vk_session = vk_api.VkApi(token=key)
    vk = vk_session.get_api()


    for i in group_id:
        try:
            wall_posts = vk.wall.get(domain=i, count=100, filter='owner')['items']
        except ApiError as e:
            print(f"Ошибка при получении постов: {e}")
            wall_posts = []

        for post in wall_posts:
            post_id = post['id']
            reposts = post['reposts']['count']
            post_id2 = f'{str(group_id[-1])}_{post_id}'
            slov_ip.update({reposts: post_id})

        sorted_keys = sorted(slov_ip.keys())
        post__idish = slov_ip[sorted_keys[-1]]
        post_id2 = f'{str(group_id[-1])}_{post__idish}'

        try:
            post = vk.wall.getById(posts=post_id2)[0]  # Метод возвращает список постов
        except vk_api.exceptions.ApiError as e:
            print(f"Ошибка при получении поста: {e}")
            post = None

        if post and 'attachments' in post:
            # Проходим по всем вложениям
            for attachment in post['attachments']:
                # Если вложение — это фото
                if attachment['type'] == 'photo':
                    # Получаем URL фотографии с максимальным размером
                    photo_url = attachment['photo']['sizes'][-1]['url']
        else:
            return "В посте нет вложений с фотографиями."
    return photo_url


def text_reposts():
    vk_session = vk_api.VkApi(token=key)
    vk = vk_session.get_api()

    for i in group_id:
        try:
            wall_posts = vk.wall.get(domain=i, count=100, filter='owner')['items']
        except ApiError as e:
            print(f"Ошибка при получении постов: {e}")
            wall_posts = []

        for post in wall_posts:
            post_id = post['id']
            reposts = post['reposts']['count']
            slov_ip.update({reposts: post_id})

        sorted_keys = sorted(slov_ip.keys())
        post__idish = slov_ip[sorted_keys[-1]]
        post_id2 = f'{str(group_id[-1])}_{post__idish}'


        try:
            # Получаем информацию о посте
            post = vk.wall.getById(posts=post_id2)[0]  # Метод возвращает список постов
            # Возвращаем количество репостов
            f =  post['reposts']['count']
        except vk_api.exceptions.ApiError as e:
            print(f"Ошибка при получении поста: {e}")
            return None
        except KeyError:
            print("Пост не содержит информации о репостах.")
            return None


        try:
            post = vk.wall.getById(posts=post_id2)[0]  # Метод возвращает список постов
        except vk_api.exceptions.ApiError as e:
            print(f"Ошибка при получении поста: {e}")
            post = None
        if post and 'text' in post and post['text'].strip():
            # Извлекаем текст поста
            post_text = post['text']
            return post_text, f'количестов репостов: {f}'
        else:
            return f"пост без текста, количество репостов: {f}"


def com():
    vk_session = vk_api.VkApi(token=key)
    vk = vk_session.get_api()


    for i in group_id:
        try:
            wall_posts = vk.wall.get(domain=i, count=100, filter='owner')['items']
        except ApiError as e:
            print(f"Ошибка при получении постов: {e}")
            wall_posts = []

        for post in wall_posts:
            post_id = post['id']
            comments = post['comments']['count']
            post_id2 = f'{str(group_id[-1])}_{post_id}'
            slov_ip.update({comments: post_id})

        sorted_keys = sorted(slov_ip.keys())
        post__idish = slov_ip[sorted_keys[-1]]
        post_id2 = f'{str(group_id[-1])}_{post__idish}'

        try:
            post = vk.wall.getById(posts=post_id2)[0]  # Метод возвращает список постов
        except vk_api.exceptions.ApiError as e:
            print(f"Ошибка при получении поста: {e}")
            post = None

        if post and 'attachments' in post:
            # Проходим по всем вложениям
            for attachment in post['attachments']:
                # Если вложение — это фото
                if attachment['type'] == 'photo':
                    # Получаем URL фотографии с максимальным размером
                    photo_url = attachment['photo']['sizes'][-1]['url']
        else:
            return "В посте нет вложений с фотографиями."
    return photo_url


def text_com():
    vk_session = vk_api.VkApi(token=key)
    vk = vk_session.get_api()

    for i in group_id:
        try:
            wall_posts = vk.wall.get(domain=i, count=100, filter='owner')['items']
        except ApiError as e:
            print(f"Ошибка при получении постов: {e}")
            wall_posts = []

        for post in wall_posts:
            post_id = post['id']
            comments = post['comments']['count']
            slov_ip.update({comments: post_id})

        sorted_keys = sorted(slov_ip.keys())
        post__idish = slov_ip[sorted_keys[-1]]
        post_id2 = f'{str(group_id[-1])}_{post__idish}'


        try:
            # Получаем информацию о посте
            post = vk.wall.getById(posts=post_id2)[0]  # Метод возвращает список постов
            # Возвращаем количество репостов
            f =  post['comments']['count']
        except vk_api.exceptions.ApiError as e:
            print(f"Ошибка при получении поста: {e}")
            return None
        except KeyError:
            print("Пост не содержит информации о репостах.")
            return None


        try:
            post = vk.wall.getById(posts=post_id2)[0]  # Метод возвращает список постов
        except vk_api.exceptions.ApiError as e:
            print(f"Ошибка при получении поста: {e}")
            post = None
        if post and 'text' in post and post['text'].strip():
            # Извлекаем текст поста
            post_text = post['text']
            return post_text, f'количестов комментариев: {f}'
        else:
            return f"пост без текста, количество комментариев: {f}"
        
def analiz(post_id):
    vk_session = vk_api.VkApi(token=key)
    vk = vk_session.get_api()
    try:
        # Получаем информацию о посте
        post = vk.wall.getById(posts=post_id)[0]  # Метод возвращает список постов
        # Возвращаем количество репостов
        f_rep =  post['reposts']['count']
    except vk_api.exceptions.ApiError as e:
        print(f"Ошибка при получении поста: {e}")
        return None
    except KeyError:
        print("Пост не содержит информации о репостах.")
        return None

    try:
        # Получаем информацию о посте
        post = vk.wall.getById(posts=post_id)[0]  # Метод возвращает список постов
        # Возвращаем количество репостов
        f_com =  post['comments']['count']
    except vk_api.exceptions.ApiError as e:
        print(f"Ошибка при получении поста: Паблик закрыл доступ к своим постам")
        return None
    except KeyError:
        print("Пост не содержит информации о комментах.")
        return None

    try:
        # Получаем информацию о посте
        post = vk.wall.getById(posts=post_id)[0]  # Метод возвращает список постов
        # Возвращаем количество репостов
        f_like =  post['likes']['count']
    except vk_api.exceptions.ApiError as e:
        print(f"Ошибка при получении поста: {e}")
        return None
    except KeyError:
        print("Пост не содержит информации о лайках.")
        return None
    
    try:
        # Получаем информацию о посте
        post = vk.wall.getById(posts=post_id)[0]  # Метод возвращает список постов
        # Возвращаем количество репостов
        f_v = post.get('views', {}).get('count', 0)
    except vk_api.exceptions.ApiError as e:
        print(f"Ошибка при получении поста: {e}")
        return None
    except KeyError:
        print("Пост не содержит информации о просмотрах.")
        return None
    return f'Просмотры: {f_v}, лайки: {f_like}, Комменты: {f_com}, Репосты: {f_rep}'


def an_photo(post_id):
    vk_session = vk_api.VkApi(token=key)
    vk = vk_session.get_api()
    try:
        post = vk.wall.getById(posts=post_id)[0]  # Метод возвращает список постов
    except vk_api.exceptions.ApiError as e:
        print(f"Ошибка при получении поста: {e}")
        post = None

    if post and 'attachments' in post:
        # Проходим по всем вложениям
        for attachment in post['attachments']:
            # Если вложение — это фото
            if attachment['type'] == 'photo':
                # Получаем URL фотографии с максимальным размером
                photo_url = attachment['photo']['sizes'][-1]['url']
    else:
        return "В посте нет вложений с фотографиями."
    return photo_url


x = the_best()
y = text()
x2 = the_best2()
y2 = text2()
x3 = the_best3()
y3 = text3()
l1 = the_likes()
l2 = text_likes()
r1 = reposts()
r2 = text_reposts()
k1 = com()
k2 = text_com()
an = analiz
ph = an_photo
