import streamlit as st
from streamlit_option_menu import option_menu

# Função para mostrar o menu
def show_menu():
    st.set_page_config(page_title="A.I PDF & Perguntas", layout="wide")
    
    # Menu de navegação
    with st.sidebar:
        selected = option_menu("Menu", ["Página Inicial", "Upload PDF", "Perguntas"], 
                               icons=["house", "upload", "question-circle"], 
                               menu_icon="cast", default_index=0)
    return selected

# Mostrar o menu
selected = show_menu()

# Navegar para a página correta com base na seleção do menu
if selected == "Página Inicial":
    st.write("## Página Inicial")
    st.write("Esta é a página para upload e análise de arquivos PDF.")
    st.write("Navegue para a página de perguntas para interagir com a IA.")
elif selected == "Upload PDF":
    st.write("## Upload e Análise de PDF")
    st.write("Aqui você pode fazer o upload de um arquivo PDF para análise.")
    # Importe e execute o código da página upload_pdf.py aqui
elif selected == "Perguntas":
    st.write("## Perguntas para IA")
    st.write("Digite sua pergunta e receba uma resposta da IA.")
    # Importe e execute o código da página questions.py aqui
