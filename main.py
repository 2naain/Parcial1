from fastapi import FastAPI
from models import Caballero

app = FastAPI()


caballeros = []



@app.get("/showallcaballeros")
def showallcaballeros():
    return [c.showcaballero() for c in caballeros]

@app.get("/showyourcaballero/{id}")
def showyourcaballero(id: int):
    for c in caballeros:
        if c.id == id:
            return c.showcaballero()
    return {"error": "Caballero no encontrado"}

@app.get("/fightcaballero/{id}")
def fightcaballero(id: int):
    for c in caballeros:
        if c.id == id:
            return c.fightcaballero()
    return {"error": "Caballero no encontrado"}

@app.get("/showconstelation/{id}")
def showconstelation(id: int):
    for c in caballeros:
        if c.id == id:
            return c.showconstelation()
    return {"error": "Caballero no encontrado"}


