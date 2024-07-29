import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
from pages.menu import show_menu

# Mostrar o menu
selected = show_menu()

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

st.title('Perguntas para IA :thinking:')

# Campo de texto para o prompt do usuário
user_text = st.text_area("Faça uma pergunta para a IA sobre o texto fornecido:")

if st.button('Enviar'):
    if user_text:
        try:
            # Enviar o texto diretamente para a API
            response = genai.GenerativeModel(model_name="models/gemini-1.5-flash").generate_content(
                [user_text],
                request_options={"timeout": 600}
            )
            st.write(response.text)
        except Exception as e:
            st.error(f"Ocorreu um erro: {e}")
    else:
        st.error("Por favor, forneça tanto o texto quanto a pergunta.")
