# Library that helps to open default webbroswer.
import webbrowser

# OS module in Python provides a way of using operating system dependent
# functionality.
# The functions that the OS module provides allows you to interface with the
# underlying operating system that Python is running on.
import os

# This module provides regular expression matching operations similar to those
# found in Perl. Both patterns and strings to be searched can be Unicode
# strings as well as 8-bit strings.
import re

'''This code helps set page layout and dynamically add movies to
the page'''

# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Maksym Savin Moviel List via Fresh Tomatoes!</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
	
    <link rel="stylesheet" type="text/css" media="screen" href="movieList.css">
    <script type="text/javascript" charset="utf-8"></script>
    <script src="movieListScript.js" type="text/javascript"></script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body>
		<div class="background-image"></div>


		<!-- Trailer Video Modal -->
		<div class="modal" id="trailer">
			<div class="modal-dialog">
				<div class="modal-content">
					<a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
						<img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
                    </a>
					<div class="scale-media" id="trailer-video-container">
					</div>
				</div>
			</div>
        </div>

    <!-- Main Page Content -->
    <div class="container">
	
	<a name="top"></a> 
		
	<div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
	    <div class="container">
			<div class="navbar-header">
				<a class="navbar-brand" href="#">Maksym Savin Movie List via Fresh Tomatoes</a>
			</div>
			</div>
        </div>
    </div>
	
    <!-- side panel (sliding) to choose different movie genres-->
	<div class = "genreMenu">
        <ul class="topnav" >
			<li><a href="#" class="closebtn" >&times;</a></li>
			<li><a href="#" id="fullListSel"><strong>Full list</strong></a></li>
			<li><a href="#" id="action"><h4>Action </h4></a></li>
			<li><a href="#" id="adventure"><h4>Adventure</h4></a></li>
			<li><a href="#" id="animation"><h4>Animation</h4></a></li>
			<li><a href="#" id="biography"><h4>Biography</h4></a></li>
			<li><a href="#" id="comedy"><h4>Comedy</h4></a></li>
			<li><a href="#" id="crime"><h4>Crime</h4></a></li>
			<li><a href="#" id="fantasy"><h4>Fantasy</h4></a></li>
			<li><a href="#" id="drama"><h4>Drama</h4></a></li>
			<li><a href="#" id="sci-fi"><h4>Sci-Fi</h4></h4></a></li>
			<li><a href="#" id="sport"><h4>Sport</h4></a></li>
			<li><a href="#" id="war"><h4>War</h4></a></li>
	    </ul>
	</div>
	
	
	<!--button to open side menu-->
	<a href="" class="toggle" >
		<img src="glyphicons-114-justify.png" alt="glyphicon menu">
	</a>
	
    <div class="container" id="main">
      {movie_tiles}
    </div>
	
	
    <!-- Go up button to scroll up the page-->
	<a href="#top" class="goUpButton">	
		
	</a>
  </body>
  
</html>
'''

# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" id= {movie_genre}
    data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal"
    data-target="#trailer">
    <img src="{poster_image_url}" width="220" height="342">
    <h2>{movie_title}</h2>
    <h3>{movie_year}</h3>
    <!-- <h4>{movie_genre}</h4>-->
</div>
'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            movie_year=movie.year,
            movie_genre=movie.genre,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id
        )
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
