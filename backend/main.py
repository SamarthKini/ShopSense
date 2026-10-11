from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "This is ShopSense. A landing page will soon be here."}