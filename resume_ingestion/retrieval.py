import psycopg
from db.connection import get_connection

def get_resume():
    conn = get_connection()
    
    with conn.cursor() as cur:
        cur.execute("""
            SELECT id, filename, filepath
            FROM resume ORDER BY created_at DESC LIMIT 1""")
        resume = cur.fetchone()
        cur.close()
        print(resume)
        return resume
        
        
        
def fetch_chunks_and_embd(id):
   conn = get_connection()
   with conn.cursor() as cur:
       cur.execute("""
            SELECT chunk_index,
                   chunk_text,
                   embedding
            FROM resume_chunks
            WHERE resume_id = %s
            ORDER BY chunk_index
                   """, (id,),)
       details = cur.fetchall()
   conn.close()
   return details