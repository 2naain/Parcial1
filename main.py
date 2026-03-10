from fastapi import FastAPI
from models import Caballero

app = FastAPI()


caballeros = []



@app.post("/caballero")
def create_caballero(c: Caballero):
    caballeros.append(c)
    return {"message": f"Caballero {c.name} creado"}

@app.get("/showallcaballeros")
def showallcaballeros():
    return [c.showcaballero() for c in caballeros]

