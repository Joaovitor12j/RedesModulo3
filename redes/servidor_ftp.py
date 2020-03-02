# -*- coding: utf-8 -*-

#pip install pyftpdlib

from pyftpdlib.authorizers import DummyAuthorizer
# DummyAuthorizer gerencia as permissões de autorização no servidor FTP
from pyftpdlib.handlers import FTPHandler
# FTPHandler verificação acesso e permissões
from pyftpdlib.servers import FTPServer
# criar io diretório

autoridade = DummyAuthorizer()
autoridade.add_user('admin', 'admin', '/home/jdso/servidorFTP',perm='elradfmw')
#autoridade.add_anonymous('/home/jdso/servidorFTP', perm='elradfmw')

gerenteFTP = FTPHandler
gerenteFTP.authorizer = autoridade

servidor = FTPServer(('10.25.201.147', 1026), gerenteFTP)
servidor.serve_forever()

#
#"e" = mudar diretório (CWD, CDUP )
#"l" = listar arquivos (LIST, NLST, STAT, MLSD, MLST, SIZE )
#"r" = baixar arquivos (RETR)
#"a" = adicionar dados a um arquivo existente (APPE )
#"d" = remover um arquivo ou diretório (DELE, RMD)
#"f" = renomear um arquivo ou diretório (RNFR, RNTO )
#"m" = criar um diretório (MKD )
#"w" = armazenar um arquivo no servidor (STOR, STOU )
#"M" = mudar as permiçeõs de um arquivo (SITE CHMOD )
#"T" = mudar o tempo do arquivo (SITE MFMT )



