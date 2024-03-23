from flask import jsonify, request
from flask.wrappers import Response

from base import db
from model.movie import Movie


def create_movie() -> Response:
    request_form = request.get_json()

    new_movie = Movie(
        id=request_form["movie"].get("id"),
        title=request_form["movie"]["title"],
        year=request_form["movie"]["year"],
        director=request_form["movie"]["director"],
        length=request_form["movie"]["length"],
        rating=request_form["movie"]["rating"],
    )
    db.session.add(new_movie)
    db.session.commit()

    movie = Movie.query.get(new_movie.id).to_dict()

    response = {"movie": movie}
    return jsonify(response)


def get_all_movies() -> Response:
    movies = Movie.query.all()
    response = {"list": []}
    for movie in movies:
        response["list"].append(movie.to_dict())
    return jsonify(response)


def get_movie_by_id(movie_id: int) -> Response:
    response = Movie.query.get_or_404(movie_id).to_dict()
    return jsonify(response)


def delete_movie(movie_id: int) -> Response:
    Movie.query.filter_by(id=movie_id).delete()
    db.session.commit()
    response = {"message": 'Movie with Id "{id}" deleted successfully'}
    return jsonify(response)


def update_movie(movie_id: int) -> Response:
    movie = Movie.query.filter_by(id=movie_id).update(request.get_json()["movie"])
    db.session.commit()
    response = {"movie": movie}
    return jsonify(response)
