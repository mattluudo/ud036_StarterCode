import webbrowser


# Movie class provides basic information for a movie such as the title
# and links to its respective poster art and trailer clip.
class Movie():
    def __init__(self, title, poster_url, trailer_url):
        self.title = title
        self.poster_url = poster_url
        self.trailer_url = trailer_url

    def show_trailer(self):
        webbrowser.open(self.trailer_url)

