from fastapi import FastAPI, HTTPException, File, UploadFile, Form, Depends
from app.schemas import PostRequest, PostResponse
from app.db import Post, create_db_and_tables, get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield
    

app = FastAPI(lifespan=lifespan)


@app.post("/upload")
async def upload_file(file: UploadFile = File(...), caption: str = Form(""), session: AsyncSession = Depends(get_async_session)):
    post = Post(
        caption = caption,
        url="dummy url",
        file_type=".jpg",
        file_name="dummy_file"
        )
    
    session.add(post)
    await session.commit()
    await session.refresh(post)
    return post


@app.get("/feed")
async def get_feed(session: AsyncSession = Depends(get_async_session)):
    result = await session.execute(select(Post).order_by(Post.created_at.desc()))
    posts = [row[0] for row in result.all()]

    post_data = []
    for post in posts:
        post_data.append(
            {
                "id": str(post.id),
                "caption": post.caption,
                "url": post.url,
                "file_type": post.file_type,
                "file_name": post.file_name,
                "created_at": post.created_at.isoformat()
            }

        )

    return {"posts": post_data}









# text_posts = {
#     1: {"title": "ABC", "Description": "XYZ"},
#     2: {"title": "FastAPI Guide", "Description": "Interview prep notes"},
#     3: {"title": "CI/CD Basics", "Description": "Learning GitHub Actions"},
#     4: {"title": "Azure Portal", "Description": "Exploring cloud services"},
#     5: {"title": "AWS S3", "Description": "Storage bucket setup"}
# }

# @app.get("/posts")
# def GetPosts(limit: int = None):
#     if limit:
#         return list(text_posts.values())[:limit]
#     return text_posts


# @app.get("/posts/{id}")
# def GetPost(id: int) -> PostResponse:
#     if id not in text_posts:
#         raise HTTPException(status_code=404, detail="Post not found")
#     return text_posts.get(id)


# @app.post("/posts")
# def CreatePost(post: PostRequest) -> PostResponse:
#     new_post = {"Title": post.Title, "Description": post.Description}
#     text_posts[max(text_posts.keys()) +1] = new_post
#     return new_post
