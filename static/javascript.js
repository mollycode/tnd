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
		

		var divs = $('div[id^="slideshow"]').hide(),
		i = 0;
	
		(function cycle() { 
			divs.eq(i).effect("slide")
					  .delay(6000)
					  .show(0)
					  .hide(0, cycle)
					  
			i = ++i % divs.length; // increment i, 
								   //   and reset to 0 when it equals divs.length
		})();


}); 