aluno = {
    "nome": "Ana",
    "curso": "Ciência da Computação",
    "idade": 20
}

aluno["nota_final"] = 9.5
aluno["idade"] = 21

for chave, valor in aluno.items():
    print(chave, ":", valor)