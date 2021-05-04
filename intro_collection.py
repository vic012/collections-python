idade = [39, 27, 18, 15]
#Verifica se há um item
print(28 in idade)
#insere um item na posição desejada
idade.insert(3, 20)
#Extende uma lista e a adiciona em outra lista
idade.extend([27,19])
#Laço for nas listas para adicionar um ano a frente
for id in idade:
	print("O próximo aniversário será:", id + 1)
ano_que_vem = []
for id in idade:
	ano_que_vem.append(id + 1)
print(ano_que_vem)
#Reduzindo
#Quero criar um lista e para cada item da lista anterior vou somar adicionando na nova lista
idade_ano_que_vem = [(id + 1) for id in idade]
print(idade_ano_que_vem)
#Impondo condições
#Para todas as idades se for maior que 21 mantenha senão não mantenha
idades_ano_que_vem_melhorada = [(id)for id in idade if id > 21]
print(idades_ano_que_vem_melhorada)


