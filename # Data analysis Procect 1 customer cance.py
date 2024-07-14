# Data analysis Procect 1 customer cancellation
#Projeto Analise de Dados 
#foco cancelamento de Clientes

#colocar o jupter detro do Vscode - instalar pandas numpy e etc 

#Passo a passo (step by step )
#Passo 1: Importar a base de dados
#Passo 2: Visualizar a base de dados
        #entender o que tem a base de dados
        #econtrar as 'cagadas' da base de dados
#Passo 3: Tratamento de dados: Verificar e corrigir os proporlemas da base de dados
#Passo 4: Analise inicial dos cancelamentos
#Passo 5: Analise de causas do cancelamento dos clientes

#
# %%
#--------------------------------------------------------------
#Passo 1: Importar a base de dados
#Pandas vai ler a base de dados cancelamento e armazenar dentr da base de dados tabela

import pandas  #importar a ferramenta pandas

tabela = pandas.read_csv("cancelamentos.csv.csv") #tabela vai ser o nome da base de dados

display (tabela)





# %%
#--------------------------------------------------------------
#Passo 2: Visualizar a base de dados

#2.1 Colunas Inuteis 
#tirar coluna Customer ID que nao vai acrescentar nada

tabela = tabela.drop(columns= "CustomerID") #comando drop tira a coluna CustomerID
display(tabela)

#obs - se quiser voltar a coluna pata tirar a linha de codigo que tira ok (deletar)

# %%
#--------------------------------------------------------------
#Passo 3: Tratamento de dados: Verificar e corrigir os proporlemas da base de dados


display(tabela.info()) # Resumo da base de dados por coluna como:




# %%
#3.3 Valores Vazios
#
tabela = tabela.dropna()  #expluindo os valroes vazios automaticamente

#para verificar a tabela
display(tabela.info())




# %%
#--------------------------------------------------------------
#Passo 4: Analise inicial dos cancelamentos

#valu_counts ---> contou o valor do 1 e o do 0
display(tabela["cancelou"].value_counts()) # vai contar os valroes da coluna cancelou --> tabela["cancelou"].value_counts() depois coloco display para visualizar
#o resulatado cancelados cancelou = 381666 --> conclusao mais clientes cancelaram

#Obs para formatar numero :
# display(tabela["cancelou"].value_counts(normalize = True).map("{:.1}".format)) ponto diz que tem casa decimal, em uma casa


# %%
#--------------------------------------------------------------
#Passo 5: Analise de causas do cancelamento dos clientes
!pip install plotly
import plotly.express as px 

#
# Instalação do plotly
#tipo do grafico ser coluna aria

#Etapa 1 - Criar o grafico 

# no eixo x eu coloco a duração do contrato
#por ser histograma coloca valores no eixo Y de acordo com cada situação
#duração do contrato anual mensal e trimestral (de acordo com 'duração do contrato')
grafico = px.histogram(tabela, x= "duracao_contrato")
grafico.show()

# %%
#OUTRO GRAFICO -->Grafico assinatura do cliente focado na assinatura 
#ja da outra oção para o eixo Y
grafico = px.histogram(tabela, x= "assinatura")
grafico.show()

# %%
# CORES -- gRAFICO DURAÇÃO DO CONTRATO
#cliente cancelou em vermelho e nao cancelou em azul
#para mudar de cor a coluna referente ao cancelamento 
grafico = px.histogram(tabela, x= "duracao_contrato", color= "cancelou" )
grafico.show()

# %%
#Legenda --> mostrando numero --> text_auto=True
# numero em cada categoria

grafico = px.histogram(tabela, x= "duracao_contrato", color= "cancelou", text_auto=True )
grafico.show()

# %%
#CRIANDO VARIOS GRAFICOS JUNTOS DE ACORDO COM A COLUNA

#Agora eu quero analsiar mudando a analsie  do dashborad
#Para cada coluna da base de dados eu quero repetir (sem)
#grafico deve ser intuitivo bater o olho e ja descobrir

coluna = "idade" #a criacao do varivel nome da "coluna" que queremos se eu mudar muda, apenas esse nome
#
for coluna in tabela.columns: #NA PRIMEIRA VEZ DE EXECULTAR SERA CRIADO O A PRIMEIRA VARIAVEL DE COLUNA E VAI VOLTAR

    #criar o grafico
    grafico = px.histogram(tabela, x= coluna, color= "cancelou")

    #exibir o grafico
    grafico.show()

# %%
#Resultado dos graficos acima
#todos os clientes que ligaram mais de quatro vezes cancelaram --> resolver os problemas dos clientes no maximo apos 4 ligacoes
#atrazo de pagamento mais de 20 dias desistiram
#contrato mensal cancelaram
#em fitro sera a condição
#coluna ligacoes call center deve ser menor ou igual a quatro


# %%
#FILTRAR UMA BASE DE DADOS


#Respostas: se eu resolver o call center, para quanto cai o cancelamento
filtro = tabela["ligacoes_callcenter"] <= 4 #pode passar a condiçao ou um nome de coluna
tabela = tabela [filtro] #novo valor vai ser o antigo valor da tabela dentor do filtro


#Respostas:  eo atraso
#um filtro vai filtrar nossa tabela para resolver o problema de atraso de pagaemnto
#menores ou igual a 20 em coluna dias atraso
filtro = tabela["dias_atraso"] <20
tabela = tabela [filtro] #novo valor vai ser o antigo valor da tabela dentor do filtro


#Respostas:  e o contrato mensal
filtro = tabela["duracao_contrato"] != "Monthly"  #duraçao do contrato mensal
tabela = tabela [filtro]

display(tabela["cancelou"].value_counts(normalize=True))


