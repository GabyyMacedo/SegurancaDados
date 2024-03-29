from hashlib import sha256

class Senhas:

    def __init__(self,senha):
        cripto=sha256(senha.encode()).hexdigest()
        senhaComp=0
        senhaSt=str(senhaComp)
        while sha256(senhaSt.encode()).hexdigest()!=cripto:
            senhaComp=senhaComp+1
            senhaSt=str(senhaComp)
        self.senha=senhaComp 

    def exibir(self):
        return f"\nAção concluída!\nA senha é: {self.senha}"
    
senha=(input("Digite a senha que será descriptografada: "))
c1=Senhas(senha)
print(c1.exibir())
