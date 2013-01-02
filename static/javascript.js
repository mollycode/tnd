$(document).ready(function() { 
        $("#courseTable").tablesorter( {
			/*sortList: [[2,0], [0,0]],
			headers: {
			0: {sorter: 'text'},
			1: {sorter: 'text'},
			2: {sorter: 'monthDayYear'}, 
			}*/
		}); 
		$("ul.thumbnails").ytplaylist({addThumbs:true, autoPlay: false, holderId: 'ytvideo1'});
    } 
); 


$.tablesorter.addParser({
  id: 'monthDayYear',
  is: function(s) {
      return false;
  },
  format: function(s) {
      var date = s.match(/^(\w{3})[ ](\d{1,2}),[ ](\d{4})$/);
      var m = monthNames[date[1]];
      var d = String(date[2]);
      if (d.length == 1) {d = "0" + d;}
      var y = date[3];
	 
      return '' + y + m + d;
  },
  type: 'numeric'
});
var monthNames = {};
monthNames["Jan"] = "01";
monthNames["Feb"] = "02";
monthNames["Mar"] = "03";
monthNames["Apr"] = "04";
monthNames["May"] = "05";
monthNames["Jun"] = "06";
monthNames["Jul"] = "07";
monthNames["Aug"] = "08";
monthNames["Sept"] = "09";
monthNames["Oct"] = "10";
monthNames["Nov"] = "11";
monthNames["Dec"] = "12";

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