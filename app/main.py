from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Welcome to Bookly 🚀"}

@app.get("/about")
def about():
    return {
    "project": "Bookly",
    "version": "1.0"
}

@app.get("/health")
def health():
    return {
    "status": "healthy"
}
