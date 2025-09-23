from fastapi import FastAPI, HTTPException
from app import soma, media

app = FastAPI(title="Fluxo CI/CD DevOps")

@app.get("/")
def root():
    return {"status": "ok"}

@app.get("/soma")
def soma_endpoint(a: float, b: float):
    return {"resultado": soma(a, b)}

@app.get("/media")
def media_endpoint(valores: str):
    # exemplo: valores=2,4,6
    try:
        nums = [float(x) for x in valores.split(",") if x.strip() != ""]
    except ValueError:
        raise HTTPException(status_code=400, detail="valores deve conter números separados por vírgula")
    if not nums:
        raise HTTPException(status_code=400, detail="lista vazia")
    return {"resultado": media(nums)}
