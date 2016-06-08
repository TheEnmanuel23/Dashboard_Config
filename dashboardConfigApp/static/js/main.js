$(document).ready(function(){
	window.views.app = new StepsConfig.Views.App($('body'));
	window.routers.steps = new StepsConfig.Routers.StepsConfig();
	window.routers.steps.on("route:root", function(){
	});
	window.routers.steps.on("route:step", function(){
	});
	Backbone.history.start({
			root: '/',
			pushState: true
	});

	$("#btnOpenFile").change(function(e){
		var workSpace = Snap("#containerImage");
		if($('#btnOpenFile').val() != '') {
			$('#containerImage').empty();
			var url = URL.createObjectURL(e.target.files[0]);
			Snap.load(url, function ( data ) {
			   	workSpace.append(data);
			});
		}
	});
});