class Produto:
    def __init__(self, nome, preco_unitario, quantidade):
        self.nome = nome
        self.preco_unitario = preco_unitario
        self.quantidade = quantidade
        self.preco_total = self.preco_unitario * self.quantidade

    def __str__(self):
        return f'{self.nome} - R$ {self.preco_unitario} - {self.quantidade} unidades em estoque'

