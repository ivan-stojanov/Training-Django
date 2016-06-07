function searchSuccess(data, textStatus, jqXHR){	
	$("#search-result").html(data);
}


$(document).ready(function(){
	
	$(document).on("click", ".delete-btn", function (e) {
		if (confirm("Are you sure you want to delete this inventory?")){
			  
		} else {
			e.preventDefault();
		}
	});
	
	$(document).on("click", ".search-btn", function (e) {
		e.preventDefault();
		$.ajax({
			type: "POST",
			url: "/stock/inventory/search/",
			data: {
				"search_term": $("#search_term").val(),
				"search_type": $("#search_type").val(),
				"sort_by_item": $("#sort_by_item").val(),
				"sort_by_dir": $("#sort_by_dir").val(),
				"search_page": $("#search_page").val(),
				"csrfmiddlewaretoken": $("input[name=csrfmiddlewaretoken]").val()
			},			
			success: searchSuccess,
			dataType: "html"			
		});		
	});	
	
	$(document).on("click", ".sort-btn", function (e) {		
		var class_id_name = e.target.id;
		var sort_by_item = class_id_name.replace("sort-", "");
		
		var sort_by_dir = "ASC";
		if($(this).hasClass("sort-desc")){
			sort_by_dir = "DESC";
		}
		
		var search_page = $("#current-page").text();
		$("#sort_by_item").val(sort_by_item);
		$("#sort_by_dir").val(sort_by_dir);
		$("#search_page").val(search_page);

		$.ajax({
			type: "POST",
			url: "/stock/inventory/search/",
			data: {
				"search_term": $("#search_term").val(),
				"search_type": $("#search_type").val(),
				"sort_by_item": sort_by_item,
				"sort_by_dir": sort_by_dir,
				"search_page": search_page,
				"csrfmiddlewaretoken": $("input[name=csrfmiddlewaretoken]").val()
			},
			success: searchSuccess,
			dataType: "html"			
		});	
	});
	
	$(document).on("click", ".pagination-btn", function (e) {		
		var class_id_name = e.target.id;
		var search_page = class_id_name.replace("page-", "");
		
		$("#search_page").val(search_page);
		
		$.ajax({
			type: "POST",
			url: "/stock/inventory/search/",
			data: {
				"search_term": $("#search_term").val(),
				"search_type": $("#search_type").val(),
				"sort_by_item": $("#sort_by_item").val(),
				"sort_by_dir": $("#sort_by_dir").val(),
				"search_page": search_page,
				"csrfmiddlewaretoken": $("input[name=csrfmiddlewaretoken]").val()
			},
			success: searchSuccess,
			dataType: "html"			
		});	
	});	
	
})