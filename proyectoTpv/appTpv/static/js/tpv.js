var camarero="";
var lista_tickets="";

$(document).ready(function(){
		$(".nombre").click(function(event) {
			camarero=$(event.target).text()
			$("#camarero").html($(event.target).text());
			$.getJSON("tickets_abiertos/"+camarero, function( data ) {
				var tickets = [];
				lista_tickets=data;
			 	$.each(data, function(i, item) {
					
						if (tickets.indexOf(item.factura)==-1){
							tickets.push(item.factura);	
							$("<tr><td>"+item.factura__fecha+"</td></tr>").appendTo( "#lista_tickets" );
							
						}
					
				});
							  
			});


			$("#lista_tickets").show();
	});







});

   



