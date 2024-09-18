from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Ventas(db.Model):
    __tablename__ = 'Ventas'
    Venta_ID = db.Column(db.Integer, primary_key=True)
    Cliente = db.Column(db.String(100), nullable=False)
    Producto = db.Column(db.String(200), nullable=False)
    Cantidad = db.Column(db.Integer, nullable=False)
    Fecha = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class AuditoriaVentas(db.Model):
    __tablename__ = 'AuditoriaVentas'
    Auditoria_ID = db.Column(db.Integer, primary_key=True)
    Venta_ID = db.Column(db.Integer, nullable=False)
    Accion = db.Column(db.String(20), nullable=False)  
    Fecha_Accion = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    Cliente = db.Column(db.String(100), nullable=False)
    Producto = db.Column(db.String(100), nullable=False)
    Cantidad = db.Column(db.Integer, nullable=False)