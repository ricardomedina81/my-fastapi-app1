from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hola Mundo desde FastAPI en Render"}

@app.get("/msg1")
def read_root():
    return {"message": "Este es un mensaje desde FastAPI en Render"}
