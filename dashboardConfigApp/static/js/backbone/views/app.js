ConfigDashboard.Views.App = Backbone.View.extend({
	el: $('body'),
	events: {
		'click #btnCreateNewProject' : 'startToCreateProject',
		'click #btnCancelCreationProject, #btnCloseCreationsProject': 'cancelCreationProject',
		'change #btnOpenFile': 'loadImageIntoContainer'
	},
	initialize: function($el){
		this.$el = $el;
	},
	startToCreateProject : function(sender){
		var projectName = $('#txtProjectName').val();
		$('#nameNewProject').html('Proyecto:'+ projectName);
		Backbone.history.navigate('new_project/' + projectName, {trigger: true});
	},
	cancelCreationProject: function(){
		Backbone.history.navigate('new_project/', {trigger: true});
		$('#contentNewProject').children().prop('disabled', 'true');
		this.newProject();
	},
	newProject: function(){
		$('#txtProjectName').val('');
		$('#nameNewProject').html('Proyecto:');
	},
	loadImageIntoContainer:  function(e){
		var workSpace = Snap("#containerImage");
		if($('#btnOpenFile').val() != '') {
			$('#containerImage').empty();
			var url = URL.createObjectURL(e.target.files[0]);
			Snap.load(url, function ( data ) {
			   	workSpace.append(data);
			});
		}
	}
});