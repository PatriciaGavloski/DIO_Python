class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome 
        self.idade = idade


    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia , nome):
        idade = 2024 - ano
        return cls(nome, idade)
    
    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18
     
# p = Pessoa("Patricia", 30)
# print(p.nome, p.idade)
    
p = Pessoa.criar_de_data_nascimento(1994, 7, 12, "Patricia")
print(p.nome, p.idade)

print(Pessoa.e_maior_idade(18))
print(Pessoa.e_maior_idade(8))