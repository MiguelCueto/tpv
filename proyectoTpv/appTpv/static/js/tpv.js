var camarero=""; //gurda el camarero seleccionado actual
var lista_tickets=""; //guarda todos los tickets abiertos del camarero actual, junto con sus articulos de cada ticket en JSON
var factura_actual=""; //guarda el id de la factura que vemos en la tabla

$(document).ready(function(){
		
		$(".nombre").click(function(event) { //cuando haga click en el nombre del camarero que me muestre sus tickets abiertos
			$("#articulos").show();
			$(".linea").remove();
			$(".linea_ticket").remove();
			$("#ticket").hide();
			$("#total").hide();
			camarero=$(event.target).text() //dentro del td con clase nombre sacame el texto que contenga y guardamelo el nombre en la variable
			$("#camarero").html($(event.target).text());//te saca el nombre del camarero
			$.getJSON("tickets_abiertos/"+camarero, function( data ) { //pedimos a la base de datos los tickets del camarero y nos lo baja en JSON, y esto se hace con AJAX, que te baja solo los dato que pides no toda la pagina
				var tickets = []; //es un array para recorrer los tickets
				lista_tickets=data; //esta variable es para guardar todo lo que bajamos del servidor
			 	$.each(data, function(i, item) {  //recorremos todos los tickets con un for
						if (tickets.indexOf(item.factura)==-1){ //miramos si es diferente que lo meta
							tickets.push(item.factura);	
							$("<tr class='linea'><td>"+item.factura__fecha+"</td></tr>").appendTo( "#lista_tickets" );
							
						}
					
				});
				$(".linea").on('click',function(event) {//cuando haga click en la fecha que me muestra lo que tiene de articulos
					$(".linea_ticket").remove(); //borro la tabla para meter la nueva
					fecha=$(event.target).text(); //esto es la manera de identificar el ticket
					var total=0; //aquig guardamos el total
					$.each(lista_tickets, function(i, item) { //recorremos los tickets
						if (item.factura__fecha==fecha){ //para seleccionar factura comparamos con las fechas
							factura_actual=item.factura //si es la factura que buscamos la guardamos en la variable globarl
							total=total+(item.cantidad)*(item.articulo__precio_unitario); //aqui calculamos el total del ticket
							$("<tr class='linea_ticket'><td>"+item.articulo__nombre+"</td><td>"+item.cantidad+"</td><td>"+item.articulo__precio_unitario+"</td><td>"+(item.cantidad)*(item.articulo__precio_unitario)+"</td></tr>").appendTo( "#lista_tabla" );
						}
						
					}); 
					$("#total").html(total);
					$("#ticket").show();
					$("#total").show();
				});
							  
			});
			

			$("#lista_tickets").show();
		});

		$(".linea_articulo").click(function(event){ //es para añadir articulos al ticket al hacer click en la lista articulos
			id_articulo=$(event.target).next();	//es para que nos coja el articulo siguiente de la lista que es el id
			$.getJSON("meterMasArticulos/"+factura_actual+"/"+id_articulo.text(), function( data ) { //pa añadir el articulo a la factura
				$.each(data, function(i, item) { //el data es lo que devuelve el servidor si consiguio guardar
						if (item=="OK"){  //si devuelve OK es que guardo y a continuacion vamos a actualizar la pagina
							$.getJSON("tickets_abiertos/"+camarero, function( data ) { //pedimos los tickets del camarero otra vez, ahora ya modificados con lo nuevo que metimos
								lista_tickets=data;
								$(".linea_ticket").remove();// borramos otra vez las lineas
								$.each(data, function(i, item) { // y recorremos otra vez los que bajamos //cada linea es un item
									if (item.factura==factura_actual){ //si la factura que recorremos es igual a la factura actual (que eso lo miramos con el id que guradamos al hacer click) entonces lo metemos
										$("<tr class='linea_ticket'><td>"+item.articulo__nombre+"</td><td>"+item.cantidad+"</td><td>"+item.articulo__precio_unitario+"</td><td>"+(item.cantidad)*(item.articulo__precio_unitario)+"</td></tr>").appendTo("#lista_tabla");	
									}
								});
	   						});
						}
						
				});
			});


			
		});



});//ready

   



