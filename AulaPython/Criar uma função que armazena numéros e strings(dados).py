#Aula 45- UDEMY
 # Vários Argumentos (xargs) identificando o Parametro. **
 #Criar uma função que armazena numéros e strings(dados)

def agencia(**carro):
    return carro 

print(agencia(marca='Gol', cor='Branca', motor=1.0))
print(agencia(marca='Gol', cor='Azul', motor=1.0))
print(agencia(marca='Gol', cor='Preto', motor=1.0))