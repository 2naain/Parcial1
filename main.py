from fastapi import FastAPI
from models import Caballero
from models import Material
app = FastAPI()


caballeros = [
    Caballero(id=1, name="Nameless King", material=Material.BRONCE, attack=250000, constelation="Pico del archidragon"),
    Caballero(id=2, name="Orstein", material=Material.PLATA, attack=300000, constelation="Anor londo"),
    Caballero(id=3, name="Fortissax", material=Material.ORO, attack=100000, constelation="Raiz profunda"),
]



@app.get("/showallcaballeros")
def show_all_caballeros():
    return [caballero.showcaballero() for caballero in caballeros]


@app.get("/showyourcaballero/{caballero_id}")
def show_your_caballero(caballero_id: int):
    for caballero in caballeros:
        if caballero.id == caballero_id:
            return caballero.showcaballero()
    return {"error": "Caballero no encontrado"}


@app.get("/fightcaballero/{caballero_id}")
def fight_caballero(caballero_id: int):
    for caballero in caballeros:
        if caballero.id == caballero_id:
            return caballero.fightcaballero()
    return {"error": "Caballero no encontrado"}


@app.get("/showconstelation/{caballero_id}")
def show_constelation(caballero_id: int):
    for caballero in caballeros:
        if caballero.id == caballero_id:
            return caballero.showconstelation()
    return {"error": "Caballero no encontrado"}


