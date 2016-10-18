# coding :utf-8
import anitube
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search_word', methods=['POST'])
def search():
    if request.method == 'POST':
        text = request.form['search_word']
        movie_infos = []

        soup = anitube.Anitube(text)
        movies = soup.getMovieURL()
        titles = soup.titles
        images = soup.thumbnails
        for i in range(len(movies)):
            movie_info = {}
            movie_info["movie_url"] = movies[i]
            movie_info["title"] = titles[i]
            movie_info["thumbnail"] = images[i]
            movie_infos.append(movie_info)

        return render_template("index.html", movie_infos=movie_infos)


if __name__ == '__main__':
    app.run(port=9999, debug=True)
