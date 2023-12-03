# Criando uma instância da classe Pessoa
pessoa = Pessoa("Allyson", 27, 1.80, "Masculino", "1996-11-06")

# Obtendo o nome usando o getter
print(pessoa.get_nome())  # Saída: Allyson

# Definindo um novo peso usando o setter
pessoa.set_peso(70)

# Obtendo o novo peso usando o getter
print(pessoa.get_peso())  # Saída: 70

# Obtendo dados a partir da função obter_dados()
dados = pessoa.obter_dados()
print(dados)