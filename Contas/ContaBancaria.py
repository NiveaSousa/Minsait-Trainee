class ContaBancaria():

    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Não há saldo")
        

    def consultar_saldo(self):
        print(f"Saldo atual: R$ {self.saldo}")


conta1 = ContaBancaria("Maria", 100)
conta1.depositar(valor = 1000)
conta1.sacar(valor = 80)
print(conta1.consultar_saldo())