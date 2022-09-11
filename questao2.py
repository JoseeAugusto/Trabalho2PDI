from PIL import Image
import statistics

img = Image.open('imagens/lena_ruido.bmp')
imagemFiltrada1 = Image.open('imagens/lena_ruido.bmp')
imagemFiltrada2 = Image.open('imagens/lena_ruido.bmp')
imagemFiltrada3 = Image.open('imagens/lena_ruido.bmp')
imagemFiltrada4 = Image.open('imagens/lena_ruido.bmp')
imagemFiltroMediana = Image.open('imagens/lena_ruido.bmp')
janela1 = [[0,1,0],[1,1,1],[0,1,0]]
janela2 = [[1,1,1],[1,1,1],[1,1,1]]
janela3 = [[1,3,1],[3,16,3],[1,3,1]]
janela4 = [[0,1,0],[1,4,1],[0,1,0]]
elementoCentral = 0


largura,altura = img.size
for i in range(largura):
    for j in range(altura):
        if i > 0 and i < 298 and j > 0 and j < 298:
            elementoCentral = round((img.getpixel((i, j))*janela1[1][1] +
                                     img.getpixel((i-1, j))*janela1[0][1] +
                                     img.getpixel((i+1, j))*janela1[2][1] +
                                     img.getpixel((i, j-1))*janela1[1][0] +
                                     img.getpixel((i, j+1))*janela1[1][2] +
                                     img.getpixel((i-1, j+1))*janela1[0][2] +
                                     img.getpixel((i+1, j+1))*janela1[2][2] +
                                     img.getpixel((i-1, j-1))*janela1[0][0] +
                                     img.getpixel((i+1, j-1))*janela1[2][0])/5)
            imagemFiltrada1.putpixel((i, j), elementoCentral)

for i in range(largura):
    for j in range(altura):
        if i > 0 and i < 298 and j > 0 and j < 298:
            elementoCentral = round((img.getpixel((i, j))*janela2[1][1] +
                                     img.getpixel((i-1, j))*janela2[0][1] +
                                     img.getpixel((i+1, j))*janela2[2][1] +
                                     img.getpixel((i, j-1))*janela2[1][0] +
                                     img.getpixel((i, j+1))*janela2[1][2] +
                                     img.getpixel((i-1, j+1))*janela2[0][2] +
                                     img.getpixel((i+1, j+1))*janela2[2][2] +
                                     img.getpixel((i-1, j-1))*janela2[0][0] +
                                     img.getpixel((i+1, j-1))*janela2[2][0])/9)
            imagemFiltrada2.putpixel((i, j), elementoCentral)

for i in range(largura):
    for j in range(altura):
        if i > 0 and i < 298 and j > 0 and j < 298:
            elementoCentral = round((img.getpixel((i, j))*janela3[1][1] +
                                     img.getpixel((i-1, j))*janela3[0][1] +
                                     img.getpixel((i+1, j))*janela3[2][1] +
                                     img.getpixel((i, j-1))*janela3[1][0] +
                                     img.getpixel((i, j+1))*janela3[1][2] +
                                     img.getpixel((i-1, j+1))*janela3[0][2] +
                                     img.getpixel((i+1, j+1))*janela3[2][2] +
                                     img.getpixel((i-1, j-1))*janela3[0][0] +
                                     img.getpixel((i+1, j-1))*janela3[2][0])/32)
            imagemFiltrada3.putpixel((i, j), elementoCentral)

for i in range(largura):
    for j in range(altura):
        if i > 0 and i < 298 and j > 0 and j < 298:
            elementoCentral = round((img.getpixel((i, j))*janela4[1][1] +
                                     img.getpixel((i-1, j))*janela4[0][1] +
                                     img.getpixel((i+1, j))*janela4[2][1] +
                                     img.getpixel((i, j-1))*janela4[1][0] +
                                     img.getpixel((i, j+1))*janela4[1][2] +
                                     img.getpixel((i-1, j+1))*janela4[0][2] +
                                     img.getpixel((i+1, j+1))*janela4[2][2] +
                                     img.getpixel((i-1, j-1))*janela4[0][0] +
                                     img.getpixel((i+1, j-1))*janela4[2][0])/8)
            imagemFiltrada4.putpixel((i, j), elementoCentral)

for i in range(largura):
    for j in range(altura):
        if i > 0 and i < 298 and j > 0 and j < 298:
            elementoCentral = statistics.median(
                [img.getpixel((i-1, j-1)), img.getpixel((i-1, j)), img.getpixel((i-1, j+1)), img.getpixel((i, j-1)),
                 img.getpixel((i, j)), img.getpixel((i, j+1)), img.getpixel((i+1, j-1)), img.getpixel((i+1, j)),
                 img.getpixel((i+1, j+1))])
            imagemFiltroMediana.putpixel((i, j), elementoCentral)
            

#imagemFiltrada1.show()

#imagemFiltrada2.show()

#imagemFiltrada3.show()

#imagemFiltrada4.show()

imagemFiltroMediana.show()
