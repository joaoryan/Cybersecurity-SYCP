import sys

import dns.resolver

resolver = dns.resolver.Resolver()

try:
	alvo = input("Digite url do alvo: ")
except:
	print("Usage: python3 dnsbrute.py dominio wordlist.txt")
	sys.exit()

try:
	with open("wordlist.txt", "r") as arq:
		subdominios = arq.read().splitlines()
except:
	print("Erro ao abrir arquivo")
	sys.exit()

for subdominio in subdominios:
	try:
		sub_alvo = "{}.{}".format(subdominio, alvo)
		resultados = resolver.resolve(sub_alvo, "A")
		for resultado in resultados:
			print("{} -> {}".format(sub_alvo, resultado))
	except:
		pass
