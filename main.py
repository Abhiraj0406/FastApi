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

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p

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

@app.get("/posts/largest")
def get_letest_post():
    post = my_posts[len(my_posts)-1]
    return {"detail": post}

@app.get("/posts/{id}")
def get_post(id: int):
    # print(id)
    # return {"post_detail": f"here is post {id}"}
    print(type(id))
    post = find_post(id)
    print(post)
    return {"post_detail": post}

