$(function(){

	var app = new Object();

	$("#homebtn").click(function(){

		//alert("home");
		loadDocuments();

	});

	$("#btn-tokenize").click(function(){

		buttonReference = $(this);
		buttonReference.button('loading');

		function loadTokenizedData(text){
			$("#tokenized-text-area").html("")
			$("#tokenized-text-area").html(text);

			buttonReference.button('reset');
		}

		function failedTokenizedData(xhr){
			console.log(xhr);
		}


		$.ajax({
			type:"POST",
			url:"/tokenizeData",
			data:{"text":app.currentDocument},
			success:loadTokenizedData,
			failure:failedTokenizedData
		});
	});

	$("#btn-pos").click(function(){

		buttonReference = $(this);
		buttonReference.button('loading');

		function loadPosTags(tags){
			$("#POS-text-area").html("");
			$("#POS-text-area").html(tags);

			buttonReference.button('reset');
		}

			function failedPosTags(xhr){
			console.log(xhr);
		}

		$.ajax({
			type:"GET",
			url:"/postags",
			success:loadPosTags,
			failure:failedPosTags
		});

	});

	$("#btn-chunk").click(function(){

		buttonReference = $(this);
		buttonReference.button('loading');


		function loadChunkedData(chunks){
			$("#chunked-text-area").html("");
			$("#chunked-text-area").html(chunks);
			buttonReference.button('reset');
		}

		function failedChunking(xhr){
			console.log(xhr);
		}

		$.ajax({
			type:"GET",
			url:"/chunk",
			success:loadChunkedData,
			failure:failedChunking

		});

	});

	$("#btn-entity").click(function(){

		buttonReference = $(this);
		buttonReference.button('loading');

		function loadEntities(entities){
			$("#entity-text-area").html("");
			$("#entity-text-area").html(entities);
			buttonReference.button('reset');

		}

		function failedEntities(xhr){
			console.log(xhr);
		}

		$.ajax({
			type:"GET",
			url:"/entities",
			success:loadEntities,
			failure:failedEntities

		});

	});

	$("#btn-tf").click(function(){

		buttonReference = $(this);
		buttonReference.button('loading');

		function loadTF(TF){
			$("#frequency-value").html("");
			buttonReference.button('reset');
			$.each(TF,function(key,value){
				$("#table-tf").append("<tr class=\"frequency-value\"><td>"+value[0]+"</td><td>"+value[1]+"</td></tr>");
			});

		}

		function failedTF(xhr){
			console.log(xhr);
		}

		$.ajax({
			type:"POST",
			url:"/tfidf",
			data:{"text":app.currentDocument},
			dataType:"json",
			success:loadTF,
			failure:failedTF

		});


	});




	$(document.body).on('click','.document-name' , function(event){
		
		loadDocument(event.target.text);
		app.currentDocument = event.target.text;

	});


	function loadDocument(document) {

		function loadDocumentSuccess(text){
			$("#plain-text-area").html("");
			$("#plain-text-area").html(text);
		}

		function loadDocumentFailure(){
			$("#Documents li.active").removeClass("active");
		}

		$.ajax({
			type:"GET",
			url:"/getContent/"+document,
			dataType:"text",
			success:loadDocumentSuccess,
			failure:loadDocumentFailure
		});		

	}

	function loadDocuments(){

		function loadDocumentsSuccess(json){
			$("#plain-text-area").html("");
			$("#tokenized-text-area").html("");
			$("#POS-text-area").html("");
			$("chunked-text-area").html("");
			$("entity-text-area").html("");

			$.each(json.data,function(key,value){
				$("#dropdown-area").append("<li><a class=document-name>"+value.name+"</a></li>");
			});		
		}

		$.ajax({
			type:"GET",
			url:"/loadFileNames",
			dataType:"json",
			success:loadDocumentsSuccess
		});

	}

	loadDocuments();

});