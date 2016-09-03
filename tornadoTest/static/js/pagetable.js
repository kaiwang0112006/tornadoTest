
function pagetable(url,tid){
	$(document).ready(function() {
		var tjid = '#'+tid;
		$(tjid).dataTable().fnDestroy();
	    $(tjid).dataTable( {
	        "bServerSide": true,
	        "sAjaxSource": url,
	        "bProcessing": true,
	        "pagingType": "full_numbers",
	    } );
	});
}


function pagetableClient(url,tid){
	var tjid = '#'+tid;
	$(tjid).dataTable( {
        "ajax": url,
        "bProcessing": true,
        "pagingType": "full_numbers",
    } );
}




function pagetableClienthtml(tid){
	var tjid = '#'+tid;
	//alert(tjid)
	$(tjid).dataTable( {
        "pagingType": "full_numbers",
    } );
}









function show_hide(id,imgid){
	var target = document.getElementById(id);
	target.hidden = !target.hidden;

	var imgid = "#"+imgid
	var img = $(imgid).attr("src")
	var pathlist = img.split('/')
	var pl = pathlist.length
	//alert(pathlist[pl-1])
	if (pathlist[pl-1] == "arrowright.png"){
		var newimg = $(imgid).attr("src").replace("arrowright", "arrowdown");
		$(imgid).attr("src",newimg)
	}else if (pathlist[pl-1] == "arrowdown.png"){
		var newimg = $(imgid).attr("src").replace("arrowdown", "arrowright");
		$(imgid).attr("src",newimg)
	}
}




function ebookpagetable(url,tid){
	$(document).ready(function() {
		var tjid = '#'+tid;
		 
	    $(tjid).dataTable( {
	        "bServerSide": true,
	        "sAjaxSource": url,
	        "bProcessing": true,
	        "pagingType": "full_numbers",
          "aoColumnDefs": [ 
            {
              "aTargets": [ 1 ],
              "mData": "download_link",
              "mRender": function ( data, type, full ) {
              	return '<a href="/ebooksPDF/'+full[0] + '">'+ full[1] +'</a>';
              }
            }
            ]
	    } );
	});

}

function videopagetable(url,tid){
	$(document).ready(function() {
		var tjid = '#'+tid;
		 
	    $(tjid).dataTable( {
	        "bServerSide": true,
	        "sAjaxSource": url,
	        "bProcessing": true,
	        "pagingType": "full_numbers",
          "aoColumnDefs": [ 
            {
              "aTargets": [ 1 ],
              "mData": "download_link",
              "mRender": function ( data, type, full ) {
              	return '<a href="/video/'+full[0] + '">'+ full[1] +'</a>';
              }
            }
            ]
	    } );
	});

}

function musicpagetable(url,tid){
	$(document).ready(function() {
		var tjid = '#'+tid;
		 
	    $(tjid).dataTable( {
	        "bServerSide": true,
	        "sAjaxSource": url,
	        "bProcessing": true,
	        "pagingType": "full_numbers",
          "aoColumnDefs": [ 
            {
              "aTargets": [ 1 ],
              "mData": "download_link",
              "mRender": function ( data, type, full ) {
              	return '<a href="/music/'+full[0] + '">'+ full[1] +'</a> (<a href="/static/music/' + full[2] + '">Download</a>)';
              }
            }
            ]
	    } );
	});

}