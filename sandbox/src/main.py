from fastapi import FastAPI

from sandbox.routers.coffee_router import router as coffee_router

app = FastAPI(title="test api")

@app.get("/")
def read_root():
    return {"status": "работает", "title": app.title}

app.include_router(coffee_router)
