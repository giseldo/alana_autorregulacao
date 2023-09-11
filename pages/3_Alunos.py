import streamlit as st
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd
from math import pi

st.title("Dados do aluno")

df = st.session_state["data"]

alunos = df["nome"]

aluno_selecionado = st.selectbox("Aluno", alunos)

dados_aluno_selecionado = df[df["nome"] == aluno_selecionado].iloc[0]
st.title(dados_aluno_selecionado["nome"])

grafico, resumo, dados, notas, dicas_automaticas, dicas_do_professor,   = st.tabs(["Gráfico MSLQ", "Resumo MSLQ", "Dados MSLQ", "Notas Atividades", "Dicas Automaticas", "Dicas do professor"])

q1 = dados_aluno_selecionado["q1"]
q2 = dados_aluno_selecionado["q2"]
q3 = dados_aluno_selecionado["q3"]
q4 = dados_aluno_selecionado["q4"]
q5 = dados_aluno_selecionado["q5"]
q6 = dados_aluno_selecionado["q6"]
q7 = dados_aluno_selecionado["q7"]
q8 = dados_aluno_selecionado["q8"]
q9 = dados_aluno_selecionado["q9"]
q10 = dados_aluno_selecionado["q10"]
q11 = dados_aluno_selecionado["q11"]
q12 = dados_aluno_selecionado["q12"]
q13 = dados_aluno_selecionado["q13"]
q14 = dados_aluno_selecionado["q14"]
q15 = dados_aluno_selecionado["q15"]
q16 = dados_aluno_selecionado["q16"]
q17 = dados_aluno_selecionado["q17"]
q18 = dados_aluno_selecionado["q18"]
q19 = dados_aluno_selecionado["q19"]
q20 = dados_aluno_selecionado["q20"]
q21 = dados_aluno_selecionado["q21"]
q22 = dados_aluno_selecionado["q22"]
q23 = dados_aluno_selecionado["q23"]
q24 = dados_aluno_selecionado["q24"]
q25 = dados_aluno_selecionado["q25"]
q26 = dados_aluno_selecionado["q26"]
q27 = dados_aluno_selecionado["q27"]
q28 = dados_aluno_selecionado["q28"]
q29 = dados_aluno_selecionado["q29"]
q30 = dados_aluno_selecionado["q30"]
q31 = dados_aluno_selecionado["q31"]
q32 = dados_aluno_selecionado["q32"]
q33 = dados_aluno_selecionado["q33"]
q34 = dados_aluno_selecionado["q34"]
q35 = dados_aluno_selecionado["q35"]
q36 = dados_aluno_selecionado["q36"]
q37 = dados_aluno_selecionado["q37"]
q38 = dados_aluno_selecionado["q38"]
q39 = dados_aluno_selecionado["q39"]
q40 = dados_aluno_selecionado["q40"]
q41 = dados_aluno_selecionado["q41"]
q42 = dados_aluno_selecionado["q42"]
q43 = dados_aluno_selecionado["q43"]
q44 = dados_aluno_selecionado["q44"]

