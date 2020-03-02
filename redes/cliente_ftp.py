# -*- coding: utf-8 -*-

from ftplib import FTP

ftp = FTP('') # cria um objeto FTP
ftp.connect('10.25.201.147',1026) # tenta conectar-se ao servidor FTP
ftp.login('admin', 'admin') # tenta logar pode ser em anonimato login()
ftp.cwd('/') # estabelece o diretório dentro do servidor

def enviarArquivo():
 nome_arquivo = raw_input('Informe o nome do arquivo:')
 ftp.storbinary('STOR '+nome_arquivo, open(nome_arquivo, 'rb'))
 # armazena arquivo remotamente no servidor FTP em modo binário de leitura

def baixarArquivo():
 nome_arquivo = raw_input('Informe o nome do arquivo:')
 arquivo_local = open(nome_arquivo, 'wb')
 # abre arquivo em modo binário de escrita
 ftp.retrbinary('RETR ' + nome_arquivo, arquivo_local.write, 1024)
 # maxblocksize = 1024
 arquivo_local.close()

def criarDiretorio():
 nome_diretorio = raw_input('informe o nome do novo diretório: ')
 ftp.mkd(nome_diretorio)

def removerDiretorio():
 nome_diretorio = raw_input('informe o nome do diretório a ser removido: ')
 ftp.rmd(nome_diretorio)

def removerArquivo():
 nome_arquivo = raw_input('informe o nome do arquivo a ser removido: ')
 ftp.delete(nome_arquivo)

def renomearArquivo():
  nome_atual = raw_input('informe o nome atual do  arquivo: ')
  nome_novo = raw_input('informe o novo nome do  arquivo: ')
  ftp.rename(nome_atual, nome_novo)

opcao = 0
while(opcao != 1):
 print 'Informe uma das opções'
 print '\t 1. sair'
 print '\t 2. listar arquivos'
 print '\t 3. enviar arquivo'
 print '\t 4. baixar arquivo'
 print '\t 5. deletar arquivo'
 print '\t 6. criar diretório'
 print '\t 7. deletar diretório'
 print '\t 8. renomear arquivo'
 opcao = input()
 if opcao == 1:
  ftp.quit()
 elif(opcao == 2):
  ftp.retrlines('LIST')
 elif(opcao == 3):
  enviarArquivo()
 elif(opcao == 4):
  baixarArquivo()
 elif(opcao==5):
  removerArquivo()
 elif(opcao==6):
  criarDiretorio()
 elif (opcao == 7):
  removerDiretorio()
 elif (opcao == 8):
  renomearArquivo()


