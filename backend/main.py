from fastapi import FastAPI

app = FastAPI(title="Climate Pollinator Explorer API")

@app.get("/health")
def health():
    return {"status": "ok"}