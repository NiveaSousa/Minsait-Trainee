from SerVivo import SerVivo

class Personsagem(SerVivo):

    def __init__(self, pontos_de_vida, pontos_de_ataque, nome):
        super().__init__(pontos_de_vida, pontos_de_ataque)
        self.nome = nome

        