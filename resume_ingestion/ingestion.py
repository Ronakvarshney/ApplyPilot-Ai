from db.connection import get_connection
from uuid import uuid4
import psycopg
from resume_ingestion.pipeline import orchestration



def insert_resume(filename , filepath):
    conn = get_connection()
    print(filename , filepath)
    id = str(uuid4())
    print(conn)
    
    with conn.cursor() as cur: 
        cur.execute(
            """
            INSERT INTO resume
            (id, filename, filepath)
            VALUES (%s, %s, %s)
            """,
            (
                id,
                filename,
                filepath,
            ),
        )
        
    conn.commit()

    
    chunks , embeddings = orchestration(filepath)
    insert_resume_chunks(chunks , embeddings , resume_id = id)
    
        
    
    
def insert_resume_chunks(chunks , embeddings , resume_id):
    if chunks or embeddings:
        conn = get_connection()
        with conn.cursor() as cur:
           for i, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
            cur.execute(
                """
                INSERT INTO resume_chunks
                (
            id,
            resume_id,
            chunk_index,
            chunk_text,
            embedding
               )
               VALUES (%s, %s, %s, %s, %s)
                """,
               (
               str(uuid4()),
               resume_id,
               i,
               chunk.page_content,
               embedding,
            ),
        )
        conn.commit()
        conn.close()
      