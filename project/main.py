import os
from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from vk_utils import get_vk_posts, sort_posts_by_likes, sort_posts_by_reposts, sort_posts_by_comments  # Импортируем функцию для получения постов

app = FastAPI()

# Получаем абсолютный путь к папке static
static_path = str(Path(__file__).parent / "static")
if not os.path.exists(static_path):
    os.makedirs(static_path)  # Создаём папку, если её нет

# Монтируем статические файлы (CSS)
app.mount("/static", StaticFiles(directory=static_path), name="static")

# Настраиваем шаблонизатор Jinja2
templates = Jinja2Templates(directory=str(Path(__file__).parent / "templates"))

# Главная страница
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Страница "О нас"
@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})

# Страница контактов
@app.get("/contact", response_class=HTMLResponse)
async def contact(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request})

@app.get("/vk-posts", response_class=HTMLResponse)
async def vk_posts(request: Request, sort_by: str = "default"):
    group_ids = [45045130, 153354594, 98581330, 92337511]  # ID групп ВКонтакте
    posts = get_vk_posts(group_ids)

    # Сортируем посты в зависимости от параметра sort_by
    if sort_by == "likes":
        posts = sort_posts_by_likes(posts)
    elif sort_by == "reposts":
        posts = sort_posts_by_reposts(posts)
    elif sort_by == "comments":
        posts = sort_posts_by_comments(posts)

    return templates.TemplateResponse("vk_posts.html", {"request": request, "posts": posts, "sort_by": sort_by})

@app.get("/telegram-bot", response_class=HTMLResponse)
async def telegram_bot(request: Request):
    return templates.TemplateResponse("telegram_bot.html", {"request": request})