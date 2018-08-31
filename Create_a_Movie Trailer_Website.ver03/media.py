#Hello, I'm hyungoo. this files is Create a Movie Website project. it is 2nd version.
#please check it. thank you.

import webbrowser

class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        """
        This function a reserved method in class. __init__ called when an object is created
        from the class and it allow the class to initialize movie's information.

        Behavior:
            this function have some attribute in common and differentiated from others by
            kind type.

        Attribute:
            movie_title(str) : holds the title of movies. this type is string.
            movie_storyline(str) : holds the plot of movies. this type is string.
            poster_image(str) : holds the url linked to the movie's image files.
            trailer_youtube(str) : holds the url to the movie's youtube trailer.

        output:
            return an instance of members for the new movie object.
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """
        this function allow trailer open when user click on web brower's movie poster image.

        Attribute:
            webbrowser.open(str) : this module imported by webbrowser and open method allow displaying
            youtube url using the default browser.
        """
        webbrowser.open(self.trailer_youtube_url)
