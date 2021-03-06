# -*- coding: utf-8 -*-
"""Aula02p.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GLFfhbo2xh2wXETpxLOypktdzTlUX5yH

## Aula 01
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
fonte = "https://github.com/alura-cursos/imersao-dados-2-2020/blob/master/MICRODADOS_ENEM_2019_SAMPLE_43278.csv?raw=true"

dados = pd.read_csv(fonte)
dados.head()

dados.shape

dados["SG_UF_RESIDENCIA"]

dados.columns.values

dados[["SG_UF_RESIDENCIA", "Q025"]]

dados["SG_UF_RESIDENCIA"].unique()

len(dados["SG_UF_RESIDENCIA"].unique())

dados["SG_UF_RESIDENCIA"].value_counts()

dados["NU_IDADE"].value_counts()

dados["NU_IDADE"].value_counts().sort_index()

dados["NU_IDADE"].hist()

dados["NU_IDADE"].hist(bins = 25,figsize = (10,8))

len(dados["NU_IDADE"])

(dados["NU_IDADE"].value_counts().sort_index() / len(dados["NU_IDADE"])*100)

dados["NU_IDADE"].sort_values()

dados[["NU_IDADE","SG_UF_RESIDENCIA"]].sort_values("NU_IDADE")

dados.query("IN_TREINEIRO == 1")["IN_TREINEIRO"]

dados.query("IN_TREINEIRO == 1")["NU_IDADE"].value_counts().sort_index()

dados["NU_NOTA_REDACAO"].hist(bins = 25, figsize = (10,8))

dados["NU_NOTA_LC"].hist(bins = 20, figsize = (10,8))

dados["NU_NOTA_REDACAO"].mean()

dados["NU_NOTA_REDACAO"].std()

provas = ["NU_NOTA_REDACAO","NU_NOTA_CN","NU_NOTA_CH","NU_NOTA_MT","NU_NOTA_LC"]

dados[provas].describe()

dados["NU_NOTA_LC"].plot.box(grid = True, figsize=(10,8))

dados[provas].boxplot(grid = True, figsize=(10,8))

"""Desafio01: Proporção de incritos por idade.

Desafio02: Descrobrir de quais estados são os incritos com 13 anos.

Desafio03: Adicionar titulo no gráfico

Desafio04: Plotas os histogramas das idades dos treineiros e não treineiros

Desafio05: Comparar as distriguições das provas em inglês e espanhol

Desafio06: Explorar a documentação matsplotlib e brincar com as visualizações

Desafio 01
"""

dados["NU_IDADE"].value_counts().sort_index() / len(dados["NU_IDADE"])*100

"""Desafio 02"""

dados[["NU_IDADE","SG_UF_RESIDENCIA"]].sort_values("NU_IDADE")

"""Desafio 03"""

dados["NU_NOTA_REDACAO"].hist(bins=25,figsize=(10,8)).set_title('Nota Redação 2019')

"""Desafio 04"""

dados.query("IN_TREINEIRO == 1")["NU_IDADE"].value_counts().sort_index()

(dados.query("IN_TREINEIRO == 1")["NU_IDADE"].sort_index()).hist(bins=20)

dados.query("IN_TREINEIRO == 1")["NU_IDADE"].hist(figsize=(10,8),bins=20)

grafico = dados.query("IN_TREINEIRO == 1")["NU_IDADE"].hist(figsize=(10,8),bins=30)
grafico.set_xticks([15,18,20,30])
grafico.set_title('Incritos no ENEM 2019 como treineiros por idade')

grafico = dados.query("IN_TREINEIRO == 0")["NU_IDADE"].hist(figsize=(10,8),bins=30)
grafico.set_xticks([15,18,20,30])
grafico.set_title('Incritos no ENEM 2019 como não treineiros por idade')

"""Desafio 05"""

dados["NU_NOTA_LC"].hist()

dados["TP_LINGUA"].value_counts()

ingles = dados.query("TP_LINGUA == 0")["NU_NOTA_LC"]
espanhol = dados.query("TP_LINGUA == 1")["NU_NOTA_LC"]
ingles.plot.box()

espanhol.plot.box()

teste = pd.DataFrame({
    "ingles":dados.query("TP_LINGUA == 0")["NU_NOTA_LC"],
    "espanhol":dados.query("TP_LINGUA == 1")["NU_NOTA_LC"]
})

caixa = teste.boxplot(grid=True,figsize=(10,8),color="blue")
caixa.set_title('Notas provas de Inglês e Espanhol')

"""Desafio 06"""

dados["NU_NOTA_REDACAO"]

dados.query("NU_IDADE < 18")[["NU_IDADE","NU_NOTA_REDACAO"]].sort_values("NU_IDADE")

maiores_menores = pd.DataFrame({
    "Menores":dados.query("NU_IDADE < 18")["NU_NOTA_REDACAO"],
    "Maiores":dados.query("NU_IDADE >= 18")["NU_NOTA_REDACAO"]
})

box = maiores_menores.boxplot(grid=True,figsize=(10,8),color="blue")
box.set_title("Notas de redação dos menores de idade x maiores de idade")

sns.displot(dados, x="NU_IDADE", hue="TP_LINGUA", aspect = 2, legend = False, kind = 'kde', fill = True, bw_adjust=.40)
plt.legend(loc='upper right', labels=['Espanhol', 'Inglês'])
plt.title('Escolha da lingua por idade')
plt.show()

"""## Aula 02"""

