import fresh_tomatoes  # import the file fresh_tomatoes kept in the same folder
import media  # import file media that contains class Movie

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar = media.Movie("Avatar",
                     "Story of people trying to acquire planet panora",
                     "avatar.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
django_unchained = media.Movie("Django Unchained",
                               "The story of a slave trying to save his wife",
                               "Django_Unchained_Poster.jpg",
                               "https://www.youtube.com/watch?v=eUdM9vrCbow")
blood_diamond = media.Movie("Blood diamond",
                            "A smuggler along with fisherman finds a diamond",
                            "Blooddiamondposter.jpg",
                            "https://www.youtube.com/watch?v=yknIZsvQjG4")
inception = media.Movie("Inception",
                        "A group of extractors enter the subconcious",
                        "Inception_poster.jpg",
                        "https://www.youtube.com/watch?v=66TuSJo4dZM")
avengers = media.Movie("The Avengers",
                       "A group of superheroes save earth from Loki's army",
                       "avengers.jpg",
                       "https://www.youtube.com/watch?v=eOrNdBpGMv8")

'''
In the above code we have created six instances of class Movie
an array containing names of all the instances of class created
'''
movies = [toy_story, avatar, django_unchained,
          blood_diamond, inception, avengers]
'''
open_movies_page is a function defined in fresh_tomatoes.ph
tomatoes.ph file that accepts movies as argument
'''
fresh_tomatoes.open_movies_page(movies)
