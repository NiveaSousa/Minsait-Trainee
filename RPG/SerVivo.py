class SerVivo:
    def __init__(self, pontos_de_vida, pontos_de_ataque):
        self.pontos_de_vida = pontos_de_vida
        self.pontos_de_ataque = pontos_de_ataque


    def atacar(self, personagem_vitima):
        personagem_vitima.sofrer_dano(self.pontos_de_ataque)

    def sofrer_dano(self, dano):
        self.pontos_de_vida -= dano
        

 
