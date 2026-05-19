from fastapi import FastAPI


app = FastAPI(
    title="Restaurant API",
    version="1.0.0"
)



@app.get("/restaurants")
def restaurants(city: str):
    return {"message": "Temporarily not implemented"}


@app.get("/")
def root():
    return {"message": "Service is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
