from PIL import Image

def dilatacao(imagem, elementoEstruturante, coordenadasCentro):
    imagemSaida = Image.new("L", imagem.size)
    largura,altura = imagem.size
    for i in range(largura):
        for j in range(altura):
            if imagem.getpixel((i,j)) == 255:
                for k in range(len(elementoEstruturante)):
                    for l in range(len(elementoEstruturante[k])):
                        if elementoEstruturante[k][l] == 1:
                            imagemSaida.putpixel((i + k - coordenadasCentro[0], j + l - coordenadasCentro[1]), 255)
    return imagemSaida


def erosao(imagem, elementoEstruturante, coordenadasCentro):
    imagemSaida = Image.new("L", imagem.size)
    largura, altura = imagem.size
    for i in range(largura):
        for j in range(altura):
            if imagem.getpixel((i,j)) == 255:
                matchComElementoEstruturante = True
                for k in range(len(elementoEstruturante)):
                    for l in range(len(elementoEstruturante[k])):
                        if elementoEstruturante[k][l] == 1:
                            if imagem.getpixel((i + k - coordenadasCentro[0], j + l - coordenadasCentro[1])) != 255:
                                matchComElementoEstruturante = False
                if matchComElementoEstruturante:
                    imagemSaida.putpixel((i,j), 255)
    return imagemSaida
                
def abertura(imagem, elementoEstruturante, coordenadasCentro):
    imagemSaida = erosao(imagem, elementoEstruturante, coordenadasCentro)
    imagemSaida = dilatacao(imagemSaida, elementoEstruturante, coordenadasCentro)

    return imagemSaida


def fechamento(imagem, elementoEstruturante, coordenadasCentro):
    imagemSaida = dilatacao(imagem, elementoEstruturante, coordenadasCentro)
    imagemSaida = erosao(imagemSaida, elementoEstruturante, coordenadasCentro)

    return imagemSaida

                

imagem1 = Image.open("imagens/imagemTeste2.bmp").convert("L")
#diferenca = Image.new("L", imagem1.size)

elementoEstruturante = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
coordenadasCentro = [1, 1]
#imagemSaida = dilatacao(imagem1, elementoEstruturante, coordenadasCentro)
#imagemSaida = erosao(imagem1, elementoEstruturante, coordenadasCentro)
#imagemSaida = abertura(imagem1, elementoEstruturante, coordenadasCentro)
imagemSaida = fechamento(imagem1, elementoEstruturante, coordenadasCentro)

imagemSaida.show()
