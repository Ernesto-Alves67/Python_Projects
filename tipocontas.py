from Re_Classes_exercicios import Conta

class ContaPoupanca(Conta):
    def saque(self, valor):
        if self.saldo < valor:
            print('Saldo insuficiente')
            return
        self.saldo -= valor


class ContaCorrente(Conta):
    def __init__(self,agencia, nam_co, saldo, limite=100):
        super().__init__(agencia, nam_co, saldo)
        self._limite = limite

    @property
    def limite(self):
        return self.limite

    def saque(self, valor):
        if (self.saldo + self.limite) < valor:
            print('saldo insuficiente')
            return
        self.saldo -= valor