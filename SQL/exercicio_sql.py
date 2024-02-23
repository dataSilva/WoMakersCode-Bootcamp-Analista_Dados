#EXERCÍCIO DE SQL - WOMAKERSCODE

import sqlite3
conexao = sqlite3.connect('banco_exercicio')
cursor = conexao.cursor()

# EXERCÍCIO 1
# cursor.execute('CREATE TABLE alunos(id int, nome varchar(50), idade int, curso varchar(20));')


#EXERCÍCIO 2
#cursor.execute('INSERT INTO alunos (id,nome, idade, curso) VALUES (1, 'Marília', 29, 'Letras'),(2, 'Rute',24, 'Matemática'), (3, 'Mauro', 18, 'Biologia'), (4, 'Roberto', 32, 'Computação'),(5, 'Lúcia', 30, 'Letras');')

#EXERCÍCIO 3
#SELECIONANDO TODOS OS REGISTROS da tabela 'alunos'
alunos = cursor.execute('SELECT * FROM alunos')
for aluno in alunos:
  print(aluno)

#SELECIONANDO ALUNOS COM MAIS DE 20 ANOS
alunos = cursor.execute('SELECT nome, idade FROM alunos WHERE idade > 20')
for aluno in alunos:
  print(aluno)

#SELECIONADO ALUNOS COM CURSO DE ENGENHARIA
alunos = cursor.execute('SELECT nome, curso FROM alunos WHERE curso = "Engenharia"')
for aluno in alunos:
  print(aluno)

#CONTANDO O NÚMERO DE ALUNOS
alunos = cursor.execute('SELECT count(nome) FROM alunos')
for aluno in alunos:
  print(aluno)

#EXERCÍCIO 4
#ATUALIZAÇÃO
#cursor.execute('UPDATE alunos SET idade = 44 WHERE nome = 'Rute';')

#REMOÇÃO
#cursor.execute('DELETE FROM alunos  WHERE id=3;')

#VISUALIZANDO
alunos = cursor.execute('SELECT * FROM alunos')
for aluno in alunos:
  print(aluno)


#EXERCÍCIO 5
#cursor.execute('CREATE TABLE clientes(id int NOT NULL PRIMARY KEY, nome VARCHAR(50), idade int, saldo float);')

#VISUALIZANDO
clientes = cursor.execute('SELECT * FROM clientes')
for cliente in clientes:
  print(cliente)

#INSERINDO VALORES
#cursor.execute('INSERT INTO clientes (id,nome, idade, saldo) VALUES (1, 'Marília', 23, 55.78),  (2, 'Jesus', 33, 75.78), (3, 'Madalena', 53, 5.78), (4, 'Tiago', 34, 100.78);')


#EXERCÍCIO 6
clientes = cursor.execute('SELECT nome, idade FROM clientes WHERE idade > 30;')
for cliente in clientes:
  print(cliente)


#MÉDIA DO SALDO
media_saldo = cursor.execute('SELECT AVG(saldo) as saldo_medio FROM clientes;')
print(media_saldo)

#SALDO MÁXIMO
max_saldo = cursor.execute('SELECT MAX(saldo) FROM clientes;')
print(max_saldo)


#CONTANDO CLIENTES COM SALDO MAIOR QUE 1000
contador = cursor.execute('SELECT count(nome) FROM clientes WHERE saldo > 1000;')
print(contador)

#EXERCÍCIO 7
#ATUALIZAR SALDO DE CLIENTE ESPECÍFICO
#cursor.execute('UPDATE clientes SET saldo= 1000.56 WHERE nome = 'Madalena';')

# clientes = cursor.execute('SELECT * FROM clientes')
# for cliente in clientes:
#   print(cliente)


#REMOVER CLIENTE PELO ID
#cursor.execute('DELETE FROM clientes WHERE id=3;')



#EXERCÍCIO 8
#JUNÇÃO DE TABELAS

#CRIAÇÃO TABELA COMPRAS
#cursor.execute('CREATE TABLE compras(id int NOT NULL PRIMARY KEY,cliente_id int,produto VARCHAR(50),valor real,CONSTRAINT cliente_id	FOREIGN KEY(cliente_id) REFERENCES clientes(id));')



#VISUALIZANDO
clientes = cursor.execute('SELECT * FROM clientes')
for cliente in clientes:
  print(cliente)

compras = cursor.execute('SELECT * FROM compras')
for compra in compras:
  print(compra)


#cursor.execute('INSERT INTO compras(id, cliente_id, produto,valor) VALUES (1, 2,'guaraná', 4.99),(2, 2,'guaraná', 4.99),(3, 1,'arroz', 24.99),(4, 4,'Pão de forma', 6.99)')


#unindo tabelas
inner_join = cursor.execute('SELECT nome, produto, valor FROM compras inner JOIN clientes ON clientes.id = compras.cliente_id;')
for inner in inner_join:
  print(inner)

conexao.commit()
conexao.close()