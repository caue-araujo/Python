class Data:

    def __init__(self, dia, mes, ano=2023):
        if  dia < 1 or dia > 31:
           return
        if mes < 1 or mes > 12:
            return
        if ano < 1:
            return

        self.dia = dia
        self.mes = mes
        self.ano = ano

    @property
    def dia(self):
        return self.__dia

    @dia.setter
    def dia(self, dia):
        if  dia < 1 or dia > 31:
            return
            
        self.__dia = dia

    @property
    def mes(self):
        return self.__mes

    @mes.setter
    def mes(self, mes):
        if  mes < 1 or mes > 12:
            return
        
        self.__mes = mes

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano):
        if ano < 1:
            return
        self.__ano = ano

    def __str__(self):
        return f"{self.dia:02d}/{self.mes:02d}/{self.ano}"

    def setData(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
