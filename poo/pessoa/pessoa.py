class Pessoa:
  def __init__(self, nome, idade, peso, altura):
    self.nome = nome 
    self.idade = idade
    self.peso = peso 
    self.altura = altura 


  def envelhecer(self, idade):
    self.idade += idade
    print(f'{self.nome}, você envelheceu {idade} ano(s). Idade atual: {self.idade} anos.')

  def engordar(self, peso):
    self.peso += peso 
    print(f"{self.nome}, você engordou {peso} KG's. Peso atual: {self.peso} KG's.")    

  def emagrecer(self, peso):
    self.peso -= peso
    print(f"{self.nome}, você emagreceu {peso} KG's. Peso atual: {self.peso} KG's")    
       
  def esticar(self, altura):
    self.altura += altura 
    print(f"{self.nome}, você cresceu {altura} cm's. Altura atual: {self.altura} cm's") 