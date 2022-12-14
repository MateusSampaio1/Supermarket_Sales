# Supermarket_Sales
 
## Contextualização
O crescimento dos supermecados nas cidades mais populosas vem aumentando e as competições de mercado também acompanham esta tendência, tendo em vista este fato, o conjunto de trabalhado neste projeto é refenrente a um histórico de vendas de uma rede de supermecados. Este histórico abrange um período de 3 meses e é relativo a 3 estabelecimentos que estão localizados em 3 cidades distintas.

Os dados aqui trabalhados foram obtidos no [Kaggle](https://www.kaggle.com/datasets/aungpyaeap/supermarket-sales).

A primeira parte deste projeto consitiu na realização da tradução dos dados, permitindo uma melhor compreenção dos dados, essa etapa do proojeto pode ser encontrado na pasta [Notebook](https://github.com/MateusSampaio1/Supermarket_Sales/tree/main/Notebook) e pode ser visualizada em formato de [Jupyter Notebook](https://github.com/MateusSampaio1/Supermarket_Sales/blob/main/Notebook/Supermarket_Sales.ipynb) ou arquivo [Python](https://github.com/MateusSampaio1/Supermarket_Sales/blob/main/Notebook/Supermarket_Sales.py).

### Análise dos dados
Após essa primeira parte, foi desenvolvido um Dashboard com a finalidade de explorar melhor as informações contidas neste conjunto de dados. Abaixo segue a imagem do Dash criado, o mesmo também pode ser encontrado entre os arquivo do projeto com o nome [Dashboard_Vendas](https://github.com/MateusSampaio1/Supermarket_Sales/blob/main/Dashboard_Vendas.pbix).
![Dash_vendas](https://user-images.githubusercontent.com/107072611/195391281-b22b44f9-a84d-47ca-8d1b-8c0981cc5b6e.png)

Como forma de auxiliar na análise dos dados presentes neste Dataset, decidi elencar algumas questões que iriam nortear a análise realizada neste projeto. 

A primeira delas é referente ao **valor das vendas realizadas pelas filiais durante o período analisado**. Como pode ser evidenciado, **a diferença entre as vendas feitas pelas lojas é pequena**, podendo chegar a pouco mais de $4.000,00 de diferença entre a filial que mais vendeu e a que menos vendeu. Em janeiro a filial que mais vendeu foi a C, em fevereiro foi a B e em março foi a filial A.

O segundo ponto levantado foi sobre **a existencia de preferência dos clientes em um método de pagamento** específico dentre aqueles oferecidos pelas lojas. Depois de analisar os dados fica evidente que **não existe uma preferência**, visto que a discrepância encontrada nas quantidades de pagamentos realizados pelos clientes nos 3 modos disponíveis é bem pequena, porém, para fim informativos destaco aqui que o método mais utilizado é a carteira digital enquanto o menos usado é o cartão de crédito.

Outro tópico considerado neste projeto foi **observação da distribuição do valor total das vendas por cada categoria de produto vendido pelas lojas**. Aqui se observou que existem diferenças entre as vendas realizadas em cada uma das lojas, enquanto na loja A a linha de produtos destinadas a casa e estilo de vida foram os mais vendidos, na loja B os mais vendidos foram os relacionado com saúde e beleza, já na Loja C os itens mais vendidos os ligados a alimentos e bebidas.

Após evidenciar as informações expostas no gráfico anterior, me sugiu uma dúvida relativa ao preço médio dos produtos de cada categoria. O valor unitário médio dos produtos não parece variar muito e tem uma diferença bem pequena, os produtos com o preço médio mais altos são os pertinentes as classes de **Acessorios de Moda** e **Esporte e Viagens**. Destaco ainda que a variação entre os preços médios praticados em cada segmento é bem pequena.

Além destes tópicos abordados acima, também é possível observar a variação de comportamento dos clientes alterando a segmentação de dados presentes no Dashboard. Ao modificar o genero, por exemplo, pode-se evidenciar mudanças nos itens mais vendidos em cada filial, no preço médio unitário e na posição que cada linha de produto ocupa. Seguindo essa mesma linha, também pode-se visualiar o comportamento durante os meses, entre os clientes associados e os não associados(Normal) ou então combinar as três segmentações para uma análise mais pontual.

Depois do desenvolvimento do dashboard de vendas, foi realizado um processo de clusterização nos dados utilizando o Kmeans. A ideia era tentar compreender melhor os grupos de clientes que frequentavam os estabelecimentos. 

Para realizar a implementação do algorítimo foi necessário fazer algumas modificações nos dados, a primeira delas foi a transformação das variáveis qualitativas em variáveis quantitativas, esse processo foi feito com auxílio do **OnehotEncoder**. Depois foi realizado a normalização dos dados, visto que existia uma grande diferença de escala entre ele, essa etapa foi efetuada com o **Standard Scaler** e só então foi possível aplicar o **KMeans**. O método de cotovelo foi utilizado para verificar qual seria o número de grupo ideal para esse conjunto de dados, o resultado  e após rodar os algoritmo foram realizados alguns testes para verificar a estabilidade do mesmo.

### Características encontradas nos grupos:
Logo após adicionar o agrupamento ao conjunto de dados original, voltei a utilizar o **Power BI** como ferramenta de visualização dos dados considerando essa nova variável (**Grupos**) e desenvolvi o dashbord abaixo, vale ressaltar que o mesmo também pode ser encontrado no arquivo [Dashboard_Vendas](https://github.com/MateusSampaio1/Supermarket_Sales/blob/main/Dashboard_Vendas.pbix) presente neste projeto e com o nome de **Dashboard - Clientes**.
![Dash_Clientes](https://user-images.githubusercontent.com/107072611/195687045-7cdae593-037c-4315-8e90-1d51a08a6805.png)

**Grupo 0**: Realizaram suas compras na Filial B e são o segundo que menos gasta nos supermecados. As mulheres deste grupo costumam consumir mais produtos relacionados a **Acessórios de Moda** e **Esporte e viagens**, enquanto os homens possuem uma variação bem pequena na quantidade de produtos consumidos das diferentes linhas.

**Grupo 1**: É composto por aqueles que realizaram as compras na Filial C e são aqueles que menos gasta com supermercado. Tanto as mulheres quanto os homens deste grupo compraram mais produtos relacionados a **Acessórios de moda**, e gastaram menos com artigos relacionados a **Esporte e Viagens**. 

**Grupo 2**: É constituídopor aqueles que compram na Filial A e são o segundo grupo que mais gasta, porém, por uma pequena diferença entre o grupo 0. As mulheres consumiram uma maior quantidade de produtos ligados a **Esporte e Viagens** enquanto os homens compraram mais produtos pertencentes a linha de **Alimentos e Bebidas**.

**Grupo 3**: É o grupo formado por aqueles que realizaram compras nas 3 filiais. São os que disparadamente mais gasta, isso esta relacionado com o consumo de produtos mais caros e esse efeito pode ser visto em todas as categorias de produtos. As clientes mulheres presentes neste grupo compraram uma maior quantidade de produtos que pertenciam a linha de **Alimentos e bebidas** e os homens a linha de **Saúde e beleza**.

Com base nestas características, acredito que seja possível admitir que os clientes podem ser divididos entre aqueles que consomem produtos com um valor médio regular e aqueles que consomem produtos mais sofisticados e por tanto com um valor médio maior.  Os primeiros três grupos seriam esses clientes com um consumo mais regular, que apresentam um gasto total bem próximo entre si. Já aqueles que compõe o grupo 3 são os clientes que consumiram produtos mais caros, resultando em um total gasto maior bem maior que os demais.






