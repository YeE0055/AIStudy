from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{user_id}/items/")
async def get_user_item(
    user_id: int,
    keyword: str | None = None,
    page: int = 1,
):
    return {
        "user_id": user_id,
        "keyword": keyword,
        "page": page,
    }
