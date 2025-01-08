version: '3.9'
services:
  minio:
    image: minio/minio
    container_name: minio
    environment:
      MINIO_ROOT_USER: {COLOQUE AQUI O NOME DO USUÁRIO DO MINIO, PADRÃO: minioadmin}
      MINIO_ROOT_PASSWORD: {COLOQUE AQUI A SENHA DO MINIO, PADRÃO: minioadmin}
    ports:
      - "9000:9000" # Porta de acesso à API do MinIO
      - "9001:9001" # Porta de acesso ao console do MinIO
    volumes:
      - ./data:/data # Mapeie o diretório local "data" para armazenar os arquivos no MinIO
    command: server /data --console-address ":9001"

  trino:
    image: trinodb/trino
    container_name: trino
    ports:
      - "8080:8080" # Porta para acessar o Trino
    # OBS: Você pode adicionar configurações personalizadas nos arquivos do Trino na pasta ./configs se necessário.

  postgres:
    image: postgres
    container_name: postgres
    environment:
      POSTGRES_USER: {COLOQUE AQUI O NOME DO USUÁRIO DO POSTGRES, PADRÃO: postgres}
      POSTGRES_PASSWORD: {COLOQUE AQUI A SENHA DO POSTGRES, PADRÃO: postgres}
      POSTGRES_DB: {COLOQUE AQUI O NOME DO BANCO DE DADOS, PADRÃO: spotify}
    ports:
      - "5432:5432" # Porta padrão para conexões PostgreSQL
    volumes:
      - ./postgres_data:/var/lib/postgresql/data # Diretório persistente para dados do Postgres

  superset:
    image: apache/superset
    container_name: superset
    environment:
      SUPERSET_LOAD_EXAMPLES: "no" # Não carregar exemplos no Superset (altere para "yes" se desejar exemplos)
      SUPERSET_SECRET_KEY: {COLOQUE AQUI UMA CHAVE SECRETA PARA O SUPERSET}
      SUPERSET_DATABASE_URL: {URL DE CONEXÃO DO POSTGRES, PADRÃO: postgresql+psycopg2://postgres:postgres@postgres:5432/spotify}
    ports:
      - "8088:8088" # Porta de acesso ao Superset
    depends_on:
      - postgres # Garante que o PostgreSQL será iniciado antes do Superset

