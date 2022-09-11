from PIL import Image

imagem = Image.open("imagens/objetosPreenchidos.png")

largura,altura = imagem.size
contAltura = 0
contLargura = 0
temDimensoes = False
janelaMenor = [[1]*43]*43
centro = [21,21]

for i in range(largura):
    for j in range(altura):
        if imagem.getpixel((i,j)) == (255,0,0):
            imagem.putpixel((i,j), (255,255,255))
        else:
            imagem.putpixel((i, j), (0,0,0))

for i in range(largura):
    for j in range(altura):
        if imagem.getpixel((i, j)) == (255, 255, 255):
            while(imagem.getpixel((i, j+contLargura)) != (0,0,0)):
                imagem.putpixel((i, j+contLargura), (255, 0, 0))
                contLargura+=1
            while(imagem.getpixel((i+contAltura, j)) != (0, 0, 0)):
                imagem.putpixel((i+contAltura, j), (255, 0, 0))
                contAltura+=1
            temDimensoes = True
        if temDimensoes == True:break
    if temDimensoes == True:break

print(contAltura)
print(contLargura)

imagem.show()