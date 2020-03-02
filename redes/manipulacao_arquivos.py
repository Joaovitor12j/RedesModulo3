# -*- coding: utf-8 -*-

arquivo = open('/home/jdso/Desktop/redes/saudacoes.txt', 'w')
arquivo.write('oi\n')
arquivo.write('galera de redes\n')
arquivo.write('tudo bem?\n')
arquivo.write('até mais\n')
arquivo.close()


arquivo = open('/home/jdso/Desktop/redes/saudacoes.txt', 'w')
arquivo.write('ainda não...\n')
arquivo.close()


arquivo = open('/home/jdso/Desktop/redes/saudacoes.txt', 'r')
print arquivo.read()