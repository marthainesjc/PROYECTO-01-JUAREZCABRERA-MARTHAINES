from lifestore_file import lifestore_products
from lifestore_file import lifestore_sales
from lifestore_file import lifestore_searches


usuarios=[["jorge","123"],["juan","345"],["misael","789"]]
#usuarios=[administrador (minusculas),contraseña (numeros)]
i=0
j=0
while i==0 and j<3:
  nombre=input("Nombre de usuario\n")
  contraseña=input("Contraseña\n")
  if [nombre,contraseña] in usuarios:
      i=1
    
  if i==0:
    print("nombre de usuario o cotraseña incorrecto\n\n")
    j+=1

if i==0:
  print("Número de intentos excedidos")
  exit("El programa ha terminado")

##este proceso nos da acceso al programa, verifica que el usuario y la contraseña sean correctas. Da 3 intentos para iniciar sesión. 

"""Quiero contar la cantidad de productos"""
total_de_productos=0

for producto in lifestore_products:
    total_de_productos+=1

"""Generar listado de productos con 15 mayores ventas"""

total_de_ventas=0

for venta in lifestore_sales:
    total_de_ventas+=1

id_product_and_sale= [] ##[numero de ventas, nombre, categoría]

for number in range(1,total_de_productos+1):
    cuenta_number=0
    for indice in range(total_de_ventas):
        if int(lifestore_sales[indice][1])==number:
            cuenta_number+=1
    id_product_and_sale.append([cuenta_number,lifestore_products[number-1][1],lifestore_products[number-1][3],])

##Del total de productos, cuento las ventas que tuvo cada uno de ellos y las guardo en una lista, agregandole la categoria del producto


"""Ordenar lista id_product_and_sale de mayor a menor"""

id_product_and_sale_ordenado=sorted(id_product_and_sale,reverse=True) 

"""Generar listado de busqueda de los productos"""

total_de_busquedas=0

for busqueda in lifestore_searches:
    total_de_busquedas+=1


id_product_and_search= [] #[#de busquedas,nombre,categoria]

for busqueda in range(1,total_de_productos+1):
    cuenta_busqueda=0
    for indice in range(total_de_busquedas):
        if int(lifestore_searches[indice][1])==busqueda:
            cuenta_busqueda+=1
    id_product_and_search.append([cuenta_busqueda,lifestore_products[busqueda-1][1],lifestore_products[busqueda-1][3]])

##Del total de productos, cuento las busquedas de cada uno de ellos y lo guardo en una lista, agregandole la categoria del producto

"""Ahora quiero ordenar mi lista id_product_and_sale de mayor a menor"""

id_product_and_search_ordenado=sorted(id_product_and_search,reverse=True)


"""Quiero separar por categoria"""
##Tengo que hacer categoria y ventas/ categoría y búsqueda

procesadores_sale=[] # [#de ventas del procesador, nombre del producto(procesador)]
procesadores_search=[]# [#de busquedas del procesador, nombre del producto(procesador)]

tarjetasvideo_sale=[]# [#de ventas de tarjetas de video, nombre del producto(tarjeta de video)]
tarjetasvideo_search=[] # [#de busquedas de tarjetas de video, nombre del producto(tarjeta de video)]

tarjetasmadre_sale=[]
tarjetasmadre_search=[]

discosduros_sale=[]
discosduros_search=[]

memoriasusb_sale=[]
memoriasusb_search=[]

pantallas_sale=[]
pantallas_search=[]

bocinas_sale=[]
bocinas_search=[]

audifonos_sale=[]
audifonos_search=[]


for i in range(total_de_productos):

 if id_product_and_sale[i][2]=="tarjetas madre":
    tarjetasmadre_sale.append(id_product_and_sale[i][0:2])
    tarjetasmadre_search.append(id_product_and_search[i][0:2])
 
 if id_product_and_sale[i][2]=="discos duros":
    discosduros_sale.append(id_product_and_sale[i][0:2])
    discosduros_search.append(id_product_and_search[i][0:2])

 if id_product_and_sale[i][2]=="memorias usb":
    memoriasusb_sale.append(id_product_and_sale[i][0:2])
    memoriasusb_search.append(id_product_and_search[i][0:2])

 if id_product_and_sale[i][2]=="pantallas":
    pantallas_sale.append(id_product_and_sale[i][0:2])
    pantallas_search.append(id_product_and_search[i][0:2])

 if id_product_and_sale[i][2]=="bocinas":
    bocinas_sale.append(id_product_and_sale[i][0:2])
    bocinas_search.append(id_product_and_search[i][0:2])

 if id_product_and_sale[i][2]=="audifonos":
    audifonos_sale.append(id_product_and_sale[i][0:2])
    audifonos_search.append(id_product_and_search[i][0:2])

 if id_product_and_sale[i][2]=="tarjetas de video":
    tarjetasvideo_sale.append(id_product_and_sale[i])
    tarjetasvideo_search.append(id_product_and_search[i][0:2])

 if id_product_and_sale[i][2]=="procesadores":
    procesadores_sale.append(id_product_and_sale[i][0:2])
    procesadores_search.append(id_product_and_search[i][0:2])

