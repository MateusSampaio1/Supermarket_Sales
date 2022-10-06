#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Importando as bibliotecas
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


#Armazendo os dados na variável 'dados'
dados = pd.read_csv('../Dados/supermarket_sales.csv')
dados.head()


# In[3]:


#Traduzindo as colunas do Dataset
dados.rename(columns={'Branch':'Filial', 
                       'City':'Cidade', 
                       'Customer type':'Tipo_cliente', 
                       'Gender': 'Genero',
                       'Product line': 'Linha_produto',
                       'Unit price': 'Preco_unitario', 
                       'Quantity':'Quantidade',
                       'Tax 5%': 'Imposto', 
                       'Date': 'Data',
                       'Time': 'Horario', 
                       'Payment': 'Pagamento',
                       'cogs':'CPV',
                       'gross margin percentage': 'Margem_bruta',
                       'gross income': 'Lucro_bruto',
                       'Rating':'Classificação'}, inplace = True)


# In[4]:


#Traduzindo as linhas do dataset
dados['Tipo_cliente'].replace({'Member':'Associado'}, inplace = True)
dados['Linha_produto'].replace({'Health and beauty':'Saude e beleza', 'Electronic accessories':'Acessorios eletonicos',
       'Home and lifestyle':'Casa e estilo de vida', 'Sports and travel':'Esporte e viagens', 'Food and beverages':'Alimentos e bebidas',
       'Fashion accessories':'Acessorios de moda'}, inplace = True)
dados['Pagamento'].replace({'Ewallet':'Carteira digital', 'Cash':'Dinheiro', 'Credit card':'Cartao de credito'}, inplace = True)
dados['Genero'].replace({'Female': 'Feminino', 'Male':'Masculino'}, inplace = True)
dados


# In[5]:


#Salvandoos dados tratados
dados.to_csv('../Dados/dados_tratados.csv')

