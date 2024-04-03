from backend.api.api import app

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/status")
async def status():
    return {"message": "Hello World, Test"}