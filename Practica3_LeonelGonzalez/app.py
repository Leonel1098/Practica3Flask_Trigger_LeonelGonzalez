from flask import Flask, flash, render_template, request, redirect,url_for
from models import db, Ventas,AuditoriaVentas
from config import Config
from datetime import datetime

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ventas", methods = ["GET","POST"])
def crear_Venta():
    if request.method == 'POST':
        # Crear nueva Venta
        new_Venta = Ventas(
            Cliente=request.form['Cliente'],
            Producto=request.form['Producto'],
            Cantidad=request.form['Cantidad'],
            Fecha=request.form['Fecha'],
        )
        db.session.add(new_Venta)
        db.session.commit()
        return redirect(url_for('listar_Ventas'))
    
    ventas = Ventas.query.all()
    return render_template('Ventas.html', ventas = ventas)

@app.route("/ventas/lista")
def listar_Ventas():
    Cliente = request.args.get('Cliente')
    Producto = request.args.get("Producto")

    query = Ventas.query

    if Cliente:
        query = query.filter(Ventas.Cliente.ilike(f'%{Cliente}%'))
    if Producto:
        query = query.filter(Ventas.Producto.ilike(f'%{Producto}%'))
    
    ventas = query.all()
    return render_template('Lista_Ventas.html', ventas = ventas)

#Actualizar Ventas
@app.route('/ventas/actualizar/<int:Venta_ID>', methods=['GET', 'POST'])
def actualizar_Ventas(Venta_ID):
    venta = Ventas.query.get_or_404(Venta_ID)

    if request.method == 'POST':
        venta.Cliente = request.form.get('Cliente', venta.Cliente)
        venta.Producto = request.form.get('Producto', venta.Producto)
        venta.Cantidad = request.form.get('Cantidad', venta.Cantidad)
        venta.Fecha = request.form.get('Fecha', venta.Fecha)

        try:
            db.session.commit()
            flash('Venta actualizada exitosamente.', 'success')
        except Exception as e:
            db.session.rollback()
            flash(f'Error al actualizar venta: {e}', 'error')
        
        return redirect(url_for('listar_Ventas'))

    return render_template('Actualizar_Ventas.html', venta=venta)

#Metodo para Eliminar Clientes
@app.route('/ventas/eliminar/<int:Venta_ID>', methods=['POST'])
def eliminar_Venta(Venta_ID):
    venta = Ventas.query.get_or_404(Venta_ID)
    db.session.delete(venta)
    db.session.commit()
    return redirect(url_for('listar_Ventas'))


#Listado de Auditoria 

@app.route("/auditoria")
def listar_Auditoria():
    Cliente = request.args.get('Cliente')
    Producto = request.args.get("Producto")
    
    print(f"Cliente: {Cliente}, Producto: {Producto}") 
    query = AuditoriaVentas.query

    if Cliente:
        query = query.filter(AuditoriaVentas.Cliente.ilike(f'%{Cliente}%'))
    if Producto:
        query = query.filter(AuditoriaVentas.Producto.ilike(f'%{Producto}%'))
    
    auditorias = query.all()
    print(auditorias)
    return render_template('Lista_Auditoria.html', auditorias = auditorias)


if __name__ == '__main__':
    app.run(debug=True) 