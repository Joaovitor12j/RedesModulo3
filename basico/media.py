# -*- coding: utf-8 -*-

L = []

print 'Informe os valores a serem inseridos na lista' \
      'ou digite SAIR para encerrar.'

valor_digitado = 'qualquer coisa'

while valor_digitado != 'SAIR':
    valor_digitado = raw_input()
    if(valor_digitado != 'SAIR'):
        L.append(valor_digitado)

print L


