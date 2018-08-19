import webbrowser
'''
webbrowser module is defined inside Python Standard Library
webbrowser module has functions like open defined in it
A class Movie has been created containing information related to movies
'''


class Movie():
    """init function initializes or creates space in memory.
    init function is called as soon as an instance is created.
    __init__ is reserved name in python,
    this is shown with the help of two underscore one both sides of word init
    self represents the instance of class.
    Instance variables are initialized with values that init function recieves.
    """
    def __init__(self, movie_name, movie_storyline,
                 movie_poster_image, youtube_tailer):
        self.title = movie_name
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster_image
        self.trailer_youtube_url = youtube_tailer

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
    """show_trailer is the function used to play the trailer.
    open function is defined in file webbrowser we used to open youtube trailer
    """
