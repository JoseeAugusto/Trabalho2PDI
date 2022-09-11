from PIL import Image, ImageDraw

def preencheObjetoVerde(imagem):
    cont = 1
    contCoordenadas = 0
    confereCima = True
    confereBaixo = True
    confereEsquerda = True
    confereDireita = True
    coordenadas = []
    largura, altura = imagem.size

    for i in range(1,largura-1):
        for j in range(1,altura-1):
            if(imagem.getpixel((i,j)) == (255,255,255)):
                while(imagem.getpixel((i-cont,j)) != (0,255,0)):
                    if(i-cont == 0):
                        confereCima = False
                        break
                    cont += 1
                cont = 1
                while(imagem.getpixel((i+cont, j)) != (0,255,0)):
                    if(i+cont == 499):
                        confereBaixo = False
                        break
                    cont += 1
                cont = 1
                while(imagem.getpixel((i, j-cont)) != (0,255,0)):
                    if(j-cont == 0):
                        confereEsquerda = False
                        break
                    cont += 1
                cont = 1
                while(imagem.getpixel((i, j+cont)) != (0,255,0)):
                    if(j+cont == 499):
                        confereDireita = False
                        break
                    cont += 1
                cont = 1
                if(confereCima and confereBaixo and confereDireita and confereEsquerda):
                    coordenadas += [[i,j]]
                    ImageDraw.floodfill(imagem, coordenadas[contCoordenadas], (0,255,0))
                    contCoordenadas+=1
                confereCima = True
                confereBaixo = True
                confereDireita = True
                confereEsquerda = True


def preencheObjetoAmarelo(imagem):
    cont = 1
    contCoordenadas = 0
    confereCima = True
    confereBaixo = True
    confereEsquerda = True
    confereDireita = True
    coordenadas = []
    largura, altura = imagem.size

    for i in range(1, largura-1):
        for j in range(1, altura-1):
            if(imagem.getpixel((i, j)) == (255, 255, 255)):
                while(imagem.getpixel((i-cont, j)) != (255, 255, 0)):
                    if(i-cont == 0):
                        confereCima = False
                        break
                    cont += 1
                cont = 1
                while(imagem.getpixel((i+cont, j)) != (255, 255, 0)):
                    if(i+cont == 499):
                        confereBaixo = False
                        break
                    cont += 1
                cont = 1
                while(imagem.getpixel((i, j-cont)) != (255, 255, 0)):
                    if(j-cont == 0):
                        confereEsquerda = False
                        break
                    cont += 1
                cont = 1
                while(imagem.getpixel((i, j+cont)) != (255, 255, 0)):
                    if(j+cont == 499):
                        confereDireita = False
                        break
                    cont += 1
                cont = 1
                if(confereCima and confereBaixo and confereDireita and confereEsquerda):
                    coordenadas += [[i, j]]
                    ImageDraw.floodfill(
                        imagem, coordenadas[contCoordenadas], (255, 255, 0))
                    contCoordenadas += 1
                confereCima = True
                confereBaixo = True
                confereDireita = True
                confereEsquerda = True


def preencheObjetoAzul(imagem):
    cont = 1
    contCoordenadas = 0
    confereCima = True
    confereBaixo = True
    confereEsquerda = True
    confereDireita = True
    objetoAzulPreenchido = False
    coordenadas = []
    largura, altura = imagem.size

    for i in range(1, largura-1):
        for j in range(1, altura-1):
            if(len(coordenadas) > 3):
                objetoAzulPreenchido = True
                break
            if(imagem.getpixel((i, j)) == (255, 255, 255)):
                while(imagem.getpixel((i-cont, j)) != (0, 0, 255)):
                    if(i-cont == 0):
                        confereCima = False
                        break
                    cont += 1
                cont = 1
                while(imagem.getpixel((i+cont, j)) != (0, 0, 255)):
                    if(i+cont == 499):
                        confereBaixo = False
                        break
                    cont += 1
                cont = 1
                while(imagem.getpixel((i, j-cont)) != (0, 0, 255)):
                    if(j-cont == 0):
                        confereEsquerda = False
                        break
                    cont += 1
                cont = 1
                while(imagem.getpixel((i, j+cont)) != (0, 0, 255)):
                    if(j+cont == 499):
                        confereDireita = False
                        break
                    cont += 1
                cont = 1
                if(confereCima and confereBaixo and confereDireita and confereEsquerda):
                    coordenadas += [[i, j]]
                    ImageDraw.floodfill(
                        imagem, coordenadas[contCoordenadas], (0, 0, 255))
                    contCoordenadas += 1
                confereCima = True
                confereBaixo = True
                confereDireita = True
                confereEsquerda = True
        if objetoAzulPreenchido:
            break

imagem = Image.open('imagens/quadro.png').convert("RGB")
preencheObjetoVerde(imagem)
preencheObjetoAmarelo(imagem)
preencheObjetoAzul(imagem)

imagem.show()
