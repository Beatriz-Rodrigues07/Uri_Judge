a = float(input())
b = float(input())
c = float(input())



def mostrar_media (media):
    print(f"MEDIA = {media:.1f}")

def media_aluno (nota_a , nota_b ,nota_c):
    soma = (nota_a * 2 + nota_b * 3 + nota_c * 5)/(2 + 3 + 5)
    mostrar_media(soma)



media_aluno(a, b, c)