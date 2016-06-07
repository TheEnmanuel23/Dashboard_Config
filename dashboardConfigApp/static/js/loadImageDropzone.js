Dropzone.options.myDropzone = {   
autoProcessQueue : false,
uploadMultiple: false,
maxFiles: 1,
addRemoveLinks: true,
init: function() {
		myDropzone = this;
		var submitButton = $('#btnSave');

		submitButton.addEventListener("click", function(e){
			e.preventDefault();
			e.stopPropagation();
			myDropzone.processQueue();
		});
	    this.on("success", function(file, responseText) {
	        // evento lanzado al terminar de subir las imágenes en cola
	        console.log(responseText);
	    });
	    this.on("addedFile", function(){
	    	console.log("se ha agregado una nueva imagen");
	    });
	}
}
	/*Dropzone.autoDiscover = false;
	$("#dropzone").dropzone({
		autoProcessQueue : false,
		addRemoveLinks: true,
		acceptedFiles: 'image/*, .svg',
		complete: function(file){
			if(file.status == "success"){
				alert("se ha subido el archivo correctamente"+ file.name);
			}
		},
		error: function(file){
			alert("Error al subir el archivo"+ file.name);
		}
	})
	*/
	/*
	Dropzone.options.zoneToLoadSvg = {
		autoProcessQueue : false,
		init: function(){

		console.log("ya inicion co dropzone");	
			var $btnSaveAll = $("#btnSaveAll");
			$btnSaveAll.addListener("click", function(){
				zoneToLoadSvg.processQueue();
			});
			this.on("addedfile", function(){

			})
		}
	}*/