var save_edits = function(edited_item, index){
	var edited_writing= edited_item;
	var idx = index;

	$.ajax({
		type:"POST",
		url: "/save_edits/" + edited_item.id,
		dataType: "json",
		contentType: "application/json; charset=utf-8",
		data: JSON.stringify(edited_writing),
		success: function(result){

			writing.splice(idx, 1, edited_writing);

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
    $("#uploadTab").removeClass("active");

      //initial display 
      $("#titleEdit").html(title);
      $("#usernameEdit").html(username);
      $("#contentEdit").html(content);
      $("#typeEdit").html(typE);
      $("#genreEdit").html(genre);

      $("#saveEdit").click(function(){
      	edited_item = {
      		"id": item,
    		"title": $("#titleEdit").val(),
    		"username": username, 
            "type": $("#typeEdit").val(), 
            "genre": $("#genreEdit").val(),
            "content": $("#contentEdit").val(),
            "feedback": ""};
        save_edits(edited_item, index);
      });
});