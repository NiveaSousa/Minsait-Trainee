from Goblin import Goblin
from Lobo import Lobo

lobo = Lobo(900, 5, "Baixo", 300)
goblin = Goblin(1000, 10, "Alto", 200)
goblin.atacar(lobo)

print(lobo.pontos_de_vida)
    