dados.query("NU_IDADE <= 14")["SG_UF_RESIDENCIA"].unique()

dados.query("NU_IDADE <= 14")["SG_UF_RESIDENCIA"].value_counts(normalize=True)

menores_14 = dados.query("NU_IDADE <= 14")
menores_14["SG_UF_RESIDENCIA"].value_counts(normalize=True).plot.pie(figsize=(10,8))

menores_14["SG_UF_RESIDENCIA"].value_counts(normalize=True).plot.bar(figsize=(10,8))

menores_14["TP_SEXO"].value_counts(normalize=True).plot.pie(figsize=(10,8)).set_title("Proporção de sexo inscrito em menores de 15 anos")

plt.figure(figsize=(10,8))
sns.boxplot(x="Q006",y = "NU_NOTA_MT", data = dados)
plt.title('Grafico comparativo por nota Mátematica por Renda')

renda_ordem = dados["Q006"].unique()
renda_ordem.sort()
plt.figure(figsize=(10,8))
sns.boxplot(x="Q006",y = "NU_NOTA_MT", data = dados, order = renda_ordem)
plt.title('Grafico comparativo por nota Mátematica por Renda')

dados["NU_NOTA_TOTAL"] = dados[provas].sum(axis=1)
renda_ordem = dados["Q006"].unique()
renda_ordem.sort()
plt.figure(figsize=(10,8))
sns.boxplot(x="Q006",y = "NU_NOTA_TOTAL", data = dados, order = renda_ordem)
plt.title('Grafico comparativo por nota Total por Renda')

sns.displot(dados, x ="NU_NOTA_TOTAL")

dados["NU_NOTA_TOTAL"] = dados[provas].sum(axis=1)
dados.query("NU_NOTA_TOTAL == 0")

provas.append("NU_NOTA_TOTAL")
dados["NU_NOTA_TOTAL"] = dados[provas].sum(axis=1)
dados_sem_zerar = dados.query("NU_NOTA_TOTAL != 0")
plt.figure(figsize=(10,8))
sns.boxplot(x="Q006",y = "NU_NOTA_TOTAL", data = dados_sem_zerar, order = renda_ordem)
plt.title('Grafico comparativo por nota Total por Renda')

provas.append("NU_NOTA_TOTAL")
dados["NU_NOTA_TOTAL"] = dados[provas].sum(axis=1)
dados_sem_zerar = dados.query("NU_NOTA_TOTAL != 0")
plt.figure(figsize=(14,8))
sns.boxplot(x="Q006",y = "NU_NOTA_TOTAL", data = dados_sem_zerar, order = renda_ordem, hue = "IN_TREINEIRO")
plt.title('Grafico comparativo por nota Total por Renda e treineiros')



