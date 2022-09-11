from PIL import Image, ImageChops

img = Image.open('imagens/lena_gray.bmp')
prewitVertical = Image.open('imagens/lena_gray.bmp')
prewitHorizontal = Image.open('imagens/lena_gray.bmp')
sobelVertical = Image.open('imagens/lena_gray.bmp')
sobelHorizontal = Image.open('imagens/lena_gray.bmp')
prewitBordaVertical = [[-1, -1, -1], [0, 0, 0], [1, 1, 1]]
prewitBordaHorizontal = [[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]]
sobelBordaVertical = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]
sobelBordaHorizontal = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
elementoCentral = 0
largura, altura = img.size

for i in range(largura):
    for j in range(altura):
        if i > 0 and i < 255 and j > 0 and j < 255:
            elementoCentral = (img.getpixel((i, j))*prewitBordaVertical[1][1] +
                                     img.getpixel((i-1, j))*prewitBordaVertical[0][1] +
                                     img.getpixel((i+1, j))*prewitBordaVertical[2][1] +
                                     img.getpixel((i, j-1))*prewitBordaVertical[1][0] +
                                     img.getpixel((i, j+1))*prewitBordaVertical[1][2] +
                                     img.getpixel((i-1, j+1))*prewitBordaVertical[0][2] +
                                     img.getpixel((i+1, j+1))*prewitBordaVertical[2][2] +
                                     img.getpixel((i-1, j-1))*prewitBordaVertical[0][0] +
                                     img.getpixel((i+1, j-1))*prewitBordaVertical[2][0])
            prewitVertical.putpixel((i, j), elementoCentral)

for i in range(largura):
    for j in range(altura):
        if i > 0 and i < 255 and j > 0 and j < 255:
            elementoCentral = (img.getpixel((i, j))*prewitBordaHorizontal[1][1] +
                               img.getpixel((i-1, j))*prewitBordaHorizontal[0][1] +
                               img.getpixel((i+1, j))*prewitBordaHorizontal[2][1] +
                               img.getpixel((i, j-1))*prewitBordaHorizontal[1][0] +
                               img.getpixel((i, j+1))*prewitBordaHorizontal[1][2] +
                               img.getpixel((i-1, j+1))*prewitBordaHorizontal[0][2] +
                               img.getpixel((i+1, j+1))*prewitBordaHorizontal[2][2] +
                               img.getpixel((i-1, j-1))*prewitBordaHorizontal[0][0] +
                               img.getpixel((i+1, j-1))*prewitBordaHorizontal[2][0])
            prewitHorizontal.putpixel((i, j), elementoCentral)

for i in range(largura):
    for j in range(altura):
        if i > 0 and i < 255 and j > 0 and j < 255:
            elementoCentral = (img.getpixel((i, j))*sobelBordaVertical[1][1] +
                               img.getpixel((i-1, j))*sobelBordaVertical[0][1] +
                               img.getpixel((i+1, j))*sobelBordaVertical[2][1] +
                               img.getpixel((i, j-1))*sobelBordaVertical[1][0] +
                               img.getpixel((i, j+1))*sobelBordaVertical[1][2] +
                               img.getpixel((i-1, j+1))*sobelBordaVertical[0][2] +
                               img.getpixel((i+1, j+1))*sobelBordaVertical[2][2] +
                               img.getpixel((i-1, j-1))*sobelBordaVertical[0][0] +
                               img.getpixel((i+1, j-1))*sobelBordaVertical[2][0])
            sobelVertical.putpixel((i, j), elementoCentral)

for i in range(largura):
    for j in range(altura):
        if i > 0 and i < 255 and j > 0 and j < 255:
            elementoCentral = (img.getpixel((i, j))*sobelBordaHorizontal[1][1] +
                               img.getpixel((i-1, j))*sobelBordaHorizontal[0][1] +
                               img.getpixel((i+1, j))*sobelBordaHorizontal[2][1] +
                               img.getpixel((i, j-1))*sobelBordaHorizontal[1][0] +
                               img.getpixel((i, j+1))*sobelBordaHorizontal[1][2] +
                               img.getpixel((i-1, j+1))*sobelBordaHorizontal[0][2] +
                               img.getpixel((i+1, j+1))*sobelBordaHorizontal[2][2] +
                               img.getpixel((i-1, j-1))*sobelBordaHorizontal[0][0] +
                               img.getpixel((i+1, j-1))*sobelBordaHorizontal[2][0])
            sobelHorizontal.putpixel((i, j), elementoCentral)

diferenca = ImageChops.difference(prewitHorizontal, sobelHorizontal)
diferenca.show()
#prewitVertical.show()
#prewitHorizontal.show()
#sobelVertical.show()
#sobelHorizontal.show()