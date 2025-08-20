from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from Function import calculator  # import Twojej funkcji

app = FastAPI()

# Model danych wejściowych (żeby API wiedziało czego się spodziewać)
class CalcRequest(BaseModel):
    a: float
    b: float
    sign: str

@app.post("/calculate")
def calculate(data: CalcRequest):
    try:
        result = calculator(data.a, data.b, data.sign)
        return {"result": result}
    except ZeroDivisionError:
        raise HTTPException(status_code=400, detail="Dzielenie przez zero")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
