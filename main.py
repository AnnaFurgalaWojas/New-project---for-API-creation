from fastapi import FastAPI
from Function import calculator

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API działa!"}

@app.get("/add")
def calculator(a: int, b: int, sign= str ):
    result = calculator(a, b,sign)
    return {"result": result}