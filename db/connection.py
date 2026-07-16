import psycopg
from pgvector.psycopg import register_vector


def get_connection():
    conn =  psycopg.connect("host=localhost port=5432 dbname=applypilot user=postgres password=postgres")
    register_vector(conn)
    return conn 