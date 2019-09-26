var search = function(search_item){
		var matchingItems = []

		//standardize to remove case sensitivity errors
		search_term = search_item.toUpperCase();

		//search each field for substring matches
		$.each(writing, function(i, piece){
			if (piece["title"].toUpperCase().includes(search_term)){
				matchingItems.unshift(piece);
				return;
			}
			if (piece["genre"].toUpperCase().includes(search_term)){
				matchingItems.unshift(piece);
				return;
			}
			if (piece["type"].toUpperCase().includes(search_term)){
				matchingItems.unshift(piece);
				return;
			}	
			if (piece["username"].toUpperCase().includes(search_term)){
				matchingItems.unshift(piece);
				return;
			}	
		});

		if(matchingItems.length != 0){
			subheading = "<div class='row' id=\"subH\"> <div class='col-md-3'> Title </div><div class=\"col-md-3\">"+
			"Username</div> <div class=\"col-md-3-2\">Type</div><div class=\"col-md-2\"> Genre </div></div>"
			$("#searchResults").append(subheading)
		}
		for(i=0; i<matchingItems.length; i++){
		var entry = "<div class='row'> <div class='col-md-3'>" + matchingItems[i].title + '\
        </div> <div class="col-md-3">' + matchingItems[i].username + '</div>\
        <div class="col-md-3-2">' + matchingItems[i].type + '</div><div class="col-md-2">' + matchingItems[i].genre + '</div>\
        <div class="col-md-2"> <button type="button" class="btn btn-view view" href="/view_item_feedback/' + matchingItems[i].id +
        '">View</button></div><br>'; 

    	$("#searchResults").append(entry);}

    	
};

$(document).ready(function(){
	$("#homeTab").removeClass("active");
	$("#viewAllTab").removeClass("active");
	$("#editTab").addClass("active");
	$("#uploadTab").removeClass("active");

	$("#search").click(function(){
		$(".add").remove();
		searchTerm = $("#searchItem").val();
		search(searchTerm);
	});
    $("#searchItem").keypress(function(event){
            var keycode = (event.keyCode ? event.keyCode : event.which);
            if(keycode == '13'){
            	$(".add").remove();
				searchTerm = $("#searchItem").val();
				search(searchTerm);
            }
    }); 
    $("#searchResults").on("click",".view", function(){

            location.href = $(this).attr("href");

      }); 
    $("#searchItem").autocomplete({
    	source:tags
    }); 
});