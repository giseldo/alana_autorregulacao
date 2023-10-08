import streamlit as st
from googleapiclient.discovery import build
import numpy as np
import matplotlib.pyplot as plt
from google.oauth2.credentials import Credentials 

st.title("Dados do aluno")

if "id_curso_selecionado" not in st.session_state:
    st.error("Volte para a tela principal faça login e carregue uma turma!")
else:
    limite = st.session_state["limite"]
    id_curso_selecionado = st.session_state["id_curso_selecionado"]
    df_estudantes = st.session_state["df_estudantes"]
    aluno_selecionado = st.selectbox("Aluno", df_estudantes["nome"])
    df_estudante_selecionado = df_estudantes[df_estudantes["nome"] == aluno_selecionado].iloc[0]
    nome_estudante_selecionado = df_estudante_selecionado["nome"]
    #st.title(nome_estudante_selecionado)
    id_estudante_selecionado = df_estudante_selecionado["userId"]
    #st.write(df_estudante_selecionado["userId"])
    email_estudante_selecionado = df_estudante_selecionado["email"]
    #st.write(email_estudante_selecionado)
    #st.warning("O Aluno solicitou ajuda!!")
    autorregulacao, bigfive,dicas = st.tabs(["Autorregulação", "Bigfive", "Dicas"])
        
    with bigfive:
        analise_big_five, grafico_big_five, dados_big_five = st.tabs(["Análise", "Gráfico", "Dados"])
        with dados_big_five:
            df_quest_reg_big_five = st.session_state["df_respostas_big_five"] 
            if len (df_quest_reg_big_five[df_quest_reg_big_five["Nome de usuário"] == email_estudante_selecionado]) > 0:
                df_quest_reg_big_five_s = df_quest_reg_big_five[df_quest_reg_big_five["Nome de usuário"] == email_estudante_selecionado].iloc[0]
                df_quest_reg_big_five_s
            else: 
                st.warning("Aluno ainda não respondeu ao questionário do Big Five.")
        with grafico_big_five:
            df_respostas_big_five = st.session_state["df_respostas_big_five"]
            if len (df_respostas_big_five[df_respostas_big_five["Nome de usuário"] == email_estudante_selecionado]) > 0:
                dfbf = df_respostas_big_five[df_respostas_big_five["Nome de usuário"] == email_estudante_selecionado].iloc[0]           
                extroversao = np.mean([dfbf.iloc[2], dfbf.iloc[7], dfbf.iloc[12], dfbf.iloc[17], dfbf.iloc[22], dfbf.iloc[27], dfbf.iloc[31], dfbf.iloc[37]])
                amababilidade = np.mean([dfbf.iloc[3], dfbf.iloc[8], dfbf.iloc[13], dfbf.iloc[18], dfbf.iloc[23], dfbf.iloc[28], dfbf.iloc[33], dfbf.iloc[38], dfbf.iloc[43]])
                conscienciosidade = np.mean([dfbf.iloc[4], dfbf.iloc[9], dfbf.iloc[14], dfbf.iloc[19], dfbf.iloc[24], dfbf.iloc[29], dfbf.iloc[34], dfbf.iloc[39], dfbf.iloc[44]])
                estabilidade_emocional = np.mean([dfbf.iloc[5], dfbf.iloc[10], dfbf.iloc[15], dfbf.iloc[20], dfbf.iloc[25], dfbf.iloc[30], dfbf.iloc[35], dfbf.iloc[40]])
                abertura_a_experiencias = np.mean([dfbf.iloc[6], dfbf.iloc[11], dfbf.iloc[16], dfbf.iloc[21], dfbf.iloc[26], dfbf.iloc[31], dfbf.iloc[36], dfbf.iloc[41], dfbf.iloc[42], dfbf.iloc[45]])
                st.success("Perfil do Bigfive")
                fig, ax = plt.subplots()
                constructors = ["Extroversao", "Amababilidade", "Conscienciosidade", "Estabilidade Emocional", "Abertura a experiencias"]
                counts = [extroversao, amababilidade, conscienciosidade,estabilidade_emocional, abertura_a_experiencias]
                graf1 = ax.barh(constructors, counts, color='#909090')
                ax.bar_label(graf1, fmt="%.01f", size=10, label_type="edge")
                ax.set_xlabel('Resposta')
                ax.set_xticks([1,2,3,4,5])
                st.pyplot(plt)
            else:
                st.warning("Aluno ainda não respondeu ao questionário Big Five.")
                
        with analise_big_five:
            df_respostas_big_five = st.session_state["df_respostas_big_five"]
            if len (df_respostas_big_five[df_respostas_big_five["Nome de usuário"] == email_estudante_selecionado]) > 0:
                dfbf = df_respostas_big_five[df_respostas_big_five["Nome de usuário"] == email_estudante_selecionado].iloc[0]
                extroversao = np.mean([dfbf.iloc[2], dfbf.iloc[7], dfbf.iloc[12], dfbf.iloc[17], dfbf.iloc[22], dfbf.iloc[27], dfbf.iloc[31], dfbf.iloc[37]])
                amababilidade = np.mean([dfbf.iloc[3], dfbf.iloc[8], dfbf.iloc[13], dfbf.iloc[18], dfbf.iloc[23], dfbf.iloc[28], dfbf.iloc[33], dfbf.iloc[38], dfbf.iloc[43]])
                conscienciosidade = np.mean([dfbf.iloc[4], dfbf.iloc[9], dfbf.iloc[14], dfbf.iloc[19], dfbf.iloc[24], dfbf.iloc[29], dfbf.iloc[34], dfbf.iloc[39], dfbf.iloc[44]])
                estabilidade_emocional = np.mean([dfbf.iloc[5], dfbf.iloc[10], dfbf.iloc[15], dfbf.iloc[20], dfbf.iloc[25], dfbf.iloc[30], dfbf.iloc[35], dfbf.iloc[40]])
                abertura_a_experiencias = np.mean([dfbf.iloc[6], dfbf.iloc[11], dfbf.iloc[16], dfbf.iloc[21], dfbf.iloc[26], dfbf.iloc[31], dfbf.iloc[36], dfbf.iloc[41], dfbf.iloc[42], dfbf.iloc[45]])
                col1, col2, col3 = st.columns(3)
                col4, col5, col6 = st.columns(3)
                
                def get_slider_name(v):
                    if v == 5:
                        return 'Totalmente Introvertido'
                    elif v == 4:
                        return 'Parcialmente Introvertido'
                    elif v == 3:
                        return 'Neutro'
                    elif v == 2:
                        return 'Parcialmente Extrovertido'
                    elif v == 1:
                        return 'Totalmente Extrovertido'
                
                st.write("### Extroversão")                
                col1b, col2b = st.columns(2)
                with col1b:
                    st.write("""Porque é importante? 
* Melhora habilidades interpessoais
* Maior dominância social
* Maior expressão emocional""")
                with col2b:    
                    st.write("""O que afeta? 
* Desempenho melhor(trabalho em equipe)
* Liderança aumentada
* Maior satisfação na vida e no trabalho""")
                st.select_slider(
                        label="",
                        key="sextroversao",
                        options=['Extrovertido', 'Parcialmente Extrovertido', 'Neutro', 'Parcialmente Introvertido', 'Introvertido'],
                        value=(get_slider_name(round(extroversao)),get_slider_name(round(extroversao))),
                        #disabled=True, 
                        label_visibility ="hidden"
                )
                col1b, col2b = st.columns(2)
                with col1b:
                    st.write("Extrovertido = (agregador, assertivo, sociável, falador, expansivo)")
                with col2b:    
                    st.write("Introvertido = (reservado, tímido, quieto, sóbrio)")
                st.divider()
                
                
                st.write("### Amababilidade")
                col1b, col2b = st.columns(2)
                with col1b:
                    st.write("""Porque é importante? 
* Mais "amado"
* Menos contestador e mais conformado""")
                with col2b:    
                    st.write("""O que afeta? 
* Melhora desempenho (trabalho em equipe)
* Níveis menores de desvios de comportamento no trabalho
""")
                st.select_slider(
                        label="",
                        key="samababilidade",
                        options=['Extrovertido', 'Parcialmente Extrovertido', 'Neutro', 'Parcialmente Introvertido', 'Introvertido'],
                        value=(get_slider_name(round(amababilidade)),get_slider_name(round(amababilidade))),
                        #disabled=True, 
                        label_visibility ="hidden"
                )
                col1b, col2b = st.columns(2)
                with col1b:
                    st.write("Amáveis = (cooperativo, receptivo, confiável, solidário,  gentil, grato)")
                with col2b:
                    st.write("Antagonista = (frio, desagradável, confrontador, crítico, frio, inamistoso)")
                st.divider()
                
                
                st.write("### Conscienciosidade")
                col1b, col2b = st.columns(2)
                with col1b:
                    st.write("""Porque é importante? 
* Maior esforço e persistência
* Naus energia e disciplina
* Mais organizado e planejador""")
                with col2b:    
                    st.write("""O que afeta? 
* Melhor desempenho
* Lidernaça aumentada
* Maior longevidade
""")
                st.select_slider(
                        label="",
                        key="sconscienciosidade",
                        options=['Extrovertido', 'Parcialmente Extrovertido', 'Neutro', 'Parcialmente Introvertido', 'Introvertido'],
                        value=(get_slider_name(round(conscienciosidade)),get_slider_name(round(conscienciosidade))),
                        #disabled=True, 
                        label_visibility ="hidden"
                )
                col1b, col2b = st.columns(2)
                with col1b:
                    st.write("Consciencioso = (responsável, organizado, confiável, persistente, cuidadoso, disciplinado)")
                with col2b:
                    st.write("Desorganizado = (distraído, desorganizado, pouco confiável, descuidado, impulsivo)")
                st.divider()
                
                
                st.write("### Estabilidade Emocional")
                col1b, col2b = st.columns(2)
                with col1b:
                    st.write("""Porque é importante? 
* Menos pensamentos e emoções negativos
* menor hipervigilância""")
                with col2b:    
                    st.write("""O que afeta? 
* Maior satisfação pessoal e no trabalho
* Menores níveis de estresse
""")
                st.select_slider(
                        label="",
                        key="sestabilidade_emocional",
                        options=['Extrovertido', 'Parcialmente Extrovertido', 'Neutro', 'Parcialmente Introvertido', 'Introvertido'],
                        value=(get_slider_name(round(estabilidade_emocional)),get_slider_name(round(estabilidade_emocional))),
                        #disabled=True, 
                        label_visibility ="hidden"
                )
                col1b, col2b = st.columns(2)
                with col1b:
                    st.write("Estável emoc. = (calmo, autoconfiante, seguro, estável)")
                with col2b:
                    st.write("Instável emoc. = (nervoso, ansioso, deprimido, inseguro, tenso)")
                st.divider()  
                
                
                st.write("### Abertura a experiencias")
                col1b, col2b = st.columns(2)
                with col1b:
                    st.write("""Porque é importante? 
* Aumento do nível de aprendizagem
* Mais criatividade
* Maior flexibilidade e autonomia""")
                with col2b:    
                    st.write("""O que afeta? 
* Desempenho no treinamento
* Liderança aumentada
* Mais adaptável a mudanças
""")
                st.select_slider(
                        label="",
                        key="sabertura_a_experiencias",
                        options=['Extrovertido', 'Parcialmente Extrovertido', 'Neutro', 'Parcialmente Introvertido', 'Introvertido'],
                        value=(get_slider_name(round(abertura_a_experiencias)),get_slider_name(round(abertura_a_experiencias))),
                        #disabled=True, 
                        label_visibility ="hidden"
                )
                col1b, col2b = st.columns(2)
                with col1b:
                    st.write("Aberto a exper. = (criativo, curioso, sensível artisiticamente, independente, imaginativo)")
                with col2b:
                    st.write("Convencional. = (convencional, conservador, prefere coisas familiares, conformista, prático)")
                    
                
            else:
                st.warning("Aluno ainda não respondeu ao questionário.")

    with autorregulacao:
        analise, grafico, dados  = st.tabs(["Análise", "Gráfico", "Dados"])
        
        with dados:
            df_quest_reg = st.session_state["df_respostas"] 
            if len (df_quest_reg[df_quest_reg["Nome de usuário"] == email_estudante_selecionado]) > 0:
                df_quest_reg_s = df_quest_reg[df_quest_reg["Nome de usuário"] == email_estudante_selecionado].iloc[0]
                df_quest_reg_s
            else: 
                st.warning("Aluno ainda não respondeu ao questionário.")

        with analise:
            df_quest_reg = st.session_state["df_respostas"]
            if len (df_quest_reg[df_quest_reg["Nome de usuário"] == email_estudante_selecionado]) > 0:
                dfreg = df_quest_reg[df_quest_reg["Nome de usuário"] == email_estudante_selecionado].iloc[0]   
                media_orientacao_metas_intrinsecas = np.mean([dfreg.iloc[2], dfreg.iloc[3]])
                media_orientacao_metas_extrinsicas = np.mean([dfreg.iloc[4], dfreg.iloc[5]])
                media_valorizacao_da_atividade = np.mean([dfreg.iloc[6], dfreg.iloc[7], dfreg.iloc[8], dfreg.iloc[9], dfreg.iloc[10], dfreg.iloc[11]])
                controle_do_aprendizado = np.mean([dfreg.iloc[12], dfreg.iloc[13], dfreg.iloc[14]])
                autoeficacia_para_aprendizado = np.mean([dfreg.iloc[15], dfreg.iloc[16], dfreg.iloc[17], dfreg.iloc[18]])
                ansiedade_em_testes = np.mean([dfreg.iloc[19], dfreg.iloc[20], dfreg.iloc[21], dfreg.iloc[22], dfreg.iloc[23]])

                st.success("Escalas de Motivação")
                col1, col2, col3 = st.columns(3)
                col4, col5, col6 = st.columns(3)
                
                help_intrisica = """
                                 A orientação a metas intrínsecas diz respeito ao grau em que o aluno percebe
                                 estar participando de uma tarefa por razões como desafio, curiosidade e domínio.
                                 """
                col1.metric("Orientação a Metas Intrínsecas ", round(media_orientacao_metas_intrinsecas, 1), "-BAIXA" if (round(media_orientacao_metas_intrinsecas, 1) < limite) else "ALTA", help = help_intrisica)
                
                help_extrinsica = """
                                  A orientação extrínseca complementa a orientação intrínseca e diz respeito ao grau 
                                  em que o aluno percebe estar participando de uma tarefa por razões como notas, recompensas, desempenho, avaliação e competição.
                                  """
                col2.metric("Orientação a Metas Extrínsicas ", round(media_orientacao_metas_extrinsicas, 1), "-BAIXA" if (round(media_orientacao_metas_extrinsicas, 1) < limite) else "ALTA", help= help_extrinsica)
                
                help_valorizacao = """
                                   A valorização da atividade, difere da orientação a metas, pois ela refere-se à
                                   avaliação do aluno sobre quão interessante, importante e útil é a atividade, enquanto a orientação 
                                   a metas associa-se aos motivos pelos quais o aluno está participando da atividade.
                                   """
                col3.metric("Valorização da Atividade ", round(media_valorizacao_da_atividade, 1), "-BAIXA" if (round(media_valorizacao_da_atividade, 1) < limite) else "ALTA", help = help_valorizacao)
                
                help_controle = """
                                O controle do aprendizado, se refere às crenças dos alunos 
                                de que seus esforços para aprender resultarão em resultados positivos, onde os resultados dependem do próprio esforço.
                                """ 
                col4.metric("Controle do Aprendizado ", round(controle_do_aprendizado, 1), "-BAIXA" if (round(controle_do_aprendizado, 1) < limite) else "ALTA", help = help_controle)
                
                help_expectativa = """
                                    Os itens que compõem esta escala avaliam dois aspectos da expectativa, a
                                    expectativa de sucesso e a autoeficácia. A expectativa de sucesso refere-se 
                                    às expectativas de desempenho e especificamente ao desempenho da atividade, 
                                    enquanto a autoeficácia é uma autoavaliação da capacidade de dominar uma tarefa.
                                    Essa é uma medida da sua percepção quanto ao seu potencial de sucesso nas
                                    disciplinas e da sua autoconfiança para entender o conteúdo da disciplina. 
                                    Uma pontuação alta significa que você acha que terá bom desempenho na disciplina 
                                    e está confiante que será capaz de dominar todo o conteúdo.
                                    """
                col5.metric("Expectativa de Sucess e Autoeficacia para Aprendizado ", round(autoeficacia_para_aprendizado,1), "-BAIXA" if (round(autoeficacia_para_aprendizado, 1) < limite) else "ALTA", help = help_expectativa)
                
                help_ansiedade = """A ansiedade em testes possui dois componentes, o componente preocupação, que são os pensamentos negativos dos alunos que 
                                    atrapalham o desempenho, e o componente emocional, que se refere a aspectos de excitação afetiva e fisiológica da ansiedade. 
                                    A preocupação cognitiva e a preocupação com o desempenho são as maiores fontes de redução do desempenho, por isso, 
                                    o treinamento no uso de estratégias eficazes de aprendizado e nas habilidades para fazer testes deve ajudar a reduzir 
                                    o grau de ansiedade. Essa é uma medida do quanto você se preocupa com as avaliações e quão frequentemente você 
                                    se distrai ao realizar uma prova. Ao contrário das outras escalas, nessa escala, uma pontuação alta significa 
                                    que você fica ansioso em situações de teste."""
                col6.metric("Ansiedade em testes ", round(ansiedade_em_testes, 1), "-BAIXA" if (round(ansiedade_em_testes, 1) < limite) else "ALTA", help=help_ansiedade)
                
                st.divider()
                st.success("Escalas de Estratégias de aprendizagem")
                col7, col8, col9 = st.columns(3)
                col10, col11, col12 = st.columns(3)
                col13, col14, col15 = st.columns(3)
                
                ensaio_memorizacao = np.mean([dfreg.iloc[24], dfreg.iloc[25], dfreg.iloc[26], dfreg.iloc[27], dfreg.iloc[28]]) 
                elaboracao = np.mean([dfreg.iloc[29], dfreg.iloc[30]]) 
                organizacao = np.mean([dfreg.iloc[31], dfreg.iloc[32], dfreg.iloc[33]]) 
                pensamento_critico = np.mean([dfreg.iloc[34]]) 
                autorregulacao_metacognitiva = np.mean([dfreg.iloc[35], dfreg.iloc[36], dfreg.iloc[37], dfreg.iloc[38], dfreg.iloc[39]]) 
                tempo_e_ambiente_de_estudo = np.mean([dfreg.iloc[40]]) 
                administracao_de_esforcos = np.mean([dfreg.iloc[41], dfreg.iloc[42], dfreg.iloc[43], dfreg.iloc[44], dfreg.iloc[45]]) 
                
                help_ensaio = """
                              Esta escala mede o quanto você utiliza estratégias de estudo, como releitura
                              de anotações da aula e de textos sobre a matéria e decora listas com palavras-chave e conceitos. 
                              Uma alta pontuação significa que você usa essas estratégias com frequência.
                              """
                col7.metric("Ensaio memorização ", round(ensaio_memorizacao, 1), "-BAIXA" if (round(ensaio_memorizacao, 1) < limite) else "ALTA", help = help_ensaio)
                
                help_elaboracao = """
                                  Esta escala mede o quanto você tenta resumir ou parafrasear (colocar nas
                                  suas próprias palavras) o que você lê em seus livros-texto e o quanto você tenta relacionar 
                                  esse material com o que já sabe ou aprendeu. Uma pontuação alta significa que você usa essas estratégias 
                                  com frequência. Essas estratégias normalmente têm melhores resultados do que a estratégia de decorar.
                                  """
                col8.metric("Elaboração ", round(elaboracao, 1), "-BAIXA" if (round(elaboracao, 1) < limite) else "ALTA", help = help_elaboracao)
                
                help_organizacao = """
                                   Esta escala se refere à sua capacidade de selecionar as ideias principais do que você lê, 
                                   assim como sua capacidade de organizar e reunir tudo que precisa aprender em determinada disciplina.
                                   """
                col9.metric("Organização ", round(organizacao, 1), "-BAIXA" if (round(organizacao, 1) < limite) else "ALTA", help = help_organizacao)
                
                # está faltando                
                col10.metric("Pensamento crítico ", round(pensamento_critico, 1), "-BAIXA" if (round(pensamento_critico, 1) < limite) else "ALTA")
                
                help_autorregulacao_meta = """
                                           Esta é uma medida da frequência com que você pensa sobre o que está lendo
                                           ou estudando quando realiza suas tarefas de estudo. Por exemplo, você monitora sua atenção 
                                           quando lê ou geralmente descobre que leu dez páginas de um livro e não se lembra de nada do que leu? 
                                           Você ajusta sua velocidade de leitura quando está lendo algo difícil, se comparado a ler jornal? 
                                           Uma pontuação alta significa que você tenta planejar seu trabalho e confere se entendeu a disciplina.
                                           """
                col11.metric("Autorregulacao Metacognitiva ", round(autorregulacao_metacognitiva, 1), "-BAIXA" if (round(autorregulacao_metacognitiva, 1) < limite) else "ALTA", help = help_autorregulacao_meta)
                
                help_tempo = """
                            Essa escala mede quão bem você administra seu tempo e sua agenda, como
                            também seu uso de um ambiente de estudo. Uma pontuação alta significa que você possui um método 
                            para administrar sua agenda e tenta estudar em um local onde você possa terminar suas tarefas de estudo.
                            """
                col12.metric("Tempo e ambiente de estudo ", round(tempo_e_ambiente_de_estudo, 1), "-BAIXA" if (round(tempo_e_ambiente_de_estudo, 1) < limite) else "ALTA", help = help_tempo)
                
                help_admesforcos = """
                                   Esta escala se refere à sua vontade de fazer suas tarefas de estudo, mesmo
                                   quando o trabalho é difícil. Uma pontuação alta significa que você se esforça bastante em seus estudos.
                                   """
                col13.metric("Administração de esforços ", round(administracao_de_esforcos,1), "-BAIXA" if (round(administracao_de_esforcos, 1) < limite) else "ALTA", help = help_admesforcos)
            else:
                st.warning("Aluno ainda não respondeu ao questionário.")
                    
        with grafico:
            df_quest_reg = st.session_state["df_respostas"]
            if len (df_quest_reg[df_quest_reg["Nome de usuário"] == email_estudante_selecionado]) > 0:
                dfreg = df_quest_reg[df_quest_reg["Nome de usuário"] == email_estudante_selecionado].iloc[0]
                media_orientacao_metas_intrinsecas = np.mean([dfreg.iloc[2], dfreg.iloc[3]])
                media_orientacao_metas_extrinsicas = np.mean([dfreg.iloc[4], dfreg.iloc[5]])
                media_valorizacao_da_atividade = np.mean([dfreg.iloc[6], dfreg.iloc[7], dfreg.iloc[8], dfreg.iloc[9], dfreg.iloc[10], dfreg.iloc[11]])
                controle_do_aprendizado = np.mean([dfreg.iloc[12], dfreg.iloc[13], dfreg.iloc[14]])
                autoeficacia_para_aprendizado = np.mean([dfreg.iloc[15], dfreg.iloc[16], dfreg.iloc[17], dfreg.iloc[18]])
                ansiedade_em_testes = np.mean([dfreg.iloc[19], dfreg.iloc[20], dfreg.iloc[21], dfreg.iloc[22], dfreg.iloc[23]])
                ensaio_memorizacao = np.mean([dfreg.iloc[24], dfreg.iloc[25], dfreg.iloc[26], dfreg.iloc[27], dfreg.iloc[28]]) 
                elaboracao = np.mean([dfreg.iloc[29], dfreg.iloc[30]]) 
                organizacao = np.mean([dfreg.iloc[31], dfreg.iloc[32], dfreg.iloc[33]]) 
                pensamento_critico = np.mean([dfreg.iloc[34]]) 
                autorregulacao_metacognitiva = np.mean([dfreg.iloc[35], dfreg.iloc[36], dfreg.iloc[37], dfreg.iloc[38], dfreg.iloc[39]]) 
                tempo_e_ambiente_de_estudo = np.mean([dfreg.iloc[40]]) 
                administracao_de_esforcos = np.mean([dfreg.iloc[41], dfreg.iloc[42], dfreg.iloc[43], dfreg.iloc[44], dfreg.iloc[45]]) 
                
                st.success("Escalas de Motivação")
                fig, ax = plt.subplots()
                constructors = ["Orientação a metas intrinsecas", "Orientação a metas extrinsicas", "Valorização da atividade", "Controle doaprendizado",
                "Autoeficacia para aprendizado", "Ansiedade em testes"]
                counts = [media_orientacao_metas_intrinsecas, media_orientacao_metas_extrinsicas, media_valorizacao_da_atividade,controle_do_aprendizado, autoeficacia_para_aprendizado, ansiedade_em_testes]
                graf1 = ax.barh(constructors, counts, color='#909090')
                ax.bar_label(graf1, fmt="%.01f", size=10, label_type="edge")
                ax.set_xlabel('Resposta')
                ax.set_xticks([1,2,3,4,5,6,7])
                
                st.pyplot(plt)
                st.divider()
                st.success("Escalas de Estratégias de aprendizagem")
                fig, ax = plt.subplots()
                constructors = ["Ensaio memorização","Elaboração","Organização","Pensamento crítico","Autorregulacao Metacognitiva","Tempo e ambiente de estudo","Administração de esforços"]
                counts = [ensaio_memorizacao,elaboracao,organizacao,pensamento_critico,autorregulacao_metacognitiva,tempo_e_ambiente_de_estudo,administracao_de_esforcos]
                graf1 = ax.barh(constructors, counts, color='#909090')
                ax.bar_label(graf1, fmt="%.01f", size=10, label_type="edge")
                ax.set_xlabel('Resposta')
                ax.set_xticks([1,2,3,4,5,6,7])
                st.pyplot(plt)
            else:
                st.warning("Aluno ainda não respondeu ao questionário.")
    with dicas:
        dicas_automaticas, dicas_do_professor = st.tabs(["Recomendação automatica autorregulação", "Recomendação personalizada"])
        with dicas_do_professor:
            st.success("Enviar uma recomendação personalizada para este aluno")
            txt_titulo_dica_prof = st.text_input("Título", key="txt_titulo_dica_prof")
            txt_desc_dica_prof = st.text_area("Descrição", key="txt_desc_dica_prof")
            btn_enviar_dica_professor = st.button("Enviar", key ="btndicaprofessor")

        def enviar_dica_professor(student_id, titulo, descricao):
            token = st.session_state['token']
            classroom = build('classroom', 'v1', credentials=Credentials(token=token.get("access_token")))
            dica = {
                    'title': titulo,
                    'description': descricao,
                    'state': 'PUBLISHED',
                    "assigneeMode": "INDIVIDUAL_STUDENTS",
                    "individualStudentsOptions": { "studentIds": [student_id] }
                }
            dica_enviada = classroom.courses().courseWorkMaterials().create(courseId=id_curso_selecionado, body=dica).execute()
            (f"Diva enviada para o sala de aula do estudante:  {dica_enviada.get('id')}")
            
        if btn_enviar_dica_professor:
            enviar_dica_professor(id_estudante_selecionado, txt_titulo_dica_prof, txt_desc_dica_prof)
            
        with dicas_automaticas:
            st.success("Dicas automáticas identenficadas pela análise do perfil de autorregulação")
            
            df_quest_reg = st.session_state["df_respostas"]
            if len (df_quest_reg[df_quest_reg["Nome de usuário"] == email_estudante_selecionado]) > 0:
                btn_enviar_dica_automaticas = st.button("Enviar todas", key ="btndicaautomatica")
                dfreg = df_quest_reg[df_quest_reg["Nome de usuário"] == email_estudante_selecionado].iloc[0]
                
                media_orientacao_metas_intrinsecas = np.mean([dfreg.iloc[2], dfreg.iloc[3]])
                media_orientacao_metas_extrinsicas = np.mean([dfreg.iloc[4], dfreg.iloc[5]])
                media_valorizacao_da_atividade = np.mean([dfreg.iloc[6], dfreg.iloc[7], dfreg.iloc[8], dfreg.iloc[9], dfreg.iloc[10], dfreg.iloc[11]])
                controle_do_aprendizado = np.mean([dfreg.iloc[12], dfreg.iloc[13], dfreg.iloc[14]])
                autoeficacia_para_aprendizado = np.mean([dfreg.iloc[15], dfreg.iloc[16], dfreg.iloc[17], dfreg.iloc[18]])
                ansiedade_em_testes = np.mean([dfreg.iloc[19], dfreg.iloc[20], dfreg.iloc[21], dfreg.iloc[22], dfreg.iloc[23]])
                ensaio_memorizacao = np.mean([dfreg.iloc[24], dfreg.iloc[25], dfreg.iloc[26], dfreg.iloc[27], dfreg.iloc[28]]) 
                elaboracao = np.mean([dfreg.iloc[29], dfreg.iloc[30]]) 
                organizacao = np.mean([dfreg.iloc[31], dfreg.iloc[32], dfreg.iloc[33]]) 
                pensamento_critico = np.mean([dfreg.iloc[34]]) 
                autorregulacao_metacognitiva = np.mean([dfreg.iloc[35], dfreg.iloc[36], dfreg.iloc[37], dfreg.iloc[38], dfreg.iloc[39]]) 
                tempo_e_ambiente_de_estudo = np.mean([dfreg.iloc[40]]) 
                administracao_de_esforcos = np.mean([dfreg.iloc[41], dfreg.iloc[42], dfreg.iloc[43], dfreg.iloc[44], dfreg.iloc[45]]) 
                
                df_dicas = st.session_state["df_dicas"]
                st.divider()
                
                if (media_orientacao_metas_intrinsecas <= limite) or (media_orientacao_metas_extrinsicas <= limite) or (media_valorizacao_da_atividade <= limite) or (controle_do_aprendizado <= limite):
                    st.write("Motivo: baixa capacidade de Orientação à metas intrínsecas")
                    st.write("Dica:")
                    for l in str(df_dicas["dicas"].iloc[0]).split(" / "):
                        st.success(l)
                    st.divider()
                if autoeficacia_para_aprendizado <= limite:
                    st.write("Motivo: baixa capacidade de autoeficácia no aprendizado")
                    st.write("Dica:")
                    for l in str(df_dicas["dicas"].iloc[1]).split(" / "):
                        st.success(l)
                    st.divider()
                if ansiedade_em_testes <= limite:
                    st.markdown("Motivo: baixa ansiedade em testes")
                    st.write("Dica:")
                    for l in str(df_dicas["dicas"].iloc[2]).split(" / "):
                        st.success(l)
                    st.divider()
                if ensaio_memorizacao <= limite:
                    st.write("Motivo: baixa memorização")
                    st.write("Dica:")
                    for l in str(df_dicas["dicas"].iloc[3]).split(" / "):
                        st.success(l)
                    st.divider()
                if elaboracao <= limite:
                    st.write("Motivo: baixa elaboração")
                    st.write("Dica:")
                    for l in str(df_dicas["dicas"].iloc[4]).split(" / "):
                        st.success(l)
                    st.divider()
                if organizacao <= limite:
                    st.write("Motivo: baixa organização")
                    st.write("Dica:")
                    for l in str(df_dicas["dicas"].iloc[5]).split(" / "):
                        st.success(l)
                    st.divider()
                #if pensamento_critico <= 3:
                #    st.write(df_dicas["dicas"].iloc[2])
                if autorregulacao_metacognitiva <= limite:
                    st.write("Motivo: baixa autorregulação metacognitiva")
                    st.write("Dica:")
                    for l in str(df_dicas["dicas"].iloc[6]).split(" / "):
                        st.success(l)
                    st.divider()
                if tempo_e_ambiente_de_estudo <= limite:
                    st.write("Motivo: baixo tempo e ambiente de estudo")
                    st.write("Dica:")
                    for l in str(df_dicas["dicas"].iloc[7]).split(" / "):
                        st.success(l)
                    st.divider()
                if administracao_de_esforcos <= limite:
                    st.write("Motivo: baixo administração de esforços")
                    st.write("Dica:")
                    for l in str(df_dicas["dicas"].iloc[8]).split(" / "):
                        st.success(l)
                    st.divider()
                
                if btn_enviar_dica_automaticas:
                    if media_orientacao_metas_intrinsecas <= 4 or media_orientacao_metas_extrinsicas <= 3 or media_valorizacao_da_atividade <= 3 or controle_do_aprendizado <= 3:
                        enviar_dica_professor(id_estudante_selecionado, "Dica: " + df_dicas["constructo"].iloc[0], df_dicas["dicas"].iloc[0])
                    if autoeficacia_para_aprendizado <= 4:
                        enviar_dica_professor(id_estudante_selecionado, "Dica: " + df_dicas["constructo"].iloc[1], df_dicas["dicas"].iloc[1])
                    if ansiedade_em_testes <= 4:
                        enviar_dica_professor(id_estudante_selecionado, "Dica: " + df_dicas["constructo"].iloc[2], df_dicas["dicas"].iloc[2])
                    if ensaio_memorizacao <= 4:
                        enviar_dica_professor(id_estudante_selecionado, "Dica: " + df_dicas["constructo"].iloc[3], df_dicas["dicas"].iloc[3])
                    if elaboracao <= 4:
                        enviar_dica_professor(id_estudante_selecionado, "Dica: " + df_dicas["constructo"].iloc[4], df_dicas["dicas"].iloc[4])
                    if organizacao <= 4:
                        enviar_dica_professor(id_estudante_selecionado, "Dica: " + df_dicas["constructo"].iloc[5], df_dicas["dicas"].iloc[5])
                    if autorregulacao_metacognitiva <= 4:
                        enviar_dica_professor(id_estudante_selecionado, "Dica: " + df_dicas["constructo"].iloc[6], df_dicas["dicas"].iloc[6])
                    if tempo_e_ambiente_de_estudo <= 4:
                        enviar_dica_professor(id_estudante_selecionado, "Dica: " + df_dicas["constructo"].iloc[7], df_dicas["dicas"].iloc[7])
                    if administracao_de_esforcos <= 4:
                        enviar_dica_professor(id_estudante_selecionado, "Dica: " + df_dicas["constructo"].iloc[8], df_dicas["dicas"].iloc[8])
            else:
                st.warning("Aluno ainda não respondeu ao questionário.")    