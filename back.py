from flask import Flask
import sqlite3 as lite


app = Flask(__name__)

@app.route("/cliente", methods=["POST"])
def cliente():
    return "inserir dados cliente"

con = lite.connect('quadra.db')


cur = con.cursor()


cur.execute("""
    select * from Quadra q 
    inner join Cliente c on q.id_cliente = c.id_cliente 
    inner join Horarios h on q.id_horario = h.id_horario 
    inner join Reserva r on q.id_reserva = r.id_reserva 
    """)
consulta = cur.fetchall()
print(consulta)