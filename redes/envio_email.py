# -*- coding: utf-8 -*-
senha = ''





import smtplib
email = 'snct.2018.ifba@gmail.com'
senha = 'admin'
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email, senha)

lista =['leandrosilvapedreira@gmail.com', 'armarius33fsa@gmail.com',
        'darlanfsa2015@hotmail.com']

mensagem = 'Você ganhou na lotofácil'
for dest in lista:
    server.sendmail(email, dest, mensagem)

server.quit()









