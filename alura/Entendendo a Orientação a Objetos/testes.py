"""
from datas import Data

data = Data(22, 10, 1995)
print(data)
"""

from conta import Conta

conta1 = Conta(123, 'Luccas', 1000, 1000)
conta2 = Conta(321, 'Day', 1000, 1000)

print(conta1.extrato)
print(conta2.extrato)

conta2.transferir(500, conta1)
print(conta2.extrato)
print(conta1.extrato)

conta2.transferir(500, conta1)
print(conta2.extrato)
print(conta1.extrato)

conta2.transferir(500, conta1)
print(conta2.extrato)
print(conta1.extrato)

conta2.transferir(500, conta1)
print(conta2.extrato)
print(conta1.extrato)

conta2.transferir(500, conta1)

codigo = Conta.codigoBancos()
print(codigo)
print(codigo['Santander'])
