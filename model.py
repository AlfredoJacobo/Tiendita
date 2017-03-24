import web

db_host = 'localhost'
db_name = 'tienda' 
db_user = 'root'
db_pw   = ''

db = web.database(
			dbn='mysql',
			host=db_host,
			db=db_name,
			user=db_user,
			pw=db_pw
			)

def get_productos():
	try:
		return db.select('productos')
	except:
		return None

def get_producto(id_producto):
	try:
		return db.select('productos',where ='id_producto=$id_producto',vars = locals())
	except:
		return None

def new_producto(producto, descripcion, existencias, precio_compra, precio_venta,imagen_producto):
    db.insert('productos', producto=producto, descripcion=descripcion, existencias=existencias, precio_compra=precio_compra, precio_venta=precio_venta, imagen_producto=imagen_producto)

def update_producto(id_producto, producto, descripcion, existencias, precio_compra, precio_venta,):
    db.update('productos', where="id_producto=$id_producto", vars=locals(), producto=producto, descripcion=descripcion, existencias=existencias, precio_compra=precio_compra, precio_venta=precio_venta, imagen_producto=imagen_producto)

def delete_producto(id_producto):
    db.delete('productos', where="id_producto=$id_producto", vars=locals())