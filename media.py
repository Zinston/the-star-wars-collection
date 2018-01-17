class Movie:
    """This class defines and display a movie.
       It takes a title and a trailer video."""

    def __init__(self, title, trailer, poster):
        self.title = title
        self.trailer_youtube_url = trailer
        self.poster_image_url = poster
