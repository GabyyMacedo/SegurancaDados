class Veiculos:
    def __init__(self, marca, ano, preco):
        self.marca=marca
        self.ano=ano
        self.preco=preco
    
    def info(self):
        return f"Marca: {self.marca}, ano: {self.ano}, preço: R${self.preco}"
    
class Carro(Veiculos):
    def __init__(self, marca, ano, preco, modelo, potencia):
        self.model=modelo
        self.pot=potencia
        super().__init__(marca, ano, preco)

    def info(self):
        return super().info()+f", modelo: {self.model}, potência: {self.pot} cavalos"
    
class Moto(Veiculos):
    def __init__(self, marca, ano, preco, cilindrada):
        self.cilin=cilindrada
        super().__init__(marca, ano, preco)
    
    def info(self):
        return super().info()+f", cilindrada: {self.cilin} cc"