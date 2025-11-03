from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Welcome to the home screen!", "health_url": "/health"}


@app.get("/health")
def health():
    return {"status": "ok"}
