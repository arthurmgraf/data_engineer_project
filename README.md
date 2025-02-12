Data Pipeline Spotify: Análise Musical com Arquitetura Medalhão na AWS
[]

Visão Geral do Projeto
Este projeto demonstra a construção de um pipeline de dados robusto e escalável para análise de dados musicais da API do Spotify.  Utilizando a arquitetura Medalhão na AWS, o pipeline ingere dados brutos, os refina em camadas de qualidade crescente e, finalmente, os disponibiliza para visualização interativa em dashboards.

O objetivo principal deste projeto é apresentar um portfólio impressionante no LinkedIn, destacando habilidades em engenharia de dados com tecnologias modernas e demandadas no mercado.

Tecnologias Utilizadas:

*   Orquestração e ETL/ELT: Mage.ai - Plataforma moderna para orquestração de pipelines de dados, ETL/ELT visual e colaborativo.
*   Processamento Distribuído: Spark (integrado ao Mage.ai) -  Motor de processamento rápido e escalável para grandes volumes de dados.
*   Modelagem e Transformação de Dados: DBT (Data Build Tool) (integrado ao Mage.ai) - Ferramenta para transformação de dados declarativa e versionada, com foco em qualidade e testes.
*   Data Warehouse Analítico: ClickHouse - Banco de dados colunar de alta performance, ideal para workloads analíticos e visualização rápida.
*   Data Lake: S3 AWS - Armazenamento de objetos escalável e durável na AWS, utilizado como Data Lake para todas as camadas do Medalhão.
*   Visualização de Dados: Superset - Plataforma de visualização de dados interativa e intuitiva para criação de dashboards.
*   Fonte de Dados: Spotify API - API REST do Spotify para extração de dados musicais.
*   Linguagens: Python, SQL
*   Formatos de Dados: JSON, Parquet

Arquitetura do Projeto (Medalhão Simplificada - S3 AWS)

