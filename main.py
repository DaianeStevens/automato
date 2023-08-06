# Daiane, Chaiene e Liara
# Utilizamos o anaconda prompt para executar a atividade | python + streamlit
# Instalamos o anaconda, abrimos o prompt anaconda e instalamos o streamlit - pip install streamlit
# Depois executamos o arquivo - streamlit run C:\Users\daias\Projetos\ProjetosAula\LinguagensFormaisCompiladores\main.py

import streamlit as st
from automato import Automato

st.header('Atividade 01')
st.markdown('Desenvolver um programa que implementa um autômato (específico) que reconhece todas as palavras terminadas em: ção')

palavra = st.text_input(label="Digite uma palavra:")
automato = Automato()

if st.button('Testar Autômato'):
    if automato.verificar_palavra(palavra):
        st.success(f"A palavra '{palavra}' é reconhecida pelo autômato.")
    else:
        st.error(f"A palavra '{palavra}' NÃO é reconhecida pelo autômato.")
