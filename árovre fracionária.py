import tkinter as tk
from math import pi,sin,cos

# explicação
print('tamanho: tamanho do ramo original, recomendo entre 200 e 300 \n'
      'rácio: o quão menor é o ramo da próxima iteração, de 0.6 a 0.7 , é necessário usar .\n'
      'ângulo: ângulo entre os ramos de uma divisão, estão em deg \n'
      'n_ramos: número de ramos de cada divisão, irão ocupar o âgnulo escolhido, têm de ser maior que 1 \n'
      'iterações: número vezes que se calcula mais ramos, acima de 15 para de fazer diferênça\n \n'
      'pode precionar "r" para reajustar a janela, caso altere o tamanho desta\n')
# variáveis
tamanho = int(input('tamanho > '))
rácio = float(input('rácio > '))
ângulo = float(input('ângulo > ')) / 57.29
n_ramos = int(input('número de ramos > '))
iterações = int(input('iterações > '))

# crioa a janela e canvas
root = tk.Tk()
canvas = tk.Canvas(root, width=root.winfo_screenwidth() ,height=root.winfo_screenheight(),bg = 'black')
canvas.pack()


def draw_tree(start_x, start_y, tamanho, ângulo_inicial, iterações):
    if iterações > 0:
        # calcula os novos pontos
        end_x = start_x - tamanho * cos(ângulo_inicial)
        end_y = start_y - tamanho * sin(ângulo_inicial)
        # desenha o ramos
        canvas.create_line(start_x, start_y, end_x, end_y,fill = 'white')

        for i in range(n_ramos):
            ângulo2 = ângulo_inicial - (ângulo / 2) + ((ângulo / (n_ramos - 1)) * i) # calcula o ângulo de cada ramo
            draw_tree( end_x, end_y, tamanho * rácio,ângulo2 , iterações - 1) # faz mais uma iteração


draw_tree(root.winfo_screenwidth()/2, root.winfo_screenheight() * 0.9, tamanho, pi/2, iterações)# desenha o fractal


def resize(event):
    if event.char != 'r': # confirma que foi a tecla 'r'
        return

    root.update() # atualiza o tamanho da janela

    canvas.config(width=root.winfo_width(),height=root.winfo_height()) # atualiza o tamanho do canvas

    canvas.delete('all') # linpa o canvas

    draw_tree(root.winfo_width()/2,root.winfo_height()*0.9,tamanho,pi/2,iterações)# redesenha o fractal
    print(2)

root.bind('<Key>',resize)# chama a função sempre que a janela é alterada


root.mainloop() # impede a janela de se fechar quando o fractal acaba de ser desenhado