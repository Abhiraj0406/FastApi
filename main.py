from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

@app.get("/")       #decorater
def root():
    return {"message": "Hello World"}

@app.get("/posts")
def get_posts():
    return {"data": "This is your posts"}

@app.post("/createposts")

# def create_posts(payLoad: dict = Body(...)):
#     print(payLoad)
#     return {"new_post": f"tittle {payLoad['tittle']} content: {payLoad['content']}"}

def create_post(post: Post):
    # print(post.published)
    # print(post.rating)
    print(post.dict())
    return {"data": post}