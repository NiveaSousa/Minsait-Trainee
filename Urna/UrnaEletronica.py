class UrnaEletronica:
    def __init__(self):
        self.candidatos = [{"nome_candidato": "eu", "partido" : "depressao"}, {"nome_candidato": "amiga", "partido" : "ansiedade"}]


    def exibe_candidatos(self):
        for candidato in self.candidatos:
            print(candidato.get("nome_candidato"))
            print(candidato.get("partido"))

    def add_novo_candidato(self, nome_candidato, partido):
        self.candidatos.append({"nome_candidato": nome_candidato , "partido" : partido})
    


urna1 = UrnaEletronica()

urna1.add_novo_candidato()
urna1.exibe_candidatos()