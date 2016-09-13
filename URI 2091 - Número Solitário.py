
while True:
	n = int(input())
	if(n == 0):
		break
	
	A = [int(a) for a in input().split()]
	
	A.sort()

	elemento_atual = A[0]
	qtd_atual = 0
	for a in A:
		if(elemento_atual != a):
			if(qtd_atual%2 != 0): # Se a quantidade é impar -> não tem par
				break
			qtd_atual = 1
			elemento_atual = a
		else:
			qtd_atual += 1
	print(elemento_atual)

