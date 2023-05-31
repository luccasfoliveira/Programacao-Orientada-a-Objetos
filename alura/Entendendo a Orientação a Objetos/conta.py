class Conta:
    def __init__(self, numero: str, titular: str, saldo: float, limite: float):
        print(f"Construindo objeto ... {self}")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    @property
    def extrato(self) -> str:
        return f'\nTitular: {self.__titular}\n' \
               f'Saldo: {self.__saldo:.2f}\n' \
               f'Limite: {self.__limite:.2f}'

    def depositar(self, valor) -> None:
        self.__saldo += valor

    def __podeSacar(self, valor_sacar: float) -> bool:
        valor_disponivel_sacar = self.__saldo + self.__limite
        if valor_sacar <= valor_disponivel_sacar:
            self.__saldo -= valor_sacar
            if self.__saldo < 0:
                self.__limite += self.__saldo
                self.__saldo = 0
            return True
        return False

    def sacar(self, valor: float) -> None:
        if self.__podeSacar(valor):
            print('Operação Realizada')
        else:
            print('\nSaldo Insuficiente...')

    def transferir(self, valor: float, destino: type['Conta']) -> None:
        if self.__podeSacar(valor):
            destino.depositar(valor)
            print('Transferência Realizada')
        else:
            print('\nSaldo Insuficiente...')

    @property
    def numero(self) -> str:
        return self.__numero

    @property
    def titular(self) -> str:
        return self.__titular

    @property
    def saldo(self) -> float:
        return self.__saldo

    @property
    def limite(self) -> float:
        return self.__limite

    @limite.setter
    def limite(self, novoLimite: float) -> None:
        self.__limite = novoLimite

    @staticmethod
    def codigo() -> str:
        return "033"

    @staticmethod
    def codigoBancos() -> dict:
        return {"Banco do Brasil": "001", "Caixa": "104", "Bradesco": "237", "Santander": "033"}
