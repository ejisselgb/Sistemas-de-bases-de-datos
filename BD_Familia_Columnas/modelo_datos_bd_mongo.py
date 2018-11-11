db.twitter.insert({"nombre_usuario": "ejisselgb", "nombre": "Erika Gutierrez", "tipo_perfil": "pub", "estado": "A", "fecha_registro": "12/05/2017", "seguidores": [{"id_usuario":"", "estado_seguidor": "", "fecha_seguidor": ""}], "seguidos": [{"id_usuario": "", "estado_seguido": "", "fecha_seguir": ""}], "ciudad": [{"nombre_ciudad": "Cali", "pais": "Colombia"}], "tweets": [{"id_message": "mes1", "texto": "Hoy es un dia muy lluvioso, no deberiamos salir", "fecha_emision": "25/06/2017", "tipo": "Nr", "hashtag": ["#diaLluvioso", "#diaTriste"], "destinatario": ""}, {"id_message": "mes2", "texto": "Feliz de compartir con mis amigos este dia tan importante", "fecha_emision": "24/08/2017", "tipo": "Nr", "hashtag": ["#felizJueves", "#diaDeAmigos"], "destinatario": ""}]})


db.twitter.insert({"nombre_usuario": "stephagube", "nombre": "Stephania Gutierrez", "tipo_perfil": "pri", "estado": "A", "fecha_registro": "18/02/2018", "seguidores": [{"id_usuario":"ejisselgb", "estado_seguidor": "A", "fecha_seguidor": "20/04/2018"}], "seguidos": [{"id_usuario": "ejisselgb", "estado_seguido": "A", "fecha_seguir": "22/04/2018"}], "ciudad": [{"nombre_ciudad": "Cali", "pais": "Colombia"}], "tweets": [{"id_message": "mes1", "texto": "Inicie mi cuenta en twitter, este es mi primer mensaje", "fecha_emision": "18/02/2018", "tipo": "Nr", "hashtag": ["#tengoCuentaEnTwitter"], "destinatario": ""}, {"id_message": "mes2", "texto": "Hola, sigueme en twitter", "fecha_emision": "19/04/2018", "tipo": "Dr", "hashtag": [], "destinatario": "ejisselgb"}, {"id_message": "mes3", "texto": "Hola, sigueme en twitter", "fecha_emision": "20/05/2018", "tipo": "Dr", "hashtag": [], "destinatario": "manuelvs10"}]})

db.twitter.insert({"nombre_usuario": "manuelvs10", "nombre": "Manuel Vasquez", "tipo_perfil": "pri", "estado": "A", "fecha_registro": "30/07/2015", "seguidores": [{"id_usuario":"ejisselgb", "estado_seguidor": "A", "fecha_seguidor": "13/05/2017"}, {"id_usuario":"stephagube", "estado_seguidor": "A", "fecha_seguidor": "20/02/2018"}], "seguidos": [{"id_usuario": "ejisselgb", "estado_seguido": "A", "fecha_seguir": "21/12/2017"}], "ciudad": [{"nombre_ciudad": "Medellin", "pais": "Colombia"}], "tweets": [{"id_message": "mes1", "texto": "Ingresando al mundo de twitter, vamos a ver como me trata", "fecha_emision": "30/07/2015", "tipo": "Nr", "hashtag": ["#tengoCuentaEnTwitter"], "destinatario": ""}, {"id_message": "mes2", "texto": "Listo para irme al trabajo, feliz miercoles", "fecha_emision": "05/08/2015", "tipo": "Nr", "hashtag": ["#work", "#wednesday", "#goToWork"], "destinatario": ""}, {"id_message": "mes3", "texto": "Me fui a recorrer el mundo, nos vemos en dos semanas", "fecha_emision": "08/12/2015", "tipo": "Nr", "hashtag": ["#travelInTheWorld", "#Europe", "#Vacaciones"], "destinatario": ""}, {"id_message": "mes4", "texto": "Feliz anio nuevo para todos", "fecha_emision": "01/01/2016", "tipo": "Nr", "hashtag": ["#HappyNewYear"], "destinatario": ""}, {"id_message": "mes5", "texto": "Bienvenida a twitter, ya te estabamos esperando", "fecha_emision": "21/12/2017", "tipo": "Dr", "hashtag": [], "destinatario": "ejisselgb"}]})


db.twitter.insert({"nombre_usuario": "jhoncito", "nombre": "Jhon Gomez", "tipo_perfil": "pub", "estado": "A", "fecha_registro": "15/03/2016", "seguidores": [{"id_usuario":"ejisselgb", "estado_seguidor": "A", "fecha_seguidor": "13/05/2017"}, {"id_usuario":"stephagube", "estado_seguidor": "A", "fecha_seguidor": "20/02/2018"}, {"id_usuario":"manuelvs10", "estado_seguidor": "A", "fecha_seguidor": "20/03/2016"}], "seguidos": [{"id_usuario": "ejisselgb", "estado_seguido": "A", "fecha_seguir": "21/12/2017"}, {"id_usuario": "manuelvs10", "estado_seguido": "A", "fecha_seguir": "21/03/2016"}], "ciudad": [{"nombre_ciudad": "Medellin", "pais": "Colombia"}], "tweets": [{"id_message": "mes1", "texto": "Ingresando a twitter para leer noticias, sigueme y te sigo", "fecha_emision": "15/04/2016", "tipo": "Nr", "hashtag": ["#DescubriendoTwitter", "#tengoCuentaEnTwitter"], "destinatario": ""}, {"id_message": "mes2", "texto": "Por muy dificil que sea, valdra la pena", "fecha_emision": "25/11/2016", "tipo": "Nr", "hashtag": ["#luchas", "#valdraLaPena"], "destinatario": ""}]}) 


db.twitter.insert({"nombre_usuario": "EdwinLeon", "nombre": "Edwind Leon", "tipo_perfil": "pri", "estado": "A", "fecha_registro": "09/09/2015", "seguidores": [{"id_usuario":"manuelvs10", "estado_seguidor": "A", "fecha_seguidor": "15/09/2015"}, {"id_usuario":"jhoncito", "estado_seguidor": "A", "fecha_seguidor": "24/06/2016"}], "seguidos": [{"id_usuario": "stephagube", "estado_seguido": "A", "fecha_seguir": "21/06/2018"}], "ciudad": [{"nombre_ciudad": "Popayan", "pais": "Colombia"}], "tweets": [{"id_message": "mes1", "texto": "Bienvenidos al twitter de Edwin Leon", "fecha_emision": "13/09/2015", "tipo": "Nr", "hashtag": ["#tengoCuentaEnTwitter"], "destinatario": ""}]}) 


db.twitter.aggregate( [
   { $group: { _id: "$seguidores.id_usuario", myCount: { $sum: 1 } } }
] )


db.twitter.find({ tweets: { $elemMatch: { "ciudad.nombre_ciudad": "Cali" }}})


db.twitter.aggregate(
   [
      {
         $project: {
            item: 1,
            numberOfColors: { $size: "$colors" }
         }
      }
   ]
)

db.twitter.aggregate([
   {
      $project: {
         seguidores: {
            $filter: {
               input: "$seguidores.id_usuario",
               cond: { myCount: { $sum: 0 }}}
            },
        numero_seguidores: { $size: "$seguidores" }
       }
   }
])





db.twitter.aggregate( [
   { $group: { _id: "$seguidores.id_usuario", myCount: { $sum: 1 } } }
] )