from datetime import datetime
class Pessoa_Model_1:
    Ano_a = int(datetime.strftime(datetime.now(), '%Y'))
    def __init__(self, nome, idade, comendo=False, falando=False, dormindo=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
        self.dormindo = dormindo

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} ja esta comendo')
            return
        print(f'{self.nome} esta comendo {alimento}')
        self.comendo = True
    def ano_nacido(self):
        ano_nacimento = (self.Ano_a - self.idade)
        return ano_nacimento
    def dormir(self,Acao):
        if self.dormindo and Acao == 'dormir':
            print(f'{self.nome} Ja esta dormindo')
            return
        else:
            if Acao == 'dormir':
                self.dormindo = True
                print(f'{self.nome} esta dormindo')
                return
            elif Acao == 'acordar':
                self.dormindo = False
                print(f'{self.nome} esta acordado')
                return


class Operacoes:
    def soma(self, a, b):
        soma = int(a) + int(b)
        return soma
    def mult(self, a, b):
        result = int(a) * int(b)
        return result