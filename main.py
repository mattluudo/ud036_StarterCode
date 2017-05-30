import fresh_tomatoes
from movie import Movie

# Create instances of my favorite movies
dark_knight = Movie(title="The Dark Knight",
                    poster_url="https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
                    trailer_url="https://www.youtube.com/watch?v=5y2szViJlaY")

remember_the_titan = Movie(title="Remember the Titans",
                           poster_url="https://upload.wikimedia.org/wikipedia/en/d/d1/Remember_the_titansposter.jpg",
                           trailer_url="https://www.youtube.com/watch?v=nPhu9XsRl4M")

gone_girl = Movie(title="Gone Girl",
                  poster_url="https://upload.wikimedia.org/wikipedia/en/0/05/Gone_Girl_Poster.jpg",
                  trailer_url="https://www.youtube.com/watch?v=2-_-1nJf8Vg")

ratatouille = Movie(title="Ratatouille",
                    poster_url="https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                    trailer_url="https://www.youtube.com/watch?v=niD-jahFURU")

inception = Movie(title="Inception",
                  poster_url="https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg",
                  trailer_url="https://www.youtube.com/watch?v=8hP9D6kZseM")

deadpool = Movie(title="Deadpool",
                 poster_url="https://upload.wikimedia.org/wikipedia/en/4/46/Deadpool_poster.jpg",
                 trailer_url="https://www.youtube.com/watch?v=Xithigfg7dA")

# Create an array for my favorite movies
movies = [dark_knight, remember_the_titan, gone_girl,
          ratatouille, inception, deadpool]

# Create and open html movie page with my favorite movies
fresh_tomatoes.open_movies_page(movies)
