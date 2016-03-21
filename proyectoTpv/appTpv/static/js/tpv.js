$(document).ready(function(){
		$(".nombre").click(function(event) {
			$("#camarero").html($(event.target).text());
			$("#ticket").hide();

	
	});
});

   



