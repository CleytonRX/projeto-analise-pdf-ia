import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
from PyPDF2 import PdfReader
from pages.menu import show_menu

# Mostrar o menu
selected = show_menu()

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

# Imprimir o token da API (Somente para fins de depuração - Remova antes de enviar para produção!)


genai.configure(api_key=GOOGLE_API_KEY)

st.title('Análise de PDF com IA :sunglasses:')

uploaded_file = st.file_uploader('Escolha seu arquivo .pdf', type="pdf")
if uploaded_file is not None:
    # Ler o conteúdo do PDF
    reader = PdfReader(uploaded_file)
    text = ''
    for page in reader.pages:
        text += page.extract_text()
    
    # Salvar o texto em um arquivo temporário
    with open('temp.txt', 'w') as temp_file:
        temp_file.write(text)
    
    st.write('Texto do PDF carregado com sucesso.')

    # Verificar se o arquivo de texto não está vazio
    if os.path.getsize('temp.txt') > 0:
        st.write("Texto do PDF extraído com sucesso.")
        
        # Mostrar o conteúdo do arquivo temporário
        st.write("Conteúdo do arquivo temporário:")
        with open('temp.txt', 'r') as file:
            content = file.read()
        st.text(content)  # Exibe o conteúdo do arquivo

        # Formulário para a pergunta do usuário
        with st.form(key='query_form'):
            user_prompt = st.text_input("Faça sua pergunta sobre o conteúdo do PDF", "me diga sobre o que é este documento")
            submit_button = st.form_submit_button(label='Perguntar')
            
            if submit_button:
                try:
                    # Enviar o arquivo de texto para a API
                    text_file = genai.upload_file(path='temp.txt')
                    st.write(f"Upload concluído: {text_file.uri}")

                    model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")

                    response = model.generate_content([user_prompt, text_file],
                                                      request_options={"timeout": 600})
                    st.write(response.text)

                    # Deletar o arquivo de texto na API
                    genai.delete_file(text_file.name)
                    
                    # Remover o arquivo temporário
                    os.remove('temp.txt')
                except Exception as e:
                    st.error(f"Ocorreu um erro: {e}")
    else:
        st.error("Falha ao extrair texto do PDF. Por favor, tente outro arquivo.")
