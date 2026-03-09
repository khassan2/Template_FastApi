from fastapi import FastAPI, HTTPException

app = FastAPI()

posts = {
    1: {"title": "ABC", "Description": "XYZ"},
    2: {"title": "FastAPI Guide", "Description": "Interview prep notes"},
    3: {"title": "CI/CD Basics", "Description": "Learning GitHub Actions"},
    4: {"title": "Azure Portal", "Description": "Exploring cloud services"},
    5: {"title": "AWS S3", "Description": "Storage bucket setup"}
}

@app.get("/posts")
def get_posts(limit: int = None):
    if limit:
        return list(posts.values())[:limit]
    return posts


@app.get("/posts/{id}")
def get_posts_by_id(id: int):
    if id not in posts:
        raise HTTPException(status_code=404, detail="Post not found")
    return posts.get(id)