##De la lista id_product_and_sale, separo los datos del numero de ventas por categorías y las guardo en listas nuevas que estan nombradas dependiendo de las categorías.

##Tambien, de la lista de id_product_and_search, separo los datos de los numeros de busqueda por categorías y los guardo en listas nuevas que estan nombradas dependiendo de las categorías

procesadores_sale.sort()
procesadores_search.sort()

tarjetasvideo_sale.sort()
tarjetasvideo_search.sort()

tarjetasmadre_sale.sort()
tarjetasmadre_search.sort()

discosduros_sale.sort()
discosduros_search.sort()

memoriasusb_sale.sort()
memoriasusb_search.sort()

pantallas_sale.sort()
pantallas_search.sort()

bocinas_sale.sort()
bocinas_search.sort()

audifonos_sale.sort()
audifonos_search.sort()

"""Tengo que mostrar dos listas en donde muestre las mejores reseñas y peores reseñas considerando productos e devolucion """

lista_score=[] #[promedio de puntuacion de reseñas, nombre del producto, devoluciones]
lista_not_score=[] #[0 reseñas (0 ventas), nombre del producto]

for indice in range(1,total_de_productos+1):
    cuenta_score=0
    suma_score=0
    cuenta_refund=0
    for numero in range(total_de_ventas):
        if lifestore_sales[numero][1]==indice:
            cuenta_score+=1
            suma_score+= lifestore_sales[numero][2]
        if lifestore_sales[numero][4]==1 and lifestore_sales[numero][1]==indice :
            cuenta_refund+=1
    if cuenta_score !=0:
        lista_score.append([suma_score/cuenta_score,lifestore_products[indice-1][1],cuenta_refund])
    else:
        lista_not_score.append([lifestore_products[indice-1][1], "No se vendió"])

##Considerando el total de productos y el numero de ventas, me fijo en las reseñas de cada producto, las sumo y las promedio y las guardo en una lista considerando también si el producto se devolvió o no. Si un producto no se vendió, lo guardo en una lista que considera los productos no vendidos  

lista_score.sort(reverse=True)

"""Consideremos las fechas"""

lista_fechas=[] #[aqui guardo todas las fechas de la lista lifestore_sales]

for fecha in lifestore_sales:
    lista_fechas.append(fecha[3])

##Guarde todas las fechas de la lista lifestore_sales

lista_ventas_mes=[] #[id product, mes (1,..12), precio]

#MESES: 1-enero, 2-febrero, 3-marzo,..., 11-noviembre, 12-diciembre

for j in range(1,10):
  for i in range(total_de_ventas):
    if j==int(lista_fechas[i][4:5]):
      id_product= int(lifestore_sales[i][1])-1
      lista_ventas_mes.append([lifestore_sales[i][1],int(lista_fechas[i][4:5]), lifestore_products[id_product][2]])

for j in range(10,13):
  for i in range(total_de_ventas):
    if j==int(lista_fechas[i][3:5]):
      id_producto=int(lifestore_sales[i][1])-1
      lista_ventas_mes.append([lifestore_sales[i][1],int(lista_fechas[i][3:5]),lifestore_products[id_producto][2]])

# A partir de los 12 meses del año, consideré los productos que se vendieron por mes y el precio de venta del producto


"""total de ventas (en cantidad) de cada producto al mes"""

venta_producto=[] #[mes,cantidad de productos vendidos al mes]
promedio_mensual=[] #[mes, promedio mensual]

for i in range(1,13):
 count_sale=0
 suma=0
 for venta in lista_ventas_mes:
   if i==venta[1]:
     count_sale+=1
     suma+=venta[2]
 if count_sale != 0:
    promedio_mensual.append([i, suma/count_sale])
    venta_producto.append([count_sale,i])
 if count_sale == 0:
   promedio_mensual.append([i, 0])

##Por mes, conté la cantidad de productos que se vendieron en ese mes y sumé los precios de los productos para promediarlos

venta_producto.sort(reverse=True)

"""Ventas totales"""
suma_total=0
for venta in lista_ventas_mes:
  suma_total+=venta[2]

##Sume todas las ventas de todos los meses



######################## MENU ##############################


print("Bienvenido al menú de LifeStore. \n Selecciona una opción del siguiente menú \n ")
print("          MENU \n")

print(" 1-Listado con los 15 productos con mayor venta \n 2-Listado con los 15 productos con mayor búsqueda \n 3-Por categoría, generar un listado con los 5 productos menos vendidos \n 4-Por categoría, generar un listado con los 10 productos con menor búsquedas \n 5-Listado con los 15 productos con las mejores reseñas \n 6-Listado con los 7 productos con peores reseñas \n 7-Productos no vendidos \n 8-Productos con devolución \n 9-Ventas promedio mensuales \n 10-Meses con más ventas al año \n 11-Venta total anual \n")

