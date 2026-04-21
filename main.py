#Exemplo que causa TypeError

nome =  "lino"

try:
    resultado = len(nome)
except TypeError as e:
    print(f"Ocorreu um erro do tipo: {e}")

