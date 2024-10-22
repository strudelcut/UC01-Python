# Consrua uma página que só aceite notas escolares entre zero e dez (treinamento para controle de erros).



controle = False

while controle == False:
    nota = int(input('Digite uma nota entre 0 e dez: '))
    if nota >= 0 and nota < 11:
        controle = True
print(f'A nota digitada: {nota}')