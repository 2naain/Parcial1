from enum import Enum, auto
from pydantic import BaseModel

class Material(Enum):
    BRONCE = auto()
    PLATA = auto()
    ORO = auto()


class Caballero(BaseModel):
    id: int
    name: str
    material: Material
    attack: int
    constelation: str

    def showcaballero(self):
        return f"Caballero {self.name} con armadura {self.material.name}"

    def fightcaballero(self):
        return f"{self.name} ataca con poder {self.attack}"

    def showconstelation(self):
        return f"Constelación: {self.constelation}"
    s