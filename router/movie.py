from flask import jsonify

from app import app
from exception import RatingValidationException
from service.movie import create_movie, get_all_movies, get_movie_by_id, update_movie


@app.route("/movies", methods=["POST"])
def post_movie():
    try:
        return create_movie(), 201
    except RatingValidationException:
        return jsonify(error="Rating must be between 0 and 10", status=403), 403


@app.route("/movies", methods=["GET"])
def get_movies():
    return get_all_movies()


@app.route("/movies/<id>", methods=["GET"])
def get_movie(id: int):
    return get_movie_by_id(id)


@app.route("/movies/<id>", methods=["PATCH"])
def patch_movie(id: int):
    try:
        return update_movie(id), 201
    except RatingValidationException:
        return jsonify(error="Rating must be between 0 and 10", status=403), 403
