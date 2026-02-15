from fastapi import FastAPI

app = FastAPI()

@app.get("/test")
def test():
    return {"message": "This is a test endpoint"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/")
def root():
    return {"hello": "buildpacks"}
