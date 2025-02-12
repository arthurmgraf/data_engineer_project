Data Pipeline Spotify: Análise Musical com Arquitetura Medalhão na AWS
[]

Visão Geral
Este projeto demonstra a construção de um pipeline de dados robusto e escalável para análise de dados musicais da API do Spotify. Utilizando a arquitetura Medalhão na AWS, o pipeline ingere dados brutos, os refina em camadas de qualidade crescente e, finalmente, os disponibiliza para visualização interativa em dashboards.

O objetivo principal é apresentar um portfólio no LinkedIn, destacando habilidades em engenharia de dados com tecnologias modernas.

Tecnologias Utilizadas
Orquestração e ETL/ELT: Mage.ai
Processamento Distribuído: Spark (integrado ao Mage.ai)
Modelagem e Transformação de Dados: DBT (Data Build Tool)
Data Warehouse Analítico: ClickHouse
Data Lake: S3 AWS
Visualização de Dados: Superset
Fonte de Dados: Spotify API
Linguagens: Python, SQL
Formatos de Dados: JSON, Parquet
Arquitetura do Projeto (Medalhão Simplificada - S3 AWS)
O projeto segue a arquitetura Medalhão, organizada em três camadas principais:

Bronze (Raw): Dados brutos da API do Spotify em formato JSON, armazenados no S3.

Silver (Cleaned & Standardized): Dados limpos e padronizados, transformados com Spark e armazenados em Parquet.

Gold (Aggregated & Business Logic): Dados agregados e modelados com DBT, armazenados no ClickHouse para análise rápida.

Fluxo de Dados
Ingestão: Dados são extraídos da API do Spotify e armazenados na camada Bronze.

Transformação: Dados da camada Bronze são limpos e padronizados na camada Silver.

Modelagem: Dados da camada Silver são agregados e modelados na camada Gold.

Visualização: Dados da camada Gold são utilizados para criar dashboards interativos no Superset.

Execução Local com Docker Compose
Pré-requisitos
Docker e Docker Compose instalados.

Passos
Clone o repositório:

```bash
git clone [link-para-o-seu-repositorio]
cd [nome-do-repositorio]
```

Configure as variáveis de ambiente (se necessário).

Execute o Docker Compose:

```bash
docker-compose up -d
```

Acesse as interfaces:

Mage.ai UI: http://localhost:6789

Superset UI: http://localhost:8088 (credenciais: admin/admin)

Executando o Data Pipeline no Mage.ai
Acesse a UI do Mage.ai.

Execute os pipelines na ordem:

Bronze Ingestion Pipeline

Silver Transformation Pipeline

Gold DBT Transformation Pipeline

Monitore a execução dos pipelines.

Explorando Dashboards no Superset
Acesse a UI do Superset.

Explore os dashboards pré-criados ou crie novos.

Próximos Passos e Melhorias Futuras
Integração com Machine Learning.

Dados em Tempo Real (Streaming).

Fontes de Dados Adicionais.

Aprimoramento dos Dashboards.

Implementação de CI/CD.

Monitoramento Avançado.

Apresentando no LinkedIn
Título do Projeto: Utilize um título chamativo.

Descrição Detalhada: Destaque tecnologias e insights.

Link para o GitHub: Inclua um link direto.

Demonstração Visual: Adicione screenshots e vídeos.

Palavras-chave: Utilize palavras-chave relevantes.

Compartilhe um Post: Compartilhe o projeto com sua rede.

Disclaimer
Este projeto é para fins educacionais e de demonstração. O uso da API do Spotify está sujeito aos termos de serviço e limitações de rate limiting.

Licença
Escolha sua licença - Exemplo: MIT License (Opcional)

Autor
Arthur Maia Graf - GitHub
