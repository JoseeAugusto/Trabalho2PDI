from PIL import Image

def uniao(imagem1, imagem2):
    imagemSaida = Image.new("L", imagem1.size)
    largura, altura = imagem1.size
    for i in range(largura):
        for j in range(altura):
            imagemSaida.putpixel((i,j), max(imagem1.getpixel((i,j)),imagem2.getpixel((i,j))))
    return imagemSaida


def intersecao(imagem1, imagem2):
    imagemSaida = Image.new("L", imagem1.size)
    largura, altura = imagem1.size
    for i in range(largura):
        for j in range(altura):
            imagemSaida.putpixel((i, j), min(imagem1.getpixel((i, j)), imagem2.getpixel((i, j))))
    return imagemSaida


def diferenca(imagem1, imagem2):
    imagemSaida = Image.new("L", imagem1.size)
    largura, altura = imagem1.size
    for i in range(largura):
        for j in range(altura):
            imagemSaida.putpixel((i, j), abs(imagem1.getpixel((i, j))-imagem2.getpixel((i, j))))
    return imagemSaida

imagem1 = Image.open("imagens/imagem1.bmp")
imagem2 = Image.open("imagens/imagem2.bmp")
#imagemSaida = uniao(imagem1,imagem2)
#imagemSaida = intersecao(imagem1,imagem2)
imagemSaida = diferenca(imagem1,imagem2)
imagemSaida.show()
