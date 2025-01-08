# Use uma imagem base do Python
FROM python:3.9-slim

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Copie o arquivo requirements.txt para o contêiner
COPY requirements.txt .

# Instale as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copie todo o código da aplicação para o contêiner
COPY . .

# Exponha a porta que sua aplicação usa (se aplicável)
EXPOSE 8888

# Comando padrão para iniciar o container (opcional)
CMD ["python", "/app/scripts/main.py"]

