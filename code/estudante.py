from pessoa import Pessoa


class Estudante(Pessoa):
    def __init__(self, nome, peso, altura, genero, data_nascimento, matricula):
        super().__init__(nome, peso, altura, genero, data_nascimento)
        self.__matricula = matricula

    def get_matricula(self):
        return self.__matricula

    def set_matricula(self, nova_matricula):
        self.__matricula = nova_matricula
        
        # Método obter dados
    def obter_dados(self):
        return {
            "Nome": self.get_nome(),
            "Peso": self.get_peso(),
            "Altura": self.get_altura(),
            "Gênero": self.get_genero(),
            "Data de Nascimento": self.get_data_nascimento(),
            "Matrícula": self.get_matricula()
        }