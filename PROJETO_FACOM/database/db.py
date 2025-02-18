import sqlite3
db = sqlite3.connect('C:/Users/Carlos Sales/Documents/CODE/PROJETO_FACOM/database/clientes.db')
cursor = db.cursor()

cursor.execute('SELECT * FROM tabela_clientes')
print(cursor.fetchall())