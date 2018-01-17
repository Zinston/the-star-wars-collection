import media
import fresh_tomatoes


def create_movies_collection():
    # Create an empty list to contain the movies
    movies = []

    # Create the movies and append them to the list
    movies.append(
      media.Movie(
        "Star Wars: Episode IV - A New Hope",
        "https://www.youtube.com/watch?v=9gvqpFbRKtQ",
        "https://images-na.ssl-images-amazon.com/images/I/61zAtWHeXLL._SY445_.jpg"  # noqa
      )
    )

    movies.append(
      media.Movie(
        "Star Wars: Episode V - The Empire Strikes Back",
                              "https://www.youtube.com/watch?v=JNwNXF9Y6kY",
                              "https://i.jeded.com/i/star-wars-episode-v--the-empire-strikes-back.13948.jpg"  # noqa
      )
    )

    movies.append(
      media.Movie(
        "Star Wars: Episode VI - Return of the Jedi",
                              "https://www.youtube.com/watch?v=CsDwpF3uiZI",
                              "https://vignette.wikia.nocookie.net/starwars/images/b/b2/ReturnOfTheJediPoster1983.jpg/revision/latest?cb=20170926193831"  # noqa
      )
    )

    movies.append(
      media.Movie(
        "Star Wars: Episode I - The Phantom Menace",
                              "https://www.youtube.com/watch?v=bD7bpG-zDJQ",
                              "https://vignette.wikia.nocookie.net/starwars/images/7/75/EPI_TPM_poster.png/revision/latest?cb=20130822171446"  # noqa
      )
    )

    movies.append(
      media.Movie(
        "Star Wars: Episode II - Attack of the Clones",
                              "https://www.youtube.com/watch?v=gYbW1F_c9eM",
                              "https://vignette.wikia.nocookie.net/starwars/images/9/98/Aotctpb.jpg/revision/latest?cb=20110206033257"  # noqa
      )
    )

    movies.append(
      media.Movie(
        "Star Wars: Episode III - Revenge of the Sith",
                              "https://www.youtube.com/watch?v=5UnjrG_N8hU",
                              "https://i.ytimg.com/vi/47JUXQU5fKw/maxresdefault.jpg"  # noqa
      )
    )

    movies.append(
      media.Movie(
        "Star Wars: Episode VII - The Force Awakens",
                              "https://www.youtube.com/watch?v=sGbxmsDFVnE",
                              "https://images-na.ssl-images-amazon.com/images/M/MV5BOTAzODEzNDAzMl5BMl5BanBnXkFtZTgwMDU1MTgzNzE@._V1_UY1200_CR91,0,630,1200_AL_.jpg"  # noqa
      )
    )

    movies.append(
      media.Movie(
        "Rogue One: A Star Wars Story",
                              "https://www.youtube.com/watch?v=frdj1zb9sMY",
                              "https://a.ltrbxd.com/resized/film-poster/2/5/8/1/2/8/258128-rogue-one-a-star-wars-story-0-230-0-345-crop.jpg?k=90f1f7dc7f"  # noqa
      )
    )

    movies.append(
      media.Movie(
        "Star Wars: Episode VIII - The Last Jedi",
                              "https://www.youtube.com/watch?v=Q0CbN8sfihY",
                              "https://vignette.wikia.nocookie.net/starwars/images/f/fe/TheLastJediTheatricalPoster.jpeg/revision/latest?cb=20171010002420"  # noqa
      )
    )

    # Return the list
    return movies

movies = create_movies_collection()
fresh_tomatoes.open_movies_page(movies)