with dados:
    st.write("Escalas de Motivação")
    st.write("Q1 - Orientação a Metas Intrínsecas - Prefiro um trabalho de classe desafiador em que eu possa aprender coisas novas:",  q1)
    st.write("Q2 - Orientação a Metas Intrínsecas - Costumo escolher tópicos de assuntos dos quais aprenderei algo -  mesmo que exijam mais trabalhos:", q2)
    st.write("Q3 - Orientação a Metas Extrínsecas - Comparado com outros alunos desta turma -  espero ter sucesso:", q3)
    st.write("Q4 - Orientação a Metas Extrínsecas - Eu acho que vou receber uma boa nota nesta aula:", q4)
    st.write("Q5 - Valorização da Atividade - É importante para mim aprender o que está sendo ensinado na aula:", q5)
    st.write("Q6 - Valorização da Atividade - Gosto do que estou aprendendo na aula:", q6)
    st.write("Q7 - Valorização da Atividade - Acho que vou poder usar o que aprendi nesta aula em outras aulas:", q7)
    st.write("Q8 - Valorização da Atividade - Acho que o que estou aprendendo nesta aula é útil para meu aprendizado:", q8)
    st.write("Q9 - Valorização da Atividade - Eu acho que o que estamos aprendendo nesta aula é interessante:", q9)
    st.write("Q10 - Valorização da Atividade - Entender esse assunto é importante para mim:", q10)
    st.write("Q11 - Controle do Aprendizado - Comparado com os outros alunos -  acho que sou um bom aluno:", q11)
    st.write("Q12 - Controle do Aprendizado - Minhas habilidades de estudo são excelentes em comparação com outras pessoas nesta classe:", q12)
    st.write("Q13 - Controle do Aprendizado - Comparado com outros alunos desta turma -  acho que sei bastante sobre o conteúdo:", q13)
    st.write("Q14 - Autoeficácia para Aprendizado - Estou certo de que posso entender as ideias ensinadas neste curso:", q14)
    st.write("Q15 - Autoeficácia para Aprendizado - Espero me sair muito bem nesta aula:", q15)
    st.write("Q16 - Autoeficácia para Aprendizado - Tenho certeza de que posso fazer um excelente trabalho nos problemas e tarefas atribuídos a esta classe:", q16)
    st.write("Q17 - Autoeficácia para Aprendizado - Eu sei que poderei aprender o material para esta aula:", q17)
    st.write("Q18 - Ansiedade em Testes - Fico tão nervoso durante uma prova que não consigo lembrar dos assuntos que aprendi:", q18)
    st.write("Q19 - Ansiedade em Testes - Sinto uma sensação desconfortável e chateada quando faço uma prova:", q19)
    st.write("Q20 - Ansiedade em Testes - Preocupo-me muito com testes:", q20)
    st.write("Q21 - Ansiedade em Testes - Quando faço uma prova -  penso em como estou mal:", q21)
    st.write("Q22 - Ansiedade em Testes - Quando estudo para uma prova -  tento lembrar o máximo de fatos que consigo:", q22)
    st.write("Q23:", q23)
    st.write("Q24:", q24)
    st.write("Q25:", q25)
    st.write("Q26:", q26)
    st.write("Q27:", q27)
    st.write("Q28:", q28)
    st.write("Q29:", q29)
    st.write("Q30:", q30)
    st.write("Q31:", q31)
    st.write("Q32:", q32)
    st.write("Q33:", q33)
    st.write("Q34:", q34)
    st.write("Q35:", q35)
    st.write("Q36:", q36)
    st.write("Q37:", q37)
    st.write("Q38:", q38)
    st.write("Q39:", q39)
    st.write("Q40:", q40)
    st.write("Q41:", q41)
    st.write("Q42:", q42)
    st.write("Q43:", q43)
    st.write("Q44:", q44)
    
   
    
with resumo:
    #st.header("Aqui vai um resumo")
   
    media_orientacao_metas_intrinsecas = np.mean([q1, q2])
    media_orientacao_metas_extrinsicas = np.mean([q3, q4])
    media_valorizacao_da_atividade = np.mean([q5, q6, q7, q8, q9, q10])
    controle_do_aprendizado = np.mean([q11, q12, q13])
    autoeficacia_para_aprendizado = np.mean([q14, q15, q16, q17])
    ansiedade_em_testes = np.mean([q18, q19, q20, q21, q22])
   
    st.write("Escalas de Motivação")
    col1, col2, col3 = st.columns(3)
    col4, col5, col6 = st.columns(3)
   
    col1.metric("Orientação a Metas Intrínsecas: ", media_orientacao_metas_intrinsecas)
    col2.metric("Orientação a Metas Extrínsicas: ", media_orientacao_metas_extrinsicas)
    col3.metric("Valorização da Atividade: ", media_valorizacao_da_atividade)
    col4.metric("Controle do Aprendizado: ", controle_do_aprendizado)
    col5.metric("Autoeficacia para Aprendizado: ", autoeficacia_para_aprendizado)
    col6.metric("Ansiedade em testes: ", ansiedade_em_testes)
    
    st.write("Escalas de Estratégias de aprendizagem")
    col7, col8, col9 = st.columns(3)
    col10, col11, col12 = st.columns(3)
    col13, col14, col15 = st.columns(3)
    
    ensaio_memorizacao = np.mean([q23, q24, q25, q26, q27]) # 5
    elaboracao = np.mean([q28, q29]) #2
    organizacao = np.mean([q30, q31, q32]) # 3
    pensamento_critico = np.mean([q33]) #1
    autorregulacao_metacognitiva = np.mean([q34, q35, q36, q37, q38]) #5
    tempo_e_ambiente_de_estudo = np.mean([q39]) 
    administracao_de_esforcos = np.mean([q40, q41, q42, q43, q44]) #5
    
    col7.metric("Ensaio memorização: ", ensaio_memorizacao)
    col8.metric("Elaboração: ", elaboracao)
    col9.metric("Organização: ", organizacao)
    col10.metric("Pensamento crítico: ", pensamento_critico)
    col11.metric("Autorregulacao Metacognitiva: ", autorregulacao_metacognitiva)
    col12.metric("Tempo e ambiente de estudo: ", tempo_e_ambiente_de_estudo)
    col13.metric("Administração de esforços: ", administracao_de_esforcos)
        
