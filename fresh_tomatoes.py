import webbrowser
import os
import re
import media


# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes!</title>
    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .movie-tile:hover {
            background-color: #EEE;
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
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
    </script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body>
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
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Fresh Tomatoes Movie Trailers</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      {movie_tiles}
    </div>
  </body>
</html>
'''


# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <img src="{poster_image_url}" width="220" height="342">
    <h2>{movie_title}</h2>
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


def create_movies_collection():
    # Create an empty list to contain the movies
    movies = []

    # Create the movies and append them to the list
    movies.append( media.Movie("Star Wars: Episode IV - A New Hope",
                              "https://www.youtube.com/watch?v=9gvqpFbRKtQ",
                              "https://images-na.ssl-images-amazon.com/images/I/51-oAlQIwIL._SX302_BO1,204,203,200_.jpg") )
    movies.append( media.Movie("Star Wars: Episode V - The Empire Strikes Back",
                              "https://www.youtube.com/watch?v=JNwNXF9Y6kY",
                              "https://i.jeded.com/i/star-wars-episode-v--the-empire-strikes-back.13948.jpg") )
    movies.append( media.Movie("Star Wars: Episode VI - Return of the Jedi",
                              "https://www.youtube.com/watch?v=CsDwpF3uiZI",
                              "https://vignette.wikia.nocookie.net/starwars/images/b/b2/ReturnOfTheJediPoster1983.jpg/revision/latest?cb=20170926193831") )
    movies.append( media.Movie("Star Wars: Episode I - The Phantom Menace",
                              "https://www.youtube.com/watch?v=bD7bpG-zDJQ",
                              "https://vignette.wikia.nocookie.net/starwars/images/7/75/EPI_TPM_poster.png/revision/latest?cb=20130822171446") )
    movies.append( media.Movie("Star Wars: Episode II - Attack of the Clones",
                              "https://www.youtube.com/watch?v=gYbW1F_c9eM",
                              "https://vignette.wikia.nocookie.net/starwars/images/9/98/Aotctpb.jpg/revision/latest?cb=20110206033257") )
    movies.append( media.Movie("Star Wars: Episode III - Revenge of the Sith",
                              "https://www.youtube.com/watch?v=5UnjrG_N8hU",
                              "https://i.ytimg.com/vi/47JUXQU5fKw/maxresdefault.jpg") )
    movies.append( media.Movie("Star Wars: Episode VII - The Force Awakens",
                              "https://www.youtube.com/watch?v=sGbxmsDFVnE",
                              "https://images-na.ssl-images-amazon.com/images/M/MV5BOTAzODEzNDAzMl5BMl5BanBnXkFtZTgwMDU1MTgzNzE@._V1_UY1200_CR91,0,630,1200_AL_.jpg") )
    movies.append( media.Movie("Rogue One: A Star Wars Story",
                              "https://www.youtube.com/watch?v=frdj1zb9sMY",
                              "https://a.ltrbxd.com/resized/film-poster/2/5/8/1/2/8/258128-rogue-one-a-star-wars-story-0-230-0-345-crop.jpg?k=90f1f7dc7f") )
    movies.append( media.Movie("Star Wars: Episode VIII - The Last Jedi",
                              "https://www.youtube.com/watch?v=Q0CbN8sfihY",
                              "https://vignette.wikia.nocookie.net/starwars/images/f/fe/TheLastJediTheatricalPoster.jpeg/revision/latest?cb=20171010002420") )

    # Return the list
    return movies

movies = create_movies_collection()
open_movies_page(movies)
