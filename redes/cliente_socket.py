# -*- coding: utf-8 -*-

import socket
msg = ''

while msg!='Sair':
    meuSocket = socket.socket()
    meuHost = '10.25.201.147'#socket.gethostname()
    minhaPorta = 12345

    meuSocket.connect((meuHost, minhaPorta))
    msg = raw_input()
    meuSocket.send(msg)
    print meuSocket.recv(1024)
    meuSocket.close

