from fastapi import FastAPI

app=FastAPI(title="DocQ API")

@app.get("/health")
def health_check():
    return {"status":"healthy"}