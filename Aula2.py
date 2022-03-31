


class Quarto:
    def __init__(self, nome = "", dimensoes = "") :
        self.nome = nome
        self.dimensoes = dimensoes

    def __str__(self):
        texto = "Quarto:" + self.nome + "," + self.dimensoes
        return texto

class Casa:
    def __init__(self, formato = "", quartos = None):
        self.formato = formato
        self.quartos = quartos

    def adicionar_quarto(self):
        nome_quarto = input("Nome do comodo:")
        dimensoes_quarto = input("Dimensoes (larg x comp): ")

        return [nome_quarto, dimensoes_quarto]

    def __str__(self):
        texto = "Casa:" + self.formato
        try:
            if self.quartos is None:
                raise "Uma casa precisa ter pelo menos um quarto"
            else:
                for quarto in self.quartos:
                    texto += "," + str(quarto)
                
        except:
            infos = self.adicionar_quarto()
            self.quartos = []
            self.quartos.append(Quarto(infos[0], infos[1]))
        return texto 
        
    
class Mobilia:
    def __init__(self, nome = "", funcao = "", material = "", quarto = Quarto): 
        self.nome = nome
        self.funcao = funcao
        self.material = material
        self.quarto = quarto

    def __str__(self):
        texto = "Mobilia:" + self.nome+ "," + self.funcao + "," + self.material
        if self.quarto:
            texto += str(self.quarto)

        return texto


if __name__ == "__main__":
    q1 = Quarto(nome="Sala", dimensoes="6x5 metros")
    print(q1)

    m1 = Mobilia(nome = "Armario", funcao = "Guardar coisas", material = "Madeira", quarto=q1) # quarto eh opcional
    print(m1)

    q2 = Quarto(nome="Banheiro", dimensoes="3x4 metros")
    c1 = Casa(formato="Germanica")
    print(c1)
        
        