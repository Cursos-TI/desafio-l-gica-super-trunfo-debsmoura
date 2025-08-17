class Carta:
    def __init__(self, nome, forca, velocidade, inteligencia, resistencia):
        self.nome = nome
        self.forca = forca
        self.velocidade = velocidade
        self.inteligencia = inteligencia
        self.resistencia = resistencia

    def atributos(self):
        return {
            "forca": self.forca,
            "velocidade": self.velocidade,
            "inteligencia": self.inteligencia,
            "resistencia": self.resistencia
        }
