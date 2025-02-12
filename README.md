# Data Pipeline Spotify: Análise Musical com Arquitetura Medalhão na AWS  

## 📌 Visão Geral  
Este projeto demonstra a construção de um pipeline de dados robusto e escalável para análise de dados musicais da API do Spotify. Utilizando a **Arquitetura Medalhão** na AWS, o pipeline ingere dados brutos, refina-os em camadas de qualidade crescente e, finalmente, os disponibiliza para visualização interativa em dashboards.  

O objetivo principal é **destacar habilidades em engenharia de dados** com tecnologias modernas, tornando este projeto um excelente portfólio no **LinkedIn**.  

---

## 🚀 Tecnologias Utilizadas  

- **Orquestração e ETL/ELT**: [Mage.ai](https://www.mage.ai/)  
- **Processamento Distribuído**: [Apache Spark](https://spark.apache.org/) (integrado ao Mage.ai)  
- **Modelagem e Transformação de Dados**: [DBT (Data Build Tool)](https://www.getdbt.com/)  
- **Data Warehouse Analítico**: [ClickHouse](https://clickhouse.com/)  
- **Data Lake**: [AWS S3](https://aws.amazon.com/s3/)  
- **Visualização de Dados**: [Apache Superset](https://superset.apache.org/)  
- **Fonte de Dados**: [Spotify API](https://developer.spotify.com/)  
- **Linguagens**: Python, SQL  
- **Formatos de Dados**: JSON, Parquet  

---

## Integração DBT com ClickHouse:

https://clickhouse.com/docs/en/integrations/dbt




## 🏗️ Arquitetura do Projeto (Medalhão Simplificada - AWS S3)  

O projeto segue a **Arquitetura Medalhão**, organizada em **três camadas principais**:  

- **Bronze (Raw)**: Dados brutos da API do Spotify em formato **JSON**, armazenados no **S3**.  
- **Silver (Cleaned & Standardized)**: Dados limpos e padronizados, transformados com **Spark** e armazenados em **Parquet**.  
- **Gold (Aggregated & Business Logic)**: Dados agregados e modelados com **DBT**, armazenados no **ClickHouse** para análise rápida.  

---

## 🔄 Fluxo de Dados  

1. **Ingestão**: Dados são extraídos da **API do Spotify** e armazenados na camada **Bronze**.  
2. **Transformação**: Dados da camada **Bronze** são limpos e padronizados na camada **Silver**.  
3. **Modelagem**: Dados da camada **Silver** são agregados e modelados na camada **Gold**.  
4. **Visualização**: Dados da camada **Gold** são utilizados para criar **dashboards interativos no Superset**.  

---


### ⚙️Fluxograma de dados:

```bash

┌──────────────────────┐      ┌───────────────────────────────┐      ┌──────────────────────────────┐
│ 📥 Fonte de Dados:   │----->│ ➡️ Bloco Mage.ai (Python):   │----->│ ➡️ Bloco Mage.ai (DBT):      │
│     API Spotify      │      │     Ingestão Bronze           │      │     Testes Bronze            │
└──────────────────────┘      └───────────────────────────────┘      └─────────── Losango Laranja ──┘
                                         │ Salva JSON Bruto no S3 (Bronze) │              /    \
                                         └───────────────────────────────┘             ✅ OK   ❌ Falha
                                                │                                        │       └── Alerta/
                                                │                                        │            Interrupção
 ┌──────────────────────┐       ────────────────┌────────────────────────────────────────┐───────────┐
 │ ➡️ Camada Bronze     │----->│ ➡️ Bloco Mage.ai (Spark):    │----->│ ➡️ Bloco Mage.ai (DBT):      │
 │     (S3 - Raw)       │      │   Transformação Silver        │      │     Testes Silver            │
 └──────────────────────┘      └───────────────────────────────┘      └─────────── Losango Laranja ──┘
                                         │ Lê Bronze (S3), Limpa/Padroniza │              /    \
                                         │ Salva Parquet no S3 (Silver)    │             ✅ OK   ❌ Falha
                                         │  **(com Spark)**                │             │       └── Alerta/
                                         └─────────────────────────────────┘             │            Interrupção
                                                │                                        │
 ┌──────────────────────┐       ────────────────┌────────────────────────────────────────┐────────────────┐──────
 │ ➡️ Camada Silver     │----->│ ➡️ Bloco Mage.ai (DBT):      │----->│ ➡️ Camada Gold       │----->│ 📊 Superset:
 │     (S3 - Clean)     │      │   Transformação & Testes Gold │      │    (ClickHouse)      │      │ Dashboards
 └──────────────────────┘      └───────────────────────────────┘      └──────────────────────┘      └──────────────┘
                                         │ Lê Silver (S3), Modela (DBT)  │
                                         │ Salva Gold (ClickHouse/S3 opc)│
                                         │ + Testes Gold                 │
                                         └───────────────────────────────┘
                                                  Losango Laranja
                                                      /    \
                                                     ✅ OK   ❌ Falha
                                                              └── Alerta/
                                                                  Interrupção

```

## 🛠 Execução Local com Docker Compose  

### 📌 Pré-requisitos  
- **Docker** e **Docker Compose** instalados.  

### 📌 Passos  

1. **Clone o repositório**:  
   ```bash
   git clone [link-para-o-seu-repositorio]
   cd [nome-do-repositorio]


Configure as variáveis de ambiente (se necessário).

Execute o Docker Compose:

```bash

docker-compose up -d
```

### 📌Acesse as interfaces:

Mage.ai UI: http://localhost:6789
Superset UI: http://localhost:8088
Credenciais: admin/admin


📊 Explorando Dashboards no Superset
Acesse a UI do Superset.

Explore os dashboards pré-criados ou crie novos.
🚀 Próximos Passos e Melhorias Futuras
✅ Integração com Machine Learning.
✅ Suporte a dados em tempo real (Streaming).
✅ Adição de fontes de dados externas.
✅ Melhorias nos dashboards.
✅ Implementação de CI/CD para automação.
✅ Monitoramento avançado para análise de desempenho.


⚠️ Disclaimer
Este projeto é para fins educacionais e de demonstração. O uso da API do Spotify está sujeito aos termos de serviço e limitações de rate limiting.

📜 Licença
Este projeto pode ser distribuído sob a licença MIT (ou outra de sua escolha).

👨‍💻 Autor
Arthur Maia Graf 

🔗 GitHub
