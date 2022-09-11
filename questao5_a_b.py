from PIL import Image


def dilatacao(imagem, elementoEstruturante, coordenadasCentro):
    imagemSaida = Image.new("RGBA", imagem.size, "white")
    for i in range(largura):
        for j in range(altura):
            if imagem.getpixel((i, j)) == (0,0,0,255):
                for k in range(len(elementoEstruturante)):
                    for l in range(len(elementoEstruturante[k])):
                        if elementoEstruturante[k][l] == 1:
                            try:
                                imagemSaida.putpixel((i + k - coordenadasCentro[0],
                                 j + l - coordenadasCentro[1]), (0,0,0,255))
                            except:
                                pass
    return imagemSaida


def erosao(imagem, elementoEstruturante, coordenadasCentro):
    imagemSaida = Image.new("RGBA", imagem.size, "white")
    largura, altura = imagem.size
    for i in range(largura):
        for j in range(altura):
            if imagem.getpixel((i, j)) == (0,0,0,255):
                matchComElementoEstruturante = True
                for k in range(len(elementoEstruturante)):
                    for l in range(len(elementoEstruturante[k])):
                        if elementoEstruturante[k][l] == 1:
                            valorMin = (0,0,0,255)
                            try:
                                valorMin = imagem.getpixel((i + k - coordenadasCentro[0],
                                 j + l - coordenadasCentro[1]))
                            except:
                                pass
                            if valorMin != (0,0,0,255):
                                matchComElementoEstruturante = False
                if matchComElementoEstruturante:
                    imagemSaida.putpixel((i, j), (0,0,0,255))
    return imagemSaida


def fechamento(imagem, elementoEstruturante, coordenadasCentro):
    imagemSaida = dilatacao(imagem, elementoEstruturante, coordenadasCentro)
    imagemSaida = erosao(imagemSaida, elementoEstruturante, coordenadasCentro)

    return imagemSaida

imagemInicial = Image.open('imagens/quadro.png')
imagemOriginal = Image.open('imagens/quadro.png')
elementoEstruturante = [[1,1,1,1,1], [1,1,1,1,1], [1,1,1,1,1], [1,1,1,1,1], [1,1,1,1,1]]
coordenadasCentro = [2, 2]

largura, altura = imagemInicial.size
for i in range(largura):
    for j in range(altura):
        if(imagemInicial.getpixel((i, j)) != (0, 0, 0, 255)):
            imagemInicial.putpixel((i, j), (255, 255, 255, 255))

imagemSaida = fechamento(imagemInicial, elementoEstruturante, coordenadasCentro)

#imagemSaida.show()

for i in range(largura):
    for j in range(altura):
        imagemSaida.putpixel((i,j), (255-imagemSaida.getpixel((i,j))[0],
                             255-imagemSaida.getpixel((i, j))[1],
                             255-imagemSaida.getpixel((i, j))[2], 255))

#imagemSaida.show()

for i in range(largura):
    for j in range(altura):
        if(imagemOriginal.getpixel((i, j)) != (255, 255, 255, 255)):
            imagemSaida.putpixel((i, j), (max(imagemOriginal.getpixel((i, j))[0], imagemSaida.getpixel((i, j))[0]),
                                          max(imagemOriginal.getpixel((i, j))[1], imagemSaida.getpixel((i, j))[1]),
                                          max(imagemOriginal.getpixel((i, j))[2], imagemSaida.getpixel((i, j))[2]),
                                           255))

#imagemSaida.show()

for i in range(largura):
    for j in range(altura):
        if(imagemSaida.getpixel((i, j)) == (0, 0, 0, 255) or imagemSaida.getpixel((i, j)) == (255, 255, 255, 255)):
            imagemSaida.putpixel((i, j), (255-imagemSaida.getpixel((i, j))[0],
                                255-imagemSaida.getpixel((i, j))[1],
                                255-imagemSaida.getpixel((i, j))[2], 255))

imagemSaida.show()
