import tkinter as tk

# variavéis e explicação
print('No tamanho recomento 1000, as iterações começão em 0 e a partir de 8 não se nota diferença')
tamanho = int(input('tamanho > '))
iterações = int(input('iterações > '))

def sierpinski(canvas, x1, y1, x2, y2, x3, y3, depth):

    if depth > 0:
        # Cálculo dos pontos do triângulo de Sierpinski
        x4 = (x1 + x2) / 2
        y4 = (y1 + y2) / 2
        x5 = (x2 + x3) / 2
        y5 = (y2 + y3) / 2
        x6 = (x3 + x1) / 2
        y6 = (y3 + y1) / 2

        # Desenha os três novos triângulos
        sierpinski(canvas, x1, y1, x4, y4, x6, y6, depth - 1)
        sierpinski(canvas, x4, y4, x2, y2, x5, y5, depth - 1)
        sierpinski(canvas, x6, y6, x5, y5, x3, y3, depth - 1)
    else:
        # Desenho do triângulo final
        canvas.create_line((x1, y1), (x2, y2), (x3, y3),(x1, y1),fill = 'white')

# Criação da janela
window = tk.Tk()
window.title("Triângulo de Sierpinski")
window.geometry(f'{window.winfo_screenwidth()}x{window.winfo_screenheight()}')
window.update()

# Criação do canvas
canvas = tk.Canvas(window, width=window.winfo_width() ,height=window.winfo_height(),bg = 'black')
canvas.pack()

# clacula alguns pontos
x = window.winfo_width()/2
y = window.winfo_height()/2
altura = int(0.433*tamanho)

# desenha o triângulo
sierpinski(canvas, x - tamanho/2,y + altura, x + tamanho/2,y + altura, x, y - altura, iterações)


def resize(event):
    canvas.config(width=event.width,height=event.height) # muda o tamanho do canvas

    # clacula os pontos de novo
    x = event.width / 2
    y = event.height / 2
    altura = int(0.433 * tamanho)

    # apaga tudo
    canvas.delete('all')

    # redesenha o triângulo
    sierpinski(canvas, x - tamanho / 2, y + altura, x + tamanho / 2, y + altura, x, y - altura, iterações)

# chama a função resize quando a janela muda de tamanho
window.bind('<Configure>',resize)


# Exibição da janela
window.mainloop()