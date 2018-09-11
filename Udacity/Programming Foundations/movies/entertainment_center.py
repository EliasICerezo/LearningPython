import media
import fresh_tomatoes
jaws = media.Movie("JAWS",
                        "A giant white shark threatens the inhabitants and tourists of a coastal town.",
                        "https://vignette.wikia.nocookie.net/jaws/images/d/da/Jaws-movie-poster.jpg/revision/latest?cb=20131015071208",
                        "https://www.youtube.com/watch?v=U1fu_sA7XhE" )



star_wars= media.Movie("Star Wars",
                       "The story of a boy, a girl and the universe",
                       "https://cdn.shopify.com/s/files/1/2028/5101/products/starwarsiv-2436-ti-1_large.jpg?v=1496332442",
                       "https://www.youtube.com/watch?v=XHk5kCIiGoM")


interstellar= media.Movie("Interstellar",
                          "A story of how love connect the universe",
                          "https://images-na.ssl-images-amazon.com/images/I/516j7Sqay4L.jpg",
                          "https://www.youtube.com/watch?v=9Lk6A_tq3DA")


mile8 = media.Movie("8-Mile",
                    "The story of Eminem",
                    "https://images-na.ssl-images-amazon.com/images/I/413DH01B7GL._SY445_.jpg",
                    "https://www.youtube.com/watch?v=axGVrfwm9L4")

alien= media.Movie("Alien the 8th Passenger",
                   "The story of how a rescue mission ends with 1 last survivor",
                   "https://images-na.ssl-images-amazon.com/images/I/5119C4MWJ0L._SY445_.jpg",
                   "https://www.youtube.com/watch?v=D3oC17nILkw")

training_day= media.Movie("Training Day",
                          "The story of how a corrupt police officer gets killed",
                          "https://pics.filmaffinity.com/training_day-607055595-large.jpg",
                          "https://www.youtube.com/watch?v=gKTVQPOH8ZA")

movies=[jaws,star_wars,interstellar,mile8,alien,training_day]

#fresh_tomatoes.open_movies_page(movies)

print(media.Movie.__module__)
