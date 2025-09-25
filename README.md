# E-mails-e-Automacao
Um script em Python para automatizar o envio de e-mails em massa usando Gmail (SMTP + Senha de App). Inclui a função de Mala Direta (Mail Merge) através de uma planilha Excel/CSV para personalizar o assunto e a mensagem de cada destinatário.


 Funcionalidades
Envio de e-mails em massa pelo Gmail.
Suporte a múltiplos destinatários.
Personalização das mensagens com dados da planilha (colunas A e B).
Fácil configuração e uso.

Tecnologias utilizadas

Python 3
smtplib
openpyxl (ou pandas)

**** Como Usar o Script
Para rodar este projeto na sua máquina, siga os passos abaixo:

1. Instale as Dependências
Primeiro, você precisa ter o Python instalado. Depois, instale as bibliotecas necessárias usando o pip:

Bash
pip install pandas python-dotenv openpyxl

2. Configure o Arquivo .env
Modifique um arquivo chamado .env na mesma pasta do script.

EMAIL_USER=seu_email@exemplo.com
EMAIL_PASS=sua_senha_ou_app_password

Importante: Se você estiver usando um serviço de e-mail como o Gmail, será necessário gerar uma "senha de aplicativo" para permitir que o script acesse sua conta. Pesquise por "gerar senha de app Gmail" para encontrar as instruções.

3. Prepare a Planilha de Contatos
Edite a planilha Excel com o nome contatos.xlsx 

4. Rode o Script
Com tudo configurado, basta executar o script no terminal:

Bash

python enviar_emails.py
O script irá ler a planilha e enviar os e-mails para todos os contatos listados.

Autor
Heric Correa
