
from selenium import webdriver
from time import sleep
from datetime import datetime

def realizarMatricula(student_id, student_pw, matricula_open, chairs):

    #   Instancia o webdriver do selenium para que posso fazer interações com o navegador Chrome.
    browser = webdriver.Chrome('/usr/bin/chromedriver')

    #   Matrícula do aluno.
    student_id = student_id
    #   Senha de acesso.
    student_pw = student_pw
    #   Horário de matrícula do aluno.
    matricula_open = datetime.strptime(matricula_open, '%d/%m/%Y %H:%M:%S')
    #   Cadeiras que o aluno quer se matricular.
    cadeiras = chairs

    #   Acessa a página de login ao controle acadêmico.
    browser.get('https://pre.ufcg.edu.br:8443/ControleAcademicoOnline/')

    #   Preencha os campos de login, senha e submete.
    browser.find_element_by_id('login').send_keys(student_id)
    browser.find_element_by_id('senha').send_keys(student_pw)
    browser.find_elements_by_class_name('btn-primary')[0].click()

    #   Acessa a página de horário do aluno.
    browser.get('https://pre.ufcg.edu.br:8443/ControleAcademicoOnline/Controlador?command=AlunoHorarioConfirmar&ano=2020&periodo=0')

    #   While que coleta a hora do servidor pela página de emissão do horário e compara para verificar se já esta no horário de matrícula.
    while True:
        time_text = browser.find_elements_by_class_name('col-sm-3')[0].text[9:]
        time = datetime.strptime(time_text, '%d/%m/%Y %H:%M:%S')
        if time >= matricula_open:
            #print(time)
            #print(matricula_open)
            #print(time >= matricula_open)
            break
        print(time)
        sleep(0.66)
        browser.refresh()

    #   Acessa a página de matrícula.
    browser.get('file:///home/otten/%C3%81rea%20de%20Trabalho/project/local.html')

    #   Coleta todas as cadeiras disponíveis.
    rows = browser.find_elements_by_tag_name('tbody')[0].find_elements_by_tag_name('tr')

    #   Marca o checkbox das cadeiras solicitadas.
    for cadeira in cadeiras:
        cont = 1
        for row in rows:
            if cadeira in row.text:
                browser.find_elements_by_xpath('//*[@id="tabOferta"]/tbody/tr['+str(cont)+']/td[6]/input')[0].click()
                break
            else: cont += 1

    #   Submete a matrícula.
    browser.find_elements_by_class_name('btn-primary')[0].click()

    sleep(60)



