FROM apache/superset:latest

USER root
RUN pip install sqlalchemy-trino
RUN pip install psycopg2-binary

USER superset