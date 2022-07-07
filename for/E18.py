preco = float(input('Digite o valor base do produto: \n'))

for i in range(50):
  print(i + 1, "- R$", round((i+1)*preco, 2))