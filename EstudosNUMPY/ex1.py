!pip install pandas 

import pandas as pd
class Feedback:
  def __init__(self,nota,comentario):
    self.nota = nota
    self.comentario = comentario

class AnalisadorFeedback:
  def __init__(self,feedbacks):
    self.feedbacks = feedbacks


def calcular_nps(self):
  detratores = sum([1for feedback in self.feedbacks if feedback.nota <=6])
  promotores = sum([1for feedback in self.feedbacks if feedback.nota >=9])
  return (promotores - detratores) / len(self.feedbacks) * 100
   

# Leitura do arquivo
dados = pd.read_csv('/Users/leantavares/Documents/feedbacks.csv')
notas = dados['nota']

print(f"O NPS é: {nps}")

feedbacks = [Feedback(linha['nota'], linha['comentario'])   for i, linha in dados.iterrows()]
analisador = AnalisadorFeedback(feedbacks)
print(nps)