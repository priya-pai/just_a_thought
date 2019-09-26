
var save_feedback = function(edited_item, index){
	var edited_writing= edited_item;
	var idx = index;

	$.ajax({
		type:"POST",
		url: "/save_feedback/" + edited_item.id,
		dataType: "json",
		contentType: "application/json; charset=utf-8",
		data: JSON.stringify(edited_writing),
		success: function(result){

      //add feedback to the term
			writing.splice(idx, 1, edited_writing);
      $("#feedbackArea").html("<p>" + edited_writing["feedback"] + "</p></div><div class = \"col-md-12\"><button type=\"button\" id=\"editFeedback\" class=\"btn btn-warning\">Edit Feedback</button>")
		},
    error: function(request, status, error){

      $("#feedbackBottom").append("<div id=\"error\">Error! Writing could not be uploaded.</div>")
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
  $("#editTab").addClass("active");
  $("#uploadTab").removeClass("active");

     //initial display 
  $("#titleView").html(title);
  $("#usernameView").html(username);
  $("#contentView").html(content);
  $("#typeView").html(typE);
  $("#genreView").html(genre);

if(feedback==""){
  $("#feedbackArea").html("<textarea rows=\"25\" cols=\"50\" id=\"feedbackEnter\"></textarea></div><div class = \"col-md-12\"><button type=\"button\" id=\"submitFeedback\" class=\"btn btn-primary\">Submit Feedback</button>");
}
else{
  $("#feedbackArea").html("<p>" + feedback + "</p></div><div class = \"col-md-12\"><button type=\"button\" id=\"editFeedback\" class=\"btn btn-warning\">Edit Feedback</button>");
}

$(document).on('click', '#editFeedback', function() {
   $("#feedbackArea").html("<textarea rows=\"25\" cols=\"50\" id=\"feedbackEnter\">" + feedback + "</textarea></div><div class = \"col-md-12\"><button type=\"button\" id=\"submitFeedback\" class=\"btn btn-primary\">Submit Feedback</button>");
})

$(document).on('click', '#submitFeedback', function() {
      edited_item = {
      "id": item,
      "title": title,
      "username": username, 
          "type": typE, 
          "genre": genre,
          "content": content,
          "feedback": $("#feedbackEnter").val()};
      save_feedback(edited_item, index);
    });
});