📦 Projeto Data Pipeline Spotify (Arquitetura Medalhão Simplificada - S3 AWS)
├── 📥 Fonte de Dados: API Spotify
│   └── 📜  Bloco Mage.ai (Python) - "Captura API Spotify"
│       └── 🔗 Conexão API REST Spotify (autenticação e requisição)
│       └── 📤 Extração Data Bruto (JSON) - Artistas, Músicas, Playlists, etc.
│       └── [Caixa de Texto: Bloco Python dedicado à extração eficiente e resiliente de dados da API Spotify. Implementar retentativas e tratamento de rate limits.]
│
├── 🗂️ Data Lake S3 AWS (Medalhão)
│   ├── 📂 Bronze (Raw) - s3://<seu-bucket>/spotify-datalake/bronze/
│   │   └── 🗄️ Buckets S3 - Organização por tipo de dado e data de ingestão
│   │       └── 📜 JSON Bruto (Particionado por data) - s3://<seu-bucket>/spotify-datalake/bronze/artistas/YYYY/MM/DD/*.json
│   │           └── [Caixa de Texto: Camada de landing zone. Dados em formato original da API, sem nenhuma transformação. Foco em preservar a linhagem dos dados e permitir reprocessamento futuro.]
│   │
│   ├── 📂 Silver (Cleaned & Standardized) - s3://<seu-bucket>/spotify-datalake/silver/
│   │   └── 🗄️ Buckets S3 - Organização por tipo de dado e data de processamento
│   │       └── 📜 Parquet Limpo e Padronizado (Particionado por data) - s3://<seu-bucket>/spotify-datalake/silver/musicas/YYYY/MM/DD/*.parquet
│   │           └── [Caixa de Texto: Dados do Bronze limpos e padronizados usando Spark. Remoção de duplicatas, tratamento de nulos, conversão de tipos, padronização de formatos. Formato Parquet para eficiência em consultas analíticas.]
│   │
│   ├── 📂 Gold (Aggregated & Business Logic) - s3://<seu-bucket>/spotify-datalake/gold/ & ClickHouse (Data Warehouse)
│   │   ├── 🗄️ Buckets S3 - Dados agregados e históricos (opcional para data lake completo)
│   │   │   └── 📜 Parquet Agregado (Particionado por área de análise) - s3://<seu-bucket>/spotify-datalake/gold/tendencias_musicais/*.parquet
│   │   │       └── [Caixa de Texto: Camada Gold no S3 é opcional, focada em data lake completo e histórico. Dados agregados para análises complexas e de longo prazo. Formato Parquet.]
│   │   ├── 🗄️ ClickHouse (Data Warehouse Analítico) - banco_de_dados: spotify_gold
│   │   │   └── 🗃️ Tabelas ClickHouse - spotify_gold.artistas_populares, spotify_gold.generos_mais_escutados, etc.
│   │   │   └── [Caixa de Texto: Camada Gold otimizada para visualização e dashboards no Superset. Tabelas desnormalizadas e pré-agregadas pelo DBT para consultas de alta performance. ClickHouse como data warehouse de alta velocidade.]
│   │
│   └── [Caixa de Texto: Data Lake S3 AWS (Medalhão): S3 como foundation da arquitetura. Escalabilidade, durabilidade e custo-efetividade do S3 para armazenar dados em todas as camadas do Medalhão. Organização lógica em Bronze, Silver e Gold para qualidade e governança de dados.]
│
├── ⚙️ Mage.ai - Orquestrador & ETL/ELT
│   ├── 🧩 Pipelines de Dados Mage.ai
│   │   ├── 🌊 Pipeline Ingestão Bronze - "Bronze Ingestion Pipeline"
│   │   │   └── [Caixa de Texto: Bloco Python "Captura API Spotify" -> Bloco Output S3 "Escrever Bronze S3". Agendamento: Diário/Horário. Pipeline de ELT (Extract-Load-Transform). Extração e carga bruta para S3.]
│   │   ├── ✨ Pipeline Transformação Silver - "Silver Transformation Pipeline"
│   │   │   └── [Caixa de Texto: Bloco Input S3 "Ler Bronze S3" -> Bloco Spark "Limpeza e Padronização Spark" -> Bloco Output S3 "Escrever Silver S3". Agendamento: Após Ingestão Bronze. Pipeline ETL (Extract-Transform-Load). Leitura do Bronze, transformação com Spark, carga no Silver.]
│   │   ├── 🏆 Pipeline Transformação Gold - DBT - "Gold DBT Transformation Pipeline"
│   │   │   └── [Caixa de Texto: Bloco DBT "Modelos DBT Gold". Modelos DBT (SQL/Python) orquestrados pelo Mage.ai. Leitura do Silver S3 -> Transformação (Agregação, Lógica de Negócio) -> Output ClickHouse "Escrever Gold ClickHouse" (principal) e Output S3 "Escrever Gold S3" (opcional). Agendamento: Após Transformação Silver. Pipeline de Transformação e Modelagem com DBT.]
│   │   └── ⏱️ Agendamento e Monitoramento Mage.ai
│   │       └── [Caixa de Texto: Agendamento centralizado dos pipelines no Mage.ai. Monitoramento integrado da execução, logs e alertas. Interface visual do Mage.ai para operacionalização e troubleshooting do pipeline.]
│   │
│   ├── 🐍 Blocos Python Mage.ai - "Blocos Python"
│   │   └── 📜 Código Python - Conexão API Spotify, funções auxiliares, etc.
│   │       └── [Caixa de Texto: Blocos Python reutilizáveis dentro do Mage.ai para tarefas específicas. Código modular e versionado dentro do contexto do pipeline.]
│   │
│   ├── 🚀 Blocos Spark Mage.ai - "Blocos Spark"
│   │   └── 📜 Código Spark - Transformações Silver (limpeza, padronização)
│   │       └── [Caixa de Texto: Blocos Spark para processamento distribuído e escalável das transformações da camada Silver. Aproveitar o poder do Spark dentro do Mage.ai para grandes volumes de dados.]
│   │
│   └── [Caixa de Texto: Mage.ai - Orquestração Centralizada e Desenvolvimento Ágil: Mage.ai como orquestrador principal do pipeline de dados. Interface low-code/no-code para desenvolvimento rápido e visual de pipelines. Integração nativa com Spark e DBT. Facilidade de agendamento, monitoramento e operacionalização.]
│
├── 🛠️ DBT (Data Build Tool) - Modelagem Camada Gold
│   └── 📂 Projetos DBT - "dbt_spotify_gold"
│       └── 📜 Modelos DBT (SQL & Python) - Transformações Gold, agregações, lógica de negócio
│       └── 🧪 Testes DBT - Qualidade e integridade dos dados transformados
│       └── 📚 Documentação DBT - Autogerada, lineage e dicionário de dados
│       └── [Caixa de Texto: DBT para Modelagem e Transformação da Camada Gold: DBT para transformações declarativas e versionadas. Foco na camada Gold para visualização e análise. Testes DBT para garantir a qualidade dos dados. Documentação para governanaça e colaboração.]
│
├── 📊 Superset - Visualização & Dashboards
    └── 🎨 Dashboards Superset - "Dashboards Analíticos Spotify"
        └── 📈 Visualizações Interativas - Gráficos, tabelas, mapas, etc.
        └── 🔗 Conexão Direta ClickHouse - Fonte de dados: Tabelas Gold ClickHouse
        └── [Caixa de Texto: Superset para Visualização e Exploração: Superset conectado diretamente ao ClickHouse (sem Trino para simplificar). Dashboards interativos e visualmente atraentes apresentando insights dos dados Spotify. Foco na experiência do usuário e storytelling com dados.]




