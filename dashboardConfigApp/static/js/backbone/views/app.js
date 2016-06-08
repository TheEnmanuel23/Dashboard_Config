StepsConfig.Views.App = Backbone.View.extend({
	el: $('body'),
	events: {
		'click #btnCreateNewProject' : 'startToCreateProject',
		'click #btnCancelCreationProject, #btnCloseCreationsProject': 'cancelCreationProject',
	},
	initialize: function($el){
		this.$el = $el;
	},
	startToCreateProject : function(sender){
		var projectName = $('#txtProjectName').val();
		$('#nameNewProject').html('Proyecto:'+ projectName);
		Backbone.history.navigate('new_project/' + projectName, {trigger: true});
		//$('#contentNewProject').prop('disabled', 'false');
	},
	cancelCreationProject: function(){
		Backbone.history.navigate('new_project/', {trigger: true});
		$('#contentNewProject').children().prop('disabled', 'true');
		this.newProject();
	},
	newProject: function(){
		$('#txtProjectName').val('');
		$('#nameNewProject').html('Proyecto:');
	}
});