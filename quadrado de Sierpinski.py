import tkinter as tk

# variavéis e explicação
print('No tamanho recomento 729, ou qualquer poder de 3, as iterações começão em 0 e a partir de 5 começa a piorar')
tamanho = int(input('tamanho > '))
iterações = int(input('iterações > '))

# cria a janela e canvas
window = tk.Tk()# cria a janela
window.geometry(f'{window.winfo_screenwidth()}x{window.winfo_screenheight()}')
window.update()# atualiza o tamanho da janela
canvas = tk.Canvas(window, width=window.winfo_width(),height=window.winfo_height(),bg = 'black')#cria o canvas
canvas.pack()



def draw_sierpinski_square(x1, x4,y1, y4, size, n): # desenha o resto do fractal

    if n > 0:
        size2 = size/3# define o tamanho dos 8 novos cubos

        x2, y2 = x1 + size2, y1 + size2  # calcula o ponto médio esquerda superior
        x3, y3 = x4 - size2, y4 - size2  # calcula o ponto médio direita inferior

        canvas.create_rectangle(x2, y2, x3, y3, fill='black')  # desenha o quadrado do meio

        # os dicionários são precisos para dividir o quadrado com um ciclo for
        x = {1: x1, 2: x2, 3: x3, 4: x4}
        y = {1: y1, 2: y2, 3: y3, 4: y4}

        # divide o quadrado
        for i in range(1,4):
            for j in range(1, 4):
                if  not (i == j and i == 2):# evita desenhar no quadrado do centro que já esta desenhado
                    draw_sierpinski_square(x[i],x[i+1],y[j],y[j+1],size2,n-1)# repete o processo para as divisões

def inciar_fractal(tamanho):
    # calcula algumas posições e valores necessários para desenhar o quadrado
    x = window.winfo_width() / 2
    y = window.winfo_height() / 2
    desvio = int(tamanho / 2)

    x1,y1 = x - desvio, y - desvio# ponto esquerda superior
    x2,y2 = x + desvio + 1 , y + desvio + 1 # ponto direita inferior

    canvas.create_rectangle(x1,y1,x2,y2,fill='white')# desenha o quadrado incial

    draw_sierpinski_square(x1, x2, y1, y2, tamanho, iterações)  # desenha o resto do fractal



inciar_fractal(tamanho) # desenha todo_ o fractal



def resize(event):# atualiza a janela

    canvas.delete('all') # linpa o cavas

    inciar_fractal(tamanho) # redesenha o fractal

window.bind('<Configure>',resize) # chama a função quando a janela muda de tamanho o posição



window.mainloop()# mostra o fractal