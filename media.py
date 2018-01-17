class Movie:
    """This class defines a movie.
       
       Attributes:
       	title (str): The title of the movie.
        trailer (str): The url of the movie's trailer on youtube.
        poster (str): The url of the movie's poster image."""

    def __init__(self, title, trailer, poster):
        self.title = title
        self.trailer_youtube_url = trailer
        self.poster_image_url = poster