opcion=int(input("Selecciona la opción \n"))

if opcion==1:
  print("[numero de ventas, nombre del producto] \n")
  for venta in id_product_and_sale_ordenado[0:15]:
   print(venta[0:2],"\n")

if opcion==2:
  print("[numero de búsquedas, nombre del producto] \n")
  for busqueda in id_product_and_search_ordenado[0:15]:
   print(busqueda[0:2],"\n")

if opcion==3:
  categoria=int(input(" Elige la categoría: \n 1-Audifonos\n 2-Bocinas\n 3-Discos duros\n 4-Memorias usb\n 5-Pantallas\n 6-Procesadores\n 7-Tarjetas de video\n 8-Tarjetas madre \n"))
  if categoria==1:
   for venta in audifonos_sale[0:5]:
     print("El producto:",venta[1], "se vendió",venta[0],"veces \n")
  if categoria==2:
   for venta in bocinas_sale[0:5]:
    print("El producto:",venta[1], "se vendió",venta[0],"veces \n")
  if categoria==3:
   for venta in discosduros_sale[0:5]:
     print("El producto:",venta[1], "se vendió",venta[0],"veces \n")
  if categoria==4:
   for venta in memoriasusb_sale:
     print("El producto:",venta[1], "se vendió",venta[0],"veces \n")
  if categoria==5:
   for venta in pantallas_sale[0:5]:
     print("El producto:",venta[1], "se vendió",venta[0],"veces \n")
  if categoria==6:
   for venta in procesadores_sale[0:5]:
     print("El producto:",venta[1], "se vendió",venta[0],"veces \n")
  if categoria==7:
   for venta in tarjetasvideo_sale[0:5]:
     print("El producto:",venta[1], "se vendió",venta[0],"veces \n")
  if categoria==8:
   for venta in tarjetasmadre_sale[0:5]:
     print("El producto:",venta[1], "se vendió",venta[0],"veces \n")



if opcion==4:
 category=int(input(" Elige la categoría: \n 1-Audifonos\n 2-Bocinas\n 3-Discos duros\n 4-Memorias usb\n 5-Pantallas\n 6-Procesadores\n 7-Tarjetas de video\n 8-Tarjetas madre \n"))
 if category==1:
  for busqueda in audifonos_search[0:10]:
    print("El producto:",busqueda[1], "se buscó", busqueda[0], "veces \n")
 if category==2:
  for busqueda in bocinas_search[0:10]:
    print("El producto:",busqueda[1], "se buscó", busqueda[0], "veces \n")
 if category==3:
  for busqueda in discosduros_search[0:10]:
    print("El producto:",busqueda[1], "se buscó", busqueda[0], "veces \n")
 if category==4:
   for busqueda in memoriasusb_search:
     print("El producto:",busqueda[1], "se buscó", busqueda[0], "veces \n")
 if category==5:
   for busqueda in pantallas_search[0:10]:
     print("El producto:",busqueda[1], "se buscó", busqueda[0], "veces \n")
 if category==6:
   for busqueda in procesadores_search[0:10]:
     print("El producto:",busqueda[1], "se buscó", busqueda[0], "veces \n")
 if category==7:
   for busqueda in tarjetasvideo_search[0:10]:
     print("El producto:",busqueda[1], "se buscó", busqueda[0], "veces \n")
 if category==8:
   for busqueda in tarjetasmadre_search[0:10]:
     print("El producto:",busqueda[1], "se buscó", busqueda[0], "veces \n")


if opcion==5:
  print("[promedio puntuacion de reseñas, nombre del producto, devoluciones]")
  for resena in lista_score[0:15]:
    print(resena, "\n")

if opcion==6:
  print("[promedio puntuacion de reseñas, nombre del producto, devoluciones] \n")
  lista_score.sort()
  for resena in lista_score[0:8]:
    print(resena, "\n")

if opcion==7:
  for novendido in lista_not_score:
    print(novendido, "\n")

if opcion==8:
  print("[promedio puntuacion de reseñas, nombre del producto, devoluciones] \n")
  for producto in lista_score:
   if producto[2]==1:
     print(producto, "\n")

if opcion==9:
  print("[mes,promedio mensual] \n")
  print("1-Enero, 2-Febrero,..., 11-Noviembre, 12-Diciembre \n")
  for venta in promedio_mensual:
    print(venta, "\n")

if opcion==10:
  print("[mes, cantidad de productos vendidos] \n")
  print("1-Enero, 2-Febrero,..., 11-Noviembre, 12-Diciembre \n")
  for mes in venta_producto[0:4]:
    print(mes, "\n")

if opcion==11:
  print(suma_total)
