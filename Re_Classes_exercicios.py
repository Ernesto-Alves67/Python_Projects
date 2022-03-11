"""
1 Classe Bola: Crie uma classe que modele uma bola:

    Atributos: Cor, circunferência, material
    Métodos: trocaCor e mostraCor

2 Classe Quadrado: Crie uma classe que modele um quadrado:

    Atributos: Tamanho do lado
    Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

5: Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. A classe deve possuir os
seguintes atributos: número da conta, nome do correntista e saldo. Os métodos são os seguintes: alterarNome,
depósito e saque; No construtor,
saldo é opcional, com valor default zero e os demais atributos são obrigatórios.
"""

# Ex: 1
from abc import ABC, abstractmethod
class BolaDiferente:
    def __init__(self, nome, cor, cfr, material):
        self.nome = nome
        self.cor = cor
        self.circun = cfr
        self.material = material
        self.dados = {'nome': nome, 'cor': cor, 'circun': cfr, 'material': material}
    def mudacor(self, cor_1):
        self.cor = cor_1
        return
    def mostracor(self):
        corb = self.cor
        return corb
    def mostradados(self):
        valor = self.dados.values()
        return valor
    def imprime(self, valor):
        for l in valor:
            print(l)

# Ex: 2
class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def mudalado(self, lado):
        self.lado = lado
        self.area = lado**2
        return self.lado, self.area

# Ex: 5
class Conta(ABC):
    def __init__(self, agencia, nam_co, saldo):
        self._saldo = saldo
        self._agencia = agencia
        self._nome = nam_co

    def alteranome(self, nome):
        self._nome = nome
        return self._nome
    @property
    def saldo(self):
        return self._saldo
    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError('Saldo precisa ser numerico')
        self._saldo = valor
    def deposito(self, valor):
        self._saldo += valor
        return self._saldo

    @abstractmethod
    def saque(self, valor):
        self._saldo -= valor
        return self._saldo
# Ex: 6
class macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    # metodos
    def comer(self, food):
        if type(food) == str:
            self.bucho.append(food)
        else:
            print('Alimento invalido')

    def ver_estomago(self):
        if len(self.bucho) == 0:
            return 'Estomago vazio'
        else:
            return self.bucho

    def digerir(self):
        self.bucho.clear()


