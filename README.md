# Spotify Data Lake Project

Este projeto implementa um pipeline de dados funcional com as seguintes etapas:
1. Ingestão de dados da API do Spotify.
2. Transformação e normalização dos dados em camadas (Bronze, Silver e Gold).
3. Armazenamento em MinIO (Data Lake).
4. Consultas com Trino.
5. Visualização com Superset.

## Estrutura de Diretórios
- `data`: Armazena os dados organizados em camadas (bronze, silver, gold).
- `scripts`: Scripts para ingestão e transformação.
- `configs`: Configurações para pipelines e ferramentas.
- `docker`: Configuração para contêineres.
- `logs`: Logs de execução.
- `pipelines`: Pipelines Mage.ai.
- `notebooks`: Notebooks para análises exploratórias.

## Ferramentas Utilizadas
- Mage.ai
- MinIO
- Trino
- PostgreSQL
- Superset

