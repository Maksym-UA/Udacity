$(document).ready(function(){
	
	//Animate scroll
		
	var amountScrolled = 380;
	//set the value when the button appears	
	$(window).scroll(function() {
		if ( $(this).scrollTop() > amountScrolled ) {
			$('a.goUpButton').fadeIn('slow');
		} 
		
		else {
			$('a.goUpButton').fadeOut('slow');
		}
	});
	
	
	$('a.goUpButton').click(function() {
		$('html, body').animate({
			scrollTop: 0
		}, 700);
		return false;
	});
	
	
	// Pause the video when the modal is closed
    $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
        // Remove the src so the player itself gets removed, as this is the only
        // reliable way to ensure the video stops playing in IE
        $("#trailer-video-container").empty();
    });
	
    // Start playing the video whenever the trailer modal is opened
    $(document).on('click', '.movie-tile', function (event) {
        var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
        var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
        $("#trailer-video-container").empty().append($("<iframe></iframe>", {
            'id': 'trailer-video',
            'type': 'text-html',
            'src': sourceUrl,
            'frameborder': 0
        }));
    });
		
    // Animate in the movies when the page loads
    $(document).ready(function () {
        $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
        });
    });

	//Call side navigation menu
	$('.toggle').click( function(){
		//panel initially positioned out of the window
		$('.genreMenu').animate({left: '0px'}, "fast");
		$('.toggle').fadeToggle(500);
					
		return false;
	});

	$('.closebtn').click( function(){
		//return panel to its initial posiiton
		$('.genreMenu').animate({left: -250}, 200);
		$('.toggle').fadeToggle(700);		
		return false;
	});		


	//Show movies of the selected genre
	var $content = $('.movie-tile');
	var $menuItems = $('.topnav a');
	//console.log(menuItems);
	//console.log(content);
		
	$($menuItems).not($menuItems[0]).each(function (){
		$(this).click(function(){
			//alert(this.id);
			for(var i = 0; i < $content.length; i++){
				//compare if the clicked menu item is the same as movie genre
				if (this.id === $content[i].id){
					console.log("menu id: " + this.id + " main id: " + $content[0].id);
					$($content[i]).fadeIn('fast');
				}
					
				else if (this.id === 'fullListSel' ){
					$('.movie-tile').fadeIn('fast');
				}
					
				else{
					$($content[i]).fadeOut('fast');
				}
			}
		});
	});
});
	