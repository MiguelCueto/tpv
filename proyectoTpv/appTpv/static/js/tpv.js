var camarero="";
var lista_tickets="";
var factura_actual="";

$(document).ready(function(){
		
		$(".nombre").click(function(event) {
			$("#articulos").show();
			$(".linea").remove();
			$(".linea_ticket").remove();
			$("#ticket").hide();
			$("#total").hide();
			camarero=$(event.target).text()
			$("#camarero").html($(event.target).text());
			$.getJSON("tickets_abiertos/"+camarero, function( data ) {
				var tickets = [];
				lista_tickets=data;
			 	$.each(data, function(i, item) {
						if (tickets.indexOf(item.factura)==-1){
							tickets.push(item.factura);	
							$("<tr class='linea'><td>"+item.factura__fecha+"</td></tr>").appendTo( "#lista_tickets" );
							
						}
					
				});
				$(".linea").on('click',function(event) {
					$(".linea_ticket").remove();
					fecha=$(event.target).text();
					var total=0;
					$.each(lista_tickets, function(i, item) {
						if (item.factura__fecha==fecha){
							factura_actual=item.factura
							total=total+(item.cantidad)*(item.articulo__precio_unitario);
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

		$(".linea_articulo").click(function(event){ 
			id_articulo=$(event.target).next();	
			$.getJSON("meterMasArticulos/"+factura_actual+"/"+id_articulo.text(), function( data ) {
				$.each(data, function(i, item) {
						if (item.result=="OK"){
							alert("ok")
						}
						
				});
			});
		});



});//ready

   



