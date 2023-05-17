t = input("Digite o texto: ")
def text(t):
    contador = 0
    tinv = ""
    for x in t:
        if x not in " ":
            contador+=1
    print(f'Texto tem: {contador} letras')
    for y in range(len(t)-1,-1,-1):
        tinv+=t[y]
    print(tinv)
text(t)