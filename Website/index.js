$(document).ready(function() {
    $('#resume_page').hide();
    $('#other_interests').hide();
	document.getElementById('resume_link').onclick = function() {
		$('#resume_page').show();
		$('#main_page_content').hide();
        $('#other_interests').hide();
	};
	document.getElementById('Other').onclick = function() {
        $('#resume_page').hide();
        $('#main_page_content').hide();
		$('#other_interests').show();
	};
    document.getElementById('about_lan').onclick = function() {
        $('#resume_page').hide();
        $('#main_page_content').show();
        $('#other_interests').hide();
    };
});







