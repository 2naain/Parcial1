from fastapi import FastAPI
from models import Caballero

app = FastAPI()


caballeros = []



@app.get("/showallcaballeros")
def showallcaballeros():
    return [c.showcaballero() for c in caballeros]

