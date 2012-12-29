$(document).ready(function() { 
        $("#courseTable").tablesorter( {sortList: [[2,0], [0,0]]} ); 
		$("ul.thumbnails").ytplaylist({addThumbs:true, autoPlay: false, holderId: 'ytvideo1'});
    } 
); 

/*$(document).ready(function() {
	$(".navtitle").mouseover(function() {
		var img = $(this).find('img');
		var file = img.attr('src').split('.')[0];
		img.attr('src', file + 'hover.png');
	}).mouseout(function() {
		var img = $(this).find('img');
		var file = img.attr('src').split('hover')[0];
		img.attr('src', file + '.png');
	});
	
	
	

	$(".more").one( "click", function () {

		$("#coursedescription").css( "height","+=200" );
		$("#coursecontent").css("height", "+=200");
		$(".author").css("top","-=200");
		$("#courseright").css("top","-=200");

	});





});

*/