with grafico:
    st.write("Escalas de Motivação")
    fig, ax = plt.subplots()
    constructors = ["Orientação a metas intrinsecas", "Orientação a metas extrinsicas", "Valorização da atividade", "Controle doaprendizado",
    "Autoeficacia para aprendizado", "Ansiedade em testes"]
    counts = [media_orientacao_metas_intrinsecas, media_orientacao_metas_extrinsicas, media_valorizacao_da_atividade,controle_do_aprendizado, autoeficacia_para_aprendizado, ansiedade_em_testes]
    graf1 = ax.barh(constructors, counts)
    ax.bar_label(graf1, fmt="%.01f", size=10, label_type="edge")
    ax.set_xlabel('Resposta')
    ax.set_xticks([1,2,3,4,5,6,7])
    #ax.set_title('Perfil do estudante - Escalas de motivação')
    st.pyplot(plt)
    
    st.write("Escalas de Estratégias de aprendizagem")
    fig, ax = plt.subplots()
    constructors = ["Ensaio memorização","Elaboração","Organização","Pensamento crítico","Autorregulacao Metacognitiva","Tempo e ambiente de estudo","Administração de esforços"]
    counts = [ensaio_memorizacao,elaboracao,organizacao,pensamento_critico,autorregulacao_metacognitiva,tempo_e_ambiente_de_estudo,administracao_de_esforcos]
    graf1 = ax.barh(constructors, counts)
    ax.bar_label(graf1, fmt="%.01f", size=10, label_type="edge")
    ax.set_xlabel('Resposta')
    ax.set_xticks([1,2,3,4,5,6,7])
    st.pyplot(plt)
    
  
with notas:
        
    st.write("Atividade 1")
    st.write("Nota: 10")
    
    st.write("=-=-=-=-=-")

    st.write("Atividade 2")
    st.write("Nota: 7")
             
with dicas_automaticas:
    st.text_area(height= 300, label="Dicas automáticas selecionadas",value= """ **Motivação: Interesse (Orientação a metas intrínsecas, Orientação a metas extrínsecas, Valorização da atividade e Controle do aprendizado)**
Leia rapidamente a lista com os conteúdos do seu material didático ou o programa da disciplina;
Faça uma lista dos três tópicos que mais te interessam e dos três tópicos que menos te interessam.
Preste atenção a esses tópicos em particular. 
O que nos três tópicos mais interessantes faz com que você goste tanto deles?
O que faz os três outros tópicos desinteressantes? 
Você encontra alguma característica dos três tópicos mais interessantes nos tópicos menos interessantes?
Se você conseguir identificar o quê, nos três tópicos mais interessantes, faz com que você goste deles, talvez você seja capaz de aplicar o que encontrou aos três menos interessantes.
E talvez você descubra que os tópicos desinteressantes não são tão desinteressantes assim!""")
    st.button("Enviar", key ="btndicaautomatizada")
    
with dicas_do_professor:
    st.text_area("Dica personalizada")
    st.button("Enviar", key ="btndicaprofessor")
    
