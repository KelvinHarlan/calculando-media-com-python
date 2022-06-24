nome = input ('Olá, Digite seu nome:\n ')
nota1 = float(input('Digite uma nota:\n '))
nota2 = float(input('Digite a Segunda nota:\n'))
media = ((nota1+nota2)/2)
#media2 = (media/2)
print(90*'-')
print(f'{nome}, estas são as informações referente a sua situação escolar:')
print(90*'-')
print (f' Olá sua média é: {media}')
if media >= 7.0:
    print(f' {nome}, Parabéns, você está aprovado(a)!')
else:
    print(f' {nome}, Lamentamos, sua situação é reprovado, solicite sua reposição.')
print(90*'-')