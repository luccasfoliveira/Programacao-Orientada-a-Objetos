"""
Criar uma classe "Veículo" que tenha atributos marca, modelo, ano de fabricação e velocidade,
e métodos para acelerar e frear.
"""


class Veiculo:
    def __init__(self, marca, modelo, ano, velocidade):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = velocidade

    def acelerar(self, valor):
        """
        :param valor: float
        :return: incrementa a velocidade,
        se não houver ultrapassado 220
        """
        if self.velocidade + valor <= 220:
            self.velocidade += valor
        else:
            print('Você está muito rápido')
            self.velocidade = 220

    def frear(self, valor):
        """
        :param valor: float
        :return: decrementa a velocidade,
        se não houver ultrapassado 0
        """
        if self.velocidade - valor >= 0:
            self.velocidade -= valor
        else:
            self.velocidade = 0

    def mostrar_velocidade(self):
        """
        :return: valocidade
        """
        print('Velocidade:', self.velocidade)


veiculo = Veiculo('GM', 'Celta', '2001', 150.)
veiculo.mostrar_velocidade()

veiculo.acelerar(80)
veiculo.mostrar_velocidade()

veiculo.frear(150)
veiculo.mostrar_velocidade()

veiculo.acelerar(42)
veiculo.mostrar_velocidade()
