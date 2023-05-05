import turtle # importa a biblioteca necessária para isto funcionar

# variavéis e explicação
print('No tamanho recomento 800, as iterações começão em 0 e a partir de 6 não se nota diferença')
tamanho = int(input('tamanho > '))
iterações = int(input('iterações > '))

def koch_curve(t, length, level):
  if level == 0:
    t.forward(length)
  else:
    koch_curve(t, length/3, level-1)
    t.left(60)
    koch_curve(t, length/3, level-1)
    t.right(120)
    koch_curve(t, length/3, level-1)
    t.left(60)
    koch_curve(t, length/3, level-1)

def koch_snowflake(t, length, level):
  for i in range(3):
    koch_curve(t, length, level)
    t.right(120)

# inicia a janela e turtel
turtle.Screen().bgcolor("black")
t = turtle.Turtle(visible=False)
t.speed('fastest')

# ajusta a posição de forma a que o floco fique centrado
t.color('black')
t.back(tamanho/2)
t.left(90)
t.forward(int(tamanho * 0.289))
t.right(90)
t.color('white')

# desenha o floco
koch_snowflake(t, tamanho, iterações)

# impede a janela de se fechar quando o floco acaba de ser desenhado
turtle.done()

