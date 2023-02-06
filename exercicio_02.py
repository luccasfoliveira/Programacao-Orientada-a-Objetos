"""
Criar uma classe "Conta Bancária" que tenha atributos: nome do titular, número da conta e saldo,
e métodos para depositar e retirar dinheiro.
"""


class ContaBancaria:
    def __init__(self, titular, conta, saldo):
        self.titular = titular
        self.conta = conta
        self.saldo = saldo

    def depositar(self, dinheiro):
        """
        :param dinheiro: float
        :return: adiciona dinheiro na conta
        """
        self.saldo += dinheiro

    def sacar(self, dinheiro):
        """
        :param dinheiro: float
        :return: retira dinheiro, se houver saldo
        """
        if self.saldo >= dinheiro:
            self.saldo -= dinheiro
        elif self.saldo < dinheiro:
            print('Saldo Insuficiente')

    def extrato(self):
        """
        :return: mostra as caracteristicas da conta
        """
        return f'Nome: {self.titular}\n' \
               f'Conta: {self.conta}\n' \
               f'Saldo: {self.saldo}'


cliente1 = ContaBancaria('Luccas', '1234-5', 1500.)
cliente1.depositar(230.)
print(cliente1.extrato())
cliente1.sacar(1800.)
cliente1.sacar(430.)
print(cliente1.extrato())
