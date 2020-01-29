from project import realizarMatricula

print('texto bonito para começar')
print('Primeiro digite sua matricula:')
matricula_i = input()
print('Agora digite sua senha de acesso:')
password_i = input()
print('Horario de matricula (Siga o formato "DD/MM/AAAA HH:MM:SS):')
horario_i = input()

print('Agora digite a cada linha as cadeiras que você gostaria de se matricular e em qual turma, garanta que tenha vaga ainda, não tenha conflito entre elas e o numero minimo de creditos. Siga o formato "CCCCCCC - TT", quando terminar digite "sair"')

chairs = []

while True:
    temp = input()
    if temp == 'sair':
        break
    chairs.append(temp)

realizarMatricula(matricula_i,password_i,horario_i,chairs)

print('Matricula realizada, queira verificar por favor.\nUm oferecimento de PATATIRO e PATATRAFICO')