Detalhes da Arquitetura
A arquitetura do projeto é baseada no padrão Medalhão, uma abordagem comprovada para organizar dados em um data lake, garantindo qualidade e facilitando o consumo. Cada camada tem um propósito específico:

*   Bronze (Raw):  Esta é a camada inicial, onde os dados brutos da API do Spotify são armazenados em seu formato original (JSON). O foco aqui é a preservação da linhagem dos dados, permitindo reprocessamento futuro caso necessário. Os dados são particionados por data para otimizar o gerenciamento e consultas.

*   Silver (Cleaned & Standardized):  Nesta camada, os dados do Bronze passam por um processo de limpeza e padronização utilizando Spark. Isso inclui a remoção de duplicatas, tratamento de valores nulos, conversão de tipos de dados e padronização de formatos. O formato Parquet é utilizado para otimizar a eficiência em consultas analíticas.

*   Gold (Aggregated & Business Logic) & ClickHouse (Data Warehouse):  A camada Gold representa os dados transformados e agregados, prontos para responder a perguntas de negócio e gerar insights.  Utilizamos o DBT para modelar esses dados, aplicando lógicas de negócio e realizando agregações.

*   S3 (Opcional):  Uma parte da camada Gold pode ser armazenada no S3, em formato Parquet, para manter um data lake completo e histórico, ideal para análises de longo prazo e cenários futuros.
    *   ClickHouse (Principal):  A principal parte da camada Gold é carregada no ClickHouse, um data warehouse analítico de alta performance. As tabelas no ClickHouse são desnormalizadas e pré-agregadas pelo DBT, otimizadas para consultas rápidas e visualização interativa no Superset. O ClickHouse atua como o data warehouse de alta velocidade para dashboards.

*   Mage.ai (Orquestrador & ETL/ELT):  O Mage.ai é a espinha dorsal do pipeline, orquestrando todas as etapas de ingestão e transformação.

