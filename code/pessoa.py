class Pessoa:
    def __init__(self, nome, peso, altura, genero, data_nascimento):
        self.__nome = nome
        self.__peso = peso
        self.__altura = altura
        self.__genero = genero
        self.__data_nascimento = data_nascimento

    # Getters e setters para o atributo nome
    def get_nome(self):
        return self.__nome

    def set_nome(self, novo_nome):
        self.__nome = novo_nome

    # Getters e setters para o atributo peso
    def get_peso(self):
        return self.__peso

    def set_peso(self, novo_peso):
        self.__peso = novo_peso

    # Getters e setters para o atributo altura
    def get_altura(self):
        return self.__altura

    def set_altura(self, nova_altura):
        self.__altura = nova_altura

    # Getters e setters para o atributo genero
    def get_genero(self):
        return self.__genero

    def set_genero(self, novo_genero):
        self.__genero = novo_genero

    # Getters e setters para o atributo data_nascimento
    def get_data_nascimento(self):
        return self.__data_nascimento

    def set_data_nascimento(self, nova_data_nascimento):
        self.__data_nascimento = nova_data_nascimento

    # Método obter dados
    def obter_dados(self):
        return {
            "Nome": self.get_nome(),
            "Peso": self.get_peso(),
            "Altura": self.get_altura(),
            "Gênero": self.get_genero(),
            "Data de Nascimento": self.get_data_nascimento()
        }
