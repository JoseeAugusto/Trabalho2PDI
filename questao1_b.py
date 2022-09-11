from PIL import Image

img = Image.open('imagens/lena_gray.bmp')
imagemSuavizada = Image.open('imagens/lena_gray.bmp')
imagemFinal = Image.open('imagens/lena_gray.bmp')
janela = [[1, 1, 1],[1, 1, 1],[1, 1, 1]]
elementoCentral = 0
mascara = []

largura, altura = img.size
for i in range(largura):
    for j in range(altura):
        if i > 0 and i < 255 and j > 0 and j < 255:
            elementoCentral = round((img.getpixel((i, j))*janela[1][1] + \
                img.getpixel((i-1, j))*janela[0][1] + \
                img.getpixel((i+1, j))*janela[2][1] + \
                img.getpixel((i, j-1))*janela[1][0] + \
                img.getpixel((i, j+1))*janela[1][2] + \
                img.getpixel((i-1,j+1))*janela[0][2] + \
                img.getpixel((i+1, j+1))*janela[2][2] + \
                img.getpixel((i-1,j-1))*janela[0][0] + \
                img.getpixel((i+1,j-1))*janela[2][0])/9)              
            imagemSuavizada.putpixel((i, j), elementoCentral)

for i in range(largura):
    for j in range(altura):
        mascara.append(img.getpixel((i,j)) - imagemSuavizada.getpixel((i,j)))

indice = 0        
for i in range(largura):
    for j in range(altura):
        imagemFinal.putpixel((i,j), mascara[indice]+img.getpixel((i,j)))
        indice += 1

imagemFinal.show()

