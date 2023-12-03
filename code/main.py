from pessoa import Pessoa
from estudante import Estudante
from professor import Professor

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

# Interagindo com a classe Estudante

# Criando um objeto Estudante
estudante = Estudante("Zezin", 70, 1.80, "Masculino", "2000-01-01", "123456")

# Definindo uma nova matricula usando o setter
estudante.set_matricula(78910)

#Obtendo uma nova metricula usando o metodo getter
estudante.get_matricula() #Saída: 78910

# Obtendo os dados do estudante
dados_estudante = estudante.obter_dados()

# Imprimindo os dados
print(dados_estudante)


# Interagindo com a classe Professor

# Criando um objeto Professor
professor = Professor("Mariazinha", 45, 1.50, "Feminino", "1999-09-09", "Fundamentos de programação")

# Definindo uma nova disciplina usando o setter
professor.set_disciplina("POO")

#Obtendo uma nova metricula usando o metodo getter
professor.get_disciplina() #Saída: POO

# Obtendo os dados do professor
dados_prof = professor.obter_dados()

# Imprimindo os dados
print(dados_prof)