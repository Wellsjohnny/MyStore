class Cliente:
    def __init__(self, nome, email, endereco):
        self.nome = nome
        self.email = email
        self.endereco = endereco

    def __str__(self):
        return f'{self.nome} - {self.email} - {self.endereco}'