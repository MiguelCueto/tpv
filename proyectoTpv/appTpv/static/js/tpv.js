var camarero="";
var lista_tickets="";

$(document).ready(function(){
		
		$(".nombre").click(function(event) {
			$(".linea").remove();
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
					fecha=$(event.target).text();
					$.each(lista_tickets, function(i, item) {
						if (item.factura__fecha==fecha){
							$("<tr class='linea_ticket'><td>"+item.articulo__nombre+"</td><td>"+item.cantidad+"</td></tr>").appendTo( "#lista_tabla" );
						}
					
					}); 
					$("#ticket").show();
				});
							  
			});
			

			$("#lista_tickets").show();
		});

		$(".celda").click(function(event){ 
			alert("hola");
			fecha=$(event.target).text();	
			$.each(lista_tickets, function(i, item) {
				if (tickets.indexOf(item.factura)==-1){
					tickets.push(item.factura);	
					$("<tr class='linea'><td class='celda'>"+item.factura__fecha+"</td></tr>").appendTo( "#lista_tickets" );
				}
					
				}); 
	
	
		});



});//ready

   



