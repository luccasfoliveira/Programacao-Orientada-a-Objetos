class Produto:
    def __init__(self, nome, descricao, preco, quantidade):
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.quantidade = quantidade

    def calcular_preco_em_estoque(self):
        return self.preco * self.quantidade

    def vender(self, quantidade):
        if quantidade <= self.quantidade:
            self.quantidade -= quantidade
            return True
        else:
            return False

    