"""
Criar uma classe "Pessoa" que tenha atributos nome, idade e endereço e métodos para retornar esses valores.
"""


class Pessoa:
    def __init__(self, nome, idade, endereco):
        """
        :param nome: str
        :param idade: int
        :param endereco: str
        """
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def retornar_nome(self):
        """
        :return: nome
        """
        return self.nome

    def retornar_idade(self):
        """
        :return: idade
        """
        return self.idade

    def retornar_endereco(self):
        """
        :return: endereço
        """
        return self.endereco

    def mudar_nome(self, nome):
        """
        :param nome: str
        :return: apenas altera o nome
        """
        self.nome = nome


pessoa1 = Pessoa('Luccas', 27, 'Rua José Augusto Escobar')
print(pessoa1.retornar_nome())
print(pessoa1.retornar_endereco())
print(pessoa1.retornar_idade())
pessoa1.mudar_nome('Luccas Oliveira')
print(pessoa1.retornar_nome())
