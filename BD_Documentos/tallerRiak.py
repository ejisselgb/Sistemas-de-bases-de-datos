
from datetime import datetime
from riak import RiakClient, RiakNode
client = RiakClient()
myBucket = client.bucket('taller_bd01_Erika')


def ordenarFechas(nombre_usuario):
        max = 0
        arrayFecha = []
	arrayFechaSort = []
	dataResultArray = []

        for key in myBucket.get_keys():
                obj =  myBucket.get(key)
                for value in obj.data:
                        if obj.key == nombre_usuario and value == "tweets":
                                for i in xrange(0,len(obj.data[value])):
                                        fecha_str = str(obj.data[value][i]['fecha_emision'])
                                        date_object = datetime.strptime(fecha_str, '%d/%m/%Y')
                                        order_fecha= date_object.strftime("%Y/%m/%d")
					date_object_order = datetime.strptime(order_fecha, '%Y/%m/%d')

                                        arrayFecha.append(date_object_order)
					array_sort = sorted(arrayFecha)
					arrayFechaSort = list(reversed(array_sort))
				count = len(obj.data[value]) - 1
				for j in arrayFechaSort:
					dataResult = {}
					dataResult['fecha'] = j
					dataResult['mensaje'] = obj.data[value][count]['texto']
					if obj.data[value][count]['tipo'] == "Dr":
						dataResult['tipo'] = obj.data[value][count]['tipo']
						dataResult['destinatario'] = obj.data[value][count]['destinatario']
					dataResultArray.append(dataResult)
					count = count - 1
        return dataResultArray

def mensajesRecibidos(usuario):

	inbox = []
	for key in myBucket.get_keys():
		obj = myBucket.get(key)
		for value in obj.data:
			if value == "tweets":
				for i in xrange(0,len(obj.data[value])):
					if obj.data[value][i]['destinatario'] == usuario:
						arrayMessage = {}
						arrayMessage['fecha_emision'] = obj.data[value][i]['fecha_emision']
						arrayMessage['mensaje_recibido'] = obj.data[value][i]['texto']
						arrayMessage['ciudad'] = obj.data['ciudad'][0]['nombre_ciudad']
						inbox.append(arrayMessage)

	return inbox

def ultimosMensajes():


	arrayMessage = []
	for key in myBucket.get_keys():
		obj = myBucket.get(key)
		for value in obj.data:
			if value == "tweets":
				if len(arrayMessage) < 5:
					for i in xrange(0,len(obj.data[value])):
						valueObj = {}
                                		valueObj['mensaje'] = obj.data[value][i]['texto']
                                		valueObj['fecha'] = obj.data[value][i]['fecha_emision']
						arrayMessage.append(valueObj)

	return arrayMessage



print "\n"
print "Mis mensajes enviados "
print  ordenarFechas('manuelvs10')
print "\n"
print "Mis mensajes recibidos "
print  mensajesRecibidos('manuelvs10')
print "\n"
print "Ultimas publicaciones"
print ultimosMensajes()
