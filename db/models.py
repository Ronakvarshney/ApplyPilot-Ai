from connection import get_connection

CREATE_RESUME_TABLE = """
CREATE TABLE IF NOT EXISTS resume (
    id UUID PRIMARY KEY ,
    filename TEXT NOT NULL ,
    filepath TEXT NOT NULL ,
    created_at TIMESTAMP DEFAULT NOW()
);
"""

CREATE_RESUME_CHUNKS = """
CREATE TABLE IF NOT EXISTS resume_chunks (
    id UUID PRIMARY KEY,
    resume_id UUID REFERENCES resume(id),
    chunk_text TEXT,
    embedding VECTOR(768),
    chunk_index INT
);
"""



def create_tables():
    conn = get_connection()
    with conn.cursor() as cur:
        cur.execute(CREATE_RESUME_TABLE)
        cur.execute(CREATE_RESUME_CHUNKS)
    
    conn.commit()
    conn.close()


create_tables()