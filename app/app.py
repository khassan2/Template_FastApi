from fastapi import FastAPI, HTTPException
from app.schemas import Post

app = FastAPI()

text_posts = {
    1: {"title": "ABC", "Description": "XYZ"},
    2: {"title": "FastAPI Guide", "Description": "Interview prep notes"},
    3: {"title": "CI/CD Basics", "Description": "Learning GitHub Actions"},
    4: {"title": "Azure Portal", "Description": "Exploring cloud services"},
    5: {"title": "AWS S3", "Description": "Storage bucket setup"}
}

@app.get("/posts")
def GetPosts(limit: int = None):
    if limit:
        return list(text_posts.values())[:limit]
    return text_posts


@app.get("/posts/{id}")
def GetPost(id: int):
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not found")
    return text_posts.get(id)


@app.post("/posts")
def CreatePost(post: Post):
    new_post = {"Title": post.Title, "Description": post.Description}
    text_posts[max(text_posts.keys()) +1] = new_post
    return new_post
