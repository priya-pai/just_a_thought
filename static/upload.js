var upload_writing = function(new_item){
	var new_writing= new_item;

	$.ajax({
		type:"POST",
		url: "/save_writing",
		dataType: "json",
		contentType: "application/json; charset=utf-8",
		data: JSON.stringify(new_writing),
		success: function(result){
			//add writing to writing variable
			writing.unshift(new_writing)
			current_id += 1
			location.href = "/view_all"
		},
        error: function(request, status, error){

        	$("#content").append("<div id=\"error\">Error! Writing could not be uploaded.</div>")
			console.log("Error")
			console.log(request)
			console.log(status)
			console.log(error)
        }
		})
};

$(document).ready(function(){
	$("#homeTab").removeClass("active");
	$("#viewAllTab").removeClass("active");
	$("#editTab").removeClass("active");
	$("#uploadTab").addClass("active");

	$("#addWriting").click(function(){
		var new_writing = {
    		"title": $("#title").val(),
    		"username": "priya_pai", 
            "type": $("#type").val(), 
            "genre": $("#genre").val(),
            "content": $("textarea#content").val(),
            "feedback": ""};
		upload_writing(new_writing);
	});
});