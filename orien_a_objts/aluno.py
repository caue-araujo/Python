class aluno:
    
    def __init__(self, matricula, nome):
        if len(matricula) != 8:
            raise ValueError("Matrícula inválida")
        matricula = int(matricula)
        self.matricula = matricula
        self.nome = nome
        self.notas = []

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome):
        if type(nome) != str:
            return
        self.__nome = nome
    
    def getMatriculaFormatada(self):
        self.matricula = str(self.matricula)
        return f'{self.matricula[:4]}.{self.matricula[4:5]}.{self.matricula[5:]}'


    def media(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)
    
    def adicionarNotas(self, outraNota):
        if type(outraNota) == bool or type(outraNota) == str:
            return
        self.notas.append(outraNota) 