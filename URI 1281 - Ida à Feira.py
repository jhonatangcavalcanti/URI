
n = int(input())
while(n > 0):
	n -= 1

	m = int(input())
	
	produtos = {}
	for i in range(m):
		produto = input()
		produto = produto.split() 
		produtos[produto[0]] = float(produto[1]) # convertendo o produto para um par {string:float} = {nome:valor}

	p = int(input())
	total = 0.0
	for i in range(p):
		produto = input()
		produto = produto.split()
		nome_produto = str(produto[0])
		qtd_produto = int(produto[1])
		total = total + produtos[nome_produto] * qtd_produto # convertendo o produto para um par {string:int} = {nome:quantidade}
	print ("R$ %.2f" % total)