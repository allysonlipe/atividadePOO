from pessoa import Pessoa


class Professor(Pessoa):
    def __init__(self, nome, peso, altura, genero, data_nascimento, disciplina):
        super().__init__(nome, peso, altura, genero, data_nascimento)
        self.__disciplina = disciplina

    def get_disciplina(self):
        return self.__disciplina

    def set_disciplina(self, nova_disciplina):
        self.__disciplina = nova_disciplina

        # Método obter dados
    def obter_dados(self):
        return {
            "Nome": self.get_nome(),
            "Peso": self.get_peso(),
            "Altura": self.get_altura(),
            "Gênero": self.get_genero(),
            "Data de Nascimento": self.get_data_nascimento(),
            "Matrícula": self.get_disciplina()
        }
