var display_writing = function(writing){

      //clear entries to allow for potential update
      $("#allWritingPieces").html("");
     

      for(i = 0; i < writing.length; i++){

            var entry = "<div class='row'> <div class='col-md-3'>" + writing[i].title + '\
            </div> <div class="col-md-3">' + writing[i].username + '</div>\
            <div class="col-md-1">' + writing[i].type + '</div><div class="col-md-1">' + writing[i].genre + '</div>' + 
            "<div class=\"col-md-1\"> <button type=\"button\" class=\"btn btn-view view\" href=\"/view_item_feedback/" + writing[i].id +
            '\">View</button></div>' ;

        if(writing[i].username == "priya_pai"){

            entry = entry + "<div class=\"col-md-1\"> <button type=\"button\" class=\"btn btn-warning edit\" href=\"/edit_item/" + writing[i].id +
            '\">Edit</button></div>' + '<div class=\"col-md-1"\> <button type=\"button\" class=\"btn btn-warning delete\"\
             data-index=\"'+ i + '\" id=\"' + writing[i].id + '\">Delete</button></div>' + '</div>';
       }

            $("#allWritingPieces").prepend(entry);
      }
}

//takes in an id, makes ajax call to server, returns array to ajax call
var delete_writing = function(id){
      id=id;
      index = $("#"+id).attr("data-index");

      $.ajax({
            type:"POST",
            url: "delete_writing/" + id,
            dataType : "json",
            contentType: "application/json; charset=utf-8",
            data : JSON.stringify(writing),
            success: function(result){

                  //update javascript sales variable - remove 
                  writing.splice(index,1);

                  //update UI
                  display_writing(writing);

            },
            error: function(request, status, error){
                  console.log("Error")
                  console.log(request)
                  console.log(status)
                  console.log(error)
            }
            })

}

$(document).ready(function(){
      $("#homeTab").removeClass("active");
      $("#viewAllTab").addClass("active");
      $("#editTab").removeClass("active");
      $("#uploadTab").removeClass("active");

      //initial display 
      display_writing(writing);

      //for deleting 
      $("#allWritingPieces").on("click",".delete", function(){

            delete_writing($(this).attr("id"));

      });

      
      $("#allWritingPieces").on("click",".edit", function(){

            location.href = $(this).attr("href");

      });

      $("#allWritingPieces").on("click",".btn-view", function(){

            location.href = $(this).attr("href");

      });
});