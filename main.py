from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

my_posts = [{"title": "title of post 1", "content": "content of post 1", "id":1}, {"title": "fsvorite foods", "content": "I like pizza", "id": 2}]

@app.get("/")       #decorater
def root():
    return {"message": "Hello World"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}

@app.post("/createposts")

# def create_posts(payLoad: dict = Body(...)):
#     print(payLoad)
#     return {"new_post": f"tittle {payLoad['tittle']} content: {payLoad['content']}"}

def create_post(post: Post):
    # print(post.published)
    # print(post.rating)
    # print(post.dict())

    post_dict = post.dict()
    post_dict['id'] = randrange(0, 100000)
    my_posts.append(post_dict)
    return {"data": post_dict}