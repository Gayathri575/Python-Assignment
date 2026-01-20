import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import mysql.connector
import json


df = pd.read_csv("products.csv")  

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(df['product_name'])

vectors = tfidf_matrix.toarray().tolist()


conn = mysql.connector.connect(
    host="localhost",      
    user="root",           
    password="G@yuR@m05",   
    database="Product"    
)

cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS products_vectors (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(255),
    vector JSON
)
""")

for i, row in df.iterrows():
    product_id = row['product_id']
    product_name = row['product_name']
    vector_json = json.dumps(vectors[i])  
    cursor.execute("""
    INSERT INTO products_vectors (product_id, product_name, vector)
    VALUES (%s, %s, %s)
    """, (product_id, product_name, vector_json))

conn.commit()
cursor.close()
conn.close()

print(" stored in MySQL successfully!")
