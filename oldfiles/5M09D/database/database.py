import sqlite3

conn = sqlite3.connect("test.db")
cur = conn.cursor()

data = (
    ('홍진우', 1, '서울'),
    ('강지수', 2, '부산'),
    ('김청진', 1, '서울'),
)
sql = "insert into customer(name,category,region) values (?, ?, ?)"
cur.executemany(sql, data)

conn.commit()
conn.close()