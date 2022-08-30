class Jogador:
  def __init__(self, nome, posicao, nascimento, nacionalidade, altura, peso):
    self.nome = nome 
    self.posicao = posicao
    self.nascimento = nascimento 
    self.nacionalidade = nacionalidade 
    self.altura = altura 
    self.peso = peso

  def printar(self):
     print(f'Nome: {self.nome}\nData de nascimento: {self.nascimento}\nNacionalidade: {self.nacionalidade}\nAltura: {self.altura}\nPeso: {self.peso}\nPosição em campo: {self.posicao}\n')

  
  def idade(self, ano):
    idade = ano - self.nascimento
    print(f'O jogador possui {idade} anos.')
    
  def aposentadoria(self, ano):
    anosAposentar = 0
    idade = ano - self.nascimento
    if (self.posicao == "Goleiro"):
      anosAposentar = 40 - idade
    if (self.posicao == "Lateral"):
      anosAposentar = 38 - idade
    if (self.posicao == "Zagueiro"):
      anosAposentar = 35 - idade
    print(f'Faltam {anosAposentar} anos para a aposentadoria do jogador.')