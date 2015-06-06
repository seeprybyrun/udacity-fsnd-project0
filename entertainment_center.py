import media
import fresh_tomatoes as ft

# imdbify and youtubify are used to reduce the number of times we
# need to rewrite repeated parts of URLs
def imdbify(id_code):
    prefix = 'http://ia.media-imdb.com/images/M/'
    suffix = '._V1_SX214_AL_.jpg'
    return prefix + id_code + suffix

def youtubify(id_code):
    return 'https://www.youtube.com/watch?v=' + id_code

# start by populating a list of the top 25 movies on IMDB
movies = [
    media.Movie(
        'The Shawshank Redemption',
        imdbify('MV5BODU4MjU4NjIwNl5BMl5BanBnXkFtZTgwMDU2MjEyMDE@'),
        youtubify('6hB3S9bIaco')
    ),
    media.Movie(
        'The Godfather',
        imdbify('MV5BMjEyMjcyNDI4MF5BMl5BanBnXkFtZTcwMDA5Mzg3OA@@'),
        youtubify('sY1S34973zA')
    ),
    media.Movie(
        'The Godfather: Part II',
        imdbify('MV5BNDc2NTM3MzU1Nl5BMl5BanBnXkFtZTcwMTA5Mzg3OA@@'),
        youtubify('qJr92K_hKl0')
    ),
    media.Movie(
        'The Dark Knight',
        imdbify('MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@'),
        youtubify('EXeTwQWrcwY')
    ),
    media.Movie(
        'Pulp Fiction',
        imdbify('MV5BMjE0ODk2NjczOV5BMl5BanBnXkFtZTYwNDQ0NDg4'),
        youtubify('wZBfmBvvotE')
    ),
    media.Movie(
        "Schindler's List",
        imdbify('MV5BMzMwMTM4MDU2N15BMl5BanBnXkFtZTgwMzQ0MjMxMDE@'),
        youtubify('dwfIf1WMhgc')
    ),
    media.Movie(
        '12 Angry Men',
        imdbify('MV5BODQwOTc5MDM2N15BMl5BanBnXkFtZTcwODQxNTEzNA@@'),
        youtubify('A7CBKT0PWFA')
    ),
    media.Movie(
        'The Good, the Bad, and the Ugly',
        imdbify('MV5BOTQ5NDI3MTI4MF5BMl5BanBnXkFtZTgwNDQ4ODE5MDE@'),
        youtubify('13EUXqIwDkQ')
    ),
    media.Movie(
        'The Lord of the Rings: The Return of the King',
        imdbify('MV5BMjE4MjA1NTAyMV5BMl5BanBnXkFtZTcwNzM1NDQyMQ@@'),
        youtubify('WIrRJ8bCZYQ')
    ),
    media.Movie(
        'Fight Club',
        imdbify('MV5BMjIwNTYzMzE1M15BMl5BanBnXkFtZTcwOTE5Mzg3OA@@'),
        youtubify('J8FRBYOFu2w')
    ),
    media.Movie(
        'The Lord of the Rings: The Fellowship of the Ring',
        imdbify('MV5BNTEyMjAwMDU1OV5BMl5BanBnXkFtZTcwNDQyNTkxMw@@'),
        youtubify('Pki6jbSbXIY')
    ),
    media.Movie(
        'Star Wars: Episode V - The Empire Strikes Back',
        imdbify('MV5BMjE2MzQwMTgxN15BMl5BanBnXkFtZTcwMDQzNjk2OQ@@'),
        youtubify('96v4XraJEPI')
    ),
    media.Movie(
        'Forrest Gump',
        imdbify('MV5BMTQwMTA5MzI1MF5BMl5BanBnXkFtZTcwMzY5Mzg3OA@@'),
        youtubify('uPIEn0M8su0')
    ),
    media.Movie(
        'Inception',
        imdbify('MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@'),
        youtubify('66TuSJo4dZM')
    ),
    media.Movie(
        "One Flew Over the Cuckoo's Nest",
        imdbify('MV5BMTk5OTA4NTc0NF5BMl5BanBnXkFtZTcwNzI5Mzg3OA@@'),
        youtubify('2WSyJgydTsA')
    ),
    media.Movie(
        'The Lord of the Rings: The Two Towers',
        imdbify('MV5BMTAyNDU0NjY4NTheQTJeQWpwZ15BbWU2MDk4MTY2Nw@@'),
        youtubify('2dlRvAjU_RI')
    ),
    media.Movie(
        'Goodfellas',
        imdbify('MV5BMTY2OTE5MzQ3MV5BMl5BanBnXkFtZTgwMTY2NTYxMTE@'),
        youtubify('qo5jJpHtI1Y')
    ),
    media.Movie(
        'The Matrix',
        imdbify('MV5BMTkxNDYxOTA4M15BMl5BanBnXkFtZTgwNTk0NzQxMTE@'),
        youtubify('m8e-FF8MsqU')
    ),
    media.Movie(
        'Star Wars: Episode IV - A New Hope',
        imdbify('MV5BMTU4NTczODkwM15BMl5BanBnXkFtZTcwMzEyMTIyMw@@'),
        youtubify('1g3_CFmnU7k')
    ),
    media.Movie(
        'Seven Samurai',
        imdbify('MV5BMTc5MDY1MjU5MF5BMl5BanBnXkFtZTgwNDM2OTE4MzE@'),
        youtubify('MwvpUtc1hBU')
    ),
    media.Movie(
        'City of God',
        imdbify('MV5BMjA4ODQ3ODkzNV5BMl5BanBnXkFtZTYwOTc4NDI3'),
        youtubify('ioUE_5wpg_E')
    ),
    media.Movie(
        'Se7en',
        imdbify('MV5BMTQwNTU3MTE4NF5BMl5BanBnXkFtZTcwOTgxNDM2Mg@@'),
        youtubify('J4YV2_TcCoE')
    ),
    media.Movie(
        'The Usual Suspects',
        imdbify('MV5BMzI1MjI5MDQyOV5BMl5BanBnXkFtZTcwNzE4Mjg3NA@@'),
        youtubify('oiXdPolca5w')
    ),
    media.Movie(
        'The Silence of the Lambs',
        imdbify('MV5BMTQ2NzkzMDI4OF5BMl5BanBnXkFtZTcwMDA0NzE1NA@@'),
        youtubify('lQKs169Sl0I')
    ),
    media.Movie(
        "It's a Wonderful Life",
        imdbify('MV5BMTMzMzY5NDc4M15BMl5BanBnXkFtZTcwMzc4NjIxNw@@'),
        youtubify('LJfZaT8ncYk')
    )
]

# then display the fresh_tomatoes page based on the movies in the
# list above
ft.open_movies_page(movies)
