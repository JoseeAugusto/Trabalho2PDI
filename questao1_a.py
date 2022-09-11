from PIL import Image

img = Image.open('imagens/lena_gray.bmp')
laplacianoSemAjuste = Image.open('imagens/lena_gray.bmp')
laplacianoComAjuste = Image.open('imagens/lena_gray.bmp')
imagemAgucada = Image.open('imagens/lena_gray.bmp')
janela = [[0,-1,0],[-1,4,-1],[0,-1,0]]
elementoCentral = 0
lista = []

largura, altura = img.size
for i in range(largura):
    for j in range(altura):
        if i > 0 and i < 255 and j > 0 and j < 255:
            elementoCentral = img.getpixel((i, j))*janela[1][1] + \
                img.getpixel((i-1, j))*janela[0][1] + \
                img.getpixel((i+1, j))*janela[2][1] + \
                img.getpixel((i, j-1))*janela[1][0] + \
                img.getpixel((i, j+1))*janela[1][2]
            laplacianoSemAjuste.putpixel((i, j), elementoCentral)
            lista.append(elementoCentral)
        else:    
            lista.append(img.getpixel((i, j)))

indice = 0
for i in range(largura):
    for j in range(altura):
        imagemAgucada.putpixel((i, j), img.getpixel((i, j)) + lista[indice])
        indice += 1

#print(min(lista))
#print(max(lista))

valorMin = min(lista)
for i in range(len(lista)):
    lista[i] = lista[i] - valorMin
valorMax = max(lista)  
for i in range(len(lista)):
    lista[i] = round(255*(lista[i]/valorMax))   


indice = 0
for i in range(largura):
    for j in range(altura):
        laplacianoComAjuste.putpixel((i,j), lista[indice])
        indice += 1    


imagemAgucada.show()        

#laplacianoComAjuste.show()

#laplacianoSemAjuste.show()
