Create Database Gestion_Ventas_Trigger
Use Gestion_Ventas_Trigger

Create Table Ventas(
Venta_ID INT PRIMARY KEY IDENTITY(1,1),
Cliente NVARCHAR(100),
Producto NVARCHAR(100),
Cantidad INT,
Fecha DATETIME DEFAULT GETDATE()
);

Create Table AuditoriaVentas(
Auditoria_ID INT PRIMARY KEY IDENTITY(1,1),
Venta_ID INT,
Accion NVARCHAR(10), -- UPDATE o DELETE
Fecha_Accion DATETIME DEFAULT GETDATE(),
Cliente NVARCHAR(100),
Producto NVARCHAR(100),
Cantidad INT);


CREATE or ALTER TRIGGER trg_AuditoriaVentas
ON Ventas
AFTER UPDATE, DELETE
AS
BEGIN
    -- Auditoría para actualizaciones
   IF EXISTS(SELECT * FROM deleted) AND NOT EXISTS(SELECT * FROM inserted)
    BEGIN
        INSERT INTO AuditoriaVentas (Venta_ID, Accion, Cliente, Producto, Cantidad)
        SELECT d.Venta_ID, 'DELETE', d.Cliente, d.Producto, d.Cantidad
        FROM deleted d;
    END

    -- Auditoría para actualizaciones
    IF EXISTS(SELECT * FROM inserted)
    BEGIN
        INSERT INTO AuditoriaVentas (Venta_ID, Accion, Cliente, Producto, Cantidad)
        SELECT i.Venta_ID, 'UPDATE', i.Cliente, i.Producto, i.Cantidad
        FROM inserted i;
    END
END;


Insert Into Ventas values('Jose Gutierrez','Fresas',50,GETDATE());



Select * From Ventas 
Select * From AuditoriaVentas


UPDATE Ventas
SET Cantidad = 85
WHERE Venta_ID = 3;

DELETE FROM Ventas
WHERE Venta_ID = 1;
