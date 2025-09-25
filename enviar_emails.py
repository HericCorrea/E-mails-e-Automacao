import pandas as pd
import smtplib
import os
import time
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# --- CONFIGURAÇÕES --- 
# As credenciais são carregadas de forma segura do arquivo .env
usuario = os.getenv("GMAIL_EMAIL")
senha = os.getenv("GMAIL_APP_PASSWORD")
arquivo_planilha = "contatos.xlsx"

# --- LER PLANILHA --- 
try:
    df = pd.read_excel(arquivo_planilha)
except FileNotFoundError:
    print(f"Erro: O arquivo '{arquivo_planilha}' não foi encontrado.")
    exit()

# --- CONECTAR AO SERVIDOR SMTP E ENVIAR E-MAILS --- 
try:
    # Usa o bloco 'with' para garantir que a conexão será encerrada
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()  # Inicia uma conexão segura (TLS)
        server.login(usuario, senha)

        for index, row in df.iterrows():
            email_destinatario = row['E-mail']
            assunto = row['Assunto']
            mensagem_html = row['Mensagem']

            # Cria o e-mail
            msg = MIMEMultipart('alternative')
            msg['From'] = usuario
            msg['To'] = email_destinatario
            msg['Subject'] = assunto
            
            # Anexa a mensagem HTML ao e-mail
            msg.attach(MIMEText(mensagem_html, 'html'))

            try:
                server.send_message(msg)
                print(f"[{index+1}/51]: E-mail enviado para {email_destinatario}")
            except Exception as e:
                print(f"[{index+1}/51]: ERRO ao enviar para {email_destinatario} -> {e}")

            time.sleep(2)  # Pausa de 2 segundos para evitar limites de envio

except Exception as e:
    print(f"Erro ao conectar ou autenticar no servidor SMTP: {e}")
    exit()

print("Todos os e-mails foram processados!")