$(function(){
	
	$("#analyze").click(function(){
		var link = document.getElementById("link").value;
		if (link==""){
			alert("Please provide a link to a spreadsheet before clicking analyze");
		}else {

			$.ajax({
				type:"GET",
				url:"/analyze"+link,
				dataType:"text",
				success:analyzeSuccess,
				failure:analyzeFailure
			});
		}
		function analyzeSuccess(){
			/*
				Update html with various statistical data
			*/
			 $(body).append("<table class='table table-striped'></table>")

		}

		function analyzeFailure(xhr){
			console.log(xhr);
		}
	});
});