*   Pipelines de Dados:  O Mage.ai permite criar pipelines visuais para cada etapa do Medalhão:
        *   Bronze Ingestion Pipeline (ELT): Extrai dados da API Spotify e carrega brutos no S3 (Bronze).
        *   Silver Transformation Pipeline (ETL): Lê dados do S3 (Bronze), transforma com Spark (limpeza e padronização) e carrega no S3 (Silver).
        *   Gold DBT Transformation Pipeline: Executa modelos DBT para ler dados do S3 (Silver), transformar (agregação, lógica de negócio) e carregar no ClickHouse (Gold) e, opcionalmente, no S3 (Gold).

*   Agendamento e Monitoramento: O Mage.ai oferece agendamento centralizado para execução automática dos pipelines e monitoramento integrado para garantir a confiabilidade do fluxo de dados.

*   Blocos Python e Spark: O Mage.ai integra-se nativamente com Python e Spark, permitindo criar blocos de código modularizados e reutilizáveis para tarefas específicas de extração, transformação e processamento.

*   DBT (Data Build Tool) - Modelagem da Camada Gold:  O DBT é utilizado para modelar e transformar os dados na camada Gold de forma declarativa e versionada.

*   Projetos DBT: Os modelos DBT são organizados em projetos, definindo as transformações SQL e Python, testes de qualidade de dados e documentação.
    *   Testes e Documentação: O DBT permite implementar testes para garantir a qualidade dos dados transformados e gera documentação automática, facilitando a governança e colaboração no projeto.

*   Superset (Visualização & Dashboards):  O Superset é conectado diretamente ao ClickHouse para criar dashboards interativos e visualmente atraentes.

*   Dashboards Analíticos:  Dashboards no Superset apresentam insights relevantes dos dados do Spotify, como tendências musicais, popularidade de artistas e características de músicas, com foco na experiência do usuário e storytelling com dados.

Getting Started (Execução Local com Docker Compose)
Para executar este projeto localmente, siga os passos abaixo:

Pré-requisitos:

*   Docker instalado na sua máquina.
*   Docker Compose instalado na sua máquina.

Passos:

1.  Clone este repositório:
    bash git clone [link-para-o-seu-repositorio] cd [nome-do-repositorio]

2.  Configure as variáveis de ambiente (se necessário):
    *   No momento, este projeto pode não necessitar de variáveis de ambiente complexas para rodar localmente (ex: credenciais AWS para um Minio local, se você optar por usar no futuro).  No entanto, se a API do Spotify ou outras partes do projeto exigirem configuração, você pode criar um arquivo .env na raiz do projeto e definir as variáveis lá.  O docker-compose.yml pode ser configurado para ler este arquivo.

3.  Execute o Docker Compose:
    bash docker-compose up -d
    Este comando irá iniciar todos os serviços necessários (Mage.ai, ClickHouse, Superset) em containers Docker.

4.  Acesse as interfaces web:
    *   Mage.ai UI:  Abra seu navegador e acesse http://localhost:6789.
    *   Superset UI: Abra seu navegador e acesse http://localhost:8088.  (As credenciais iniciais do Superset geralmente são admin/admin).
    *   ClickHouse CLI (Opcional):  Para acessar a linha de comando do ClickHouse dentro do container (para exploração e troubleshooting, se necessário):
        bash docker exec -it clickhouse-server clickhouse-client

Executando o Data Pipeline no Mage.ai
1.  Acesse a UI do Mage.ai: http://localhost:6789.
2.  Navegue até a seção de Pipelines.
3.  Execute os pipelines na ordem correta:
    *   Bronze Ingestion Pipeline: Para iniciar a extração de dados da API do Spotify e carregar na camada Bronze do S3 (local, se estiver usando Minio, ou AWS S3 se configurado).
    *   Silver Transformation Pipeline: Após a ingestão do Bronze, execute este pipeline para limpar e padronizar os dados e carregar na camada Silver do S3.
    *   Gold DBT Transformation Pipeline:  Por fim, execute este pipeline (DBT) para transformar e agregar os dados da camada Silver e carregar na camada Gold (S3 e ClickHouse).