"""Desafio 01: pessoas que fazem a prova em estado diferente do estado de moradia

Desafio 02: limpar os dados

Desafio 03: Criar uma função para plotar o boxplot do seaborn

Desafio 04: Verificar se quem zerou a prova foi eliminado ounão estava presente

Desafio 05: Quem é eliminado tira zero ou NaN

Desafio 06: Verificar a proporção dos participantes de rendas mais alta e mais baixas como treineiros e não treineiros

Desafio 07: fazer o mesmo boxsplot olhando para a questão 25, e tirar uma  conclusão 

Desafio 08: quem não foi e não tem carro

Desafio 09: aumentar a amostra para alunos menor de idade e comparar proporção por estado

MEGA Desafio: pegar a amostra completa dos alunos de 13 e 14 anos

Desafio 01
"""

dados.query("SG_UF_RESIDENCIA != SG_UF_PROVA")["Q006"].value_counts()

"""Desafio 02"""

provas.append("NU_NOTA_TOTAL")
dados["NU_NOTA_TOTAL"] = dados[provas].sum(axis=1)
dados_sem_zerar = dados.query("NU_NOTA_TOTAL != 0")
sns.displot(dados_sem_zerar, x="NU_NOTA_TOTAL")

"""Desafio 03"""

def plotar(xx,yy,titulo='grafico',base=dados_sem_zerar):
  provas.append("NU_NOTA_TOTAL")
  dados["NU_NOTA_TOTAL"] = dados[provas].sum(axis=1)
  dados_sem_zerar = dados.query("NU_NOTA_TOTAL != 0")
  plt.figure(figsize=(10,8))
  sns.boxplot(x=xx,y = yy, data = base)
  plt.title(titulo)

plotar("Q015","NU_NOTA_CN",'EXEMPLO GRAFICO COM FUNCAO')

"""Desafio 04"""

dados_sem_zerar = dados.query("NU_NOTA_TOTAL != 0")
dados_zeraram = dados.query("NU_NOTA_TOTAL == 0")
len(dados_zeraram.query("TP_PRESENCA_CH == 1"))
len(dados_zeraram.query("TP_PRESENCA_CH == 2"))
len(dados_zeraram.query("TP_PRESENCA_CH == 0"))
dados_zeraram["TP_PRESENCA_CH"].value_counts(normalize=True)

"""Desafio 05 / NaN"""

dados_eliminadosd1 = dados.query("TP_PRESENCA_CH == 2")
dados_eliminadosd2 = dados.query("TP_PRESENCA_MT == 2")
print(len(dados_eliminadosd1))
print(len(dados_eliminadosd2))
dados_eliminadosd1[provas]

"""Desafio 06"""

dados_sem_zerar = dados.query("NU_NOTA_TOTAL != 0")
classe1 = dados_sem_zerar.query("Q006 in 'A'")
classe2 = dados_sem_zerar.query("Q006 in 'Q'")

classe1["IN_TREINEIRO"].value_counts(normalize=True).plot.pie().set_title('Grafico Com proporção Menor Renda, entre treineiros e não treineiros')

classe2["IN_TREINEIRO"].value_counts(normalize=True).plot.pie().set_title('Grafico com proporção Maior Renda, entre treineiros e não treineiros')

"""Desafio 07"""

dados_sem_zerar = dados.query("NU_NOTA_TOTAL != 0")
plt.figure(figsize=(14,8))
sns.boxplot(x="Q025",y = "NU_NOTA_TOTAL", data = dados_sem_zerar)
plt.title('Grafico Candidatos que tem acesso a internet x não te acesso')

"""Desafio 08"""



dados_faltososd1 = dados.query("TP_PRESENCA_CH == 0")
dados_faltososd2 = dados_faltososd1.query("TP_PRESENCA_MT == 0")
dados_faltosos = dados_faltososd2.query("Q010 == 'A'")["Q006"].value_counts(normalize=True)
# dados_faltosos3 = dados_faltososd2.query("Q010 != 'A'")["Q006"].value_counts(normalize=True)
dados_faltosos.sort_index().plot.bar(figsize=(14,10)).set_title("Pessoas que faltaram em ambos os dias de prova e não tem carros, separados por renda")
# dados_faltosos3.sort_index().plot.bar(figsize=(14,10)).set_title("Pessoas que faltaram em ambos os dias de prova e não tem carros, separados por renda")

"""Desafio 09"""

menores_idade = dados.query("NU_IDADE < 18")
menores_idade["SG_UF_RESIDENCIA"].value_counts(normalize=True).plot.bar(figsize=(12,9)).set_title('Numeros de estudantes menores de idade por estado')