4.  Monitore a execução dos pipelines:  O Mage.ai oferece uma interface visual para acompanhar o status de cada pipeline, logs e identificar possíveis erros.

Explorando Dashboards no Superset
1.  Acesse a UI do Superset: http://localhost:8088.
2.  Faça login com as credenciais iniciais (geralmente admin/admin).
3.  Navegue até a seção de Dashboards.
4.  Abra os Dashboards Analíticos Spotify:  Explore os dashboards pré-criados (ou crie seus próprios!) para visualizar os insights gerados a partir dos dados do Spotify.  Exemplos de dashboards podem incluir:
    *   Tendências Musicais por Gênero ao longo do tempo.
    *   Ranking de Artistas Mais Populares.
    *   Distribuição de Características de Áudio das Músicas por Gênero.
    *   E muito mais!

Próximos Passos e Melhorias Futuras
Este projeto pode ser expandido e aprimorado de diversas formas:

*   Integração com Machine Learning: Adicionar modelos de machine learning para recomendação de músicas, análise de sentimento em letras, etc.
*   Dados em Tempo Real (Streaming): Explorar a possibilidade de trabalhar com dados em tempo real ou quase real time da API do Spotify para dashboards dinâmicos.
*   Fontes de Dados Adicionais: Combinar dados do Spotify com outras fontes de dados (redes sociais, dados demográficos, etc.) para análises mais ricas.
*   Aprimoramento dos Dashboards:  Criar dashboards mais interativos e personalizados no Superset, explorando diferentes tipos de visualizações e métricas.
*   Implementação de CI/CD:  Configurar um pipeline de CI/CD para automatizar testes, build e deployment do pipeline Mage.ai.
*   Monitoramento Avançado: Implementar um sistema de monitoramento mais robusto com alertas e métricas detalhadas do pipeline.

Apresentando no LinkedIn
Para destacar este projeto no seu perfil do LinkedIn e impressionar recrutadores:

*   Título do Projeto: Utilize um título chamativo como "Data Pipeline Medalhão para Análise Musical com Spotify API, Mage.ai, Spark, ClickHouse, Superset e DBT".
*   Descrição Detalhada: Na seção de projetos do LinkedIn, forneça uma descrição clara e concisa do projeto, destacando as tecnologias utilizadas, a arquitetura Medalhão e os principais insights que você obteve.
*   Link para o GitHub: Inclua um link direto para este repositório do GitHub para que recrutadores possam explorar o código e a documentação.
*   Demonstração Visual: Adicione screenshots dos dashboards do Superset no README do GitHub e, idealmente, inclua um vídeo curto (screencast) demonstrando os dashboards em ação.
*   Palavras-chave: Utilize palavras-chave relevantes para engenharia de dados (Data Engineering, Data Pipeline, Cloud, AWS, Mage.ai, Spark, DBT, ClickHouse, Superset, Data Lake, Data Warehouse, etc.) na descrição do projeto e no seu perfil do LinkedIn.
*   Compartilhe um Post: Após publicar o projeto, faça um post no LinkedIn compartilhando com sua rede. Explique o que você construiu, as tecnologias utilizadas e convide as pessoas a conferirem o repositório no GitHub.

Disclaimer
Este projeto é desenvolvido para fins educacionais e de demonstração de habilidades em engenharia de dados.  O uso da API do Spotify está sujeito aos termos de serviço e limitações de rate limiting da plataforma.  Certifique-se de respeitar a privacidade dos dados e os termos de uso da API do Spotify.

Licença
[Escolha sua licença - Exemplo: MIT License] (Opcional)

Autor
Arthur Maia Graf - (https://github.com/arthurmgraf)
