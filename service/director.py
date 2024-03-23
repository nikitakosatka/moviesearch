from flask import jsonify, request
from flask.wrappers import Response

from base import db
from model.director import Director


def create_director() -> Response:
    request_form = request.get_json()

    new_director = Director(
        fio=request_form["director"]["fio"],
    )
    db.session.add(new_director)
    db.session.commit()

    director = Director.query.get(new_director.id).to_dict()

    response = {"director": director}
    return jsonify(response)


def get_all_directors() -> Response:
    directors = Director.query.all()
    response = {"list": []}
    for director in directors:
        response["list"].append(director.to_dict())
    return jsonify(response)


def get_director_by_id(director_id: int) -> Response:
    response = Director.query.get_or_404(director_id).to_dict()
    return jsonify(response)


def delete_director(director_id: int) -> Response:
    Director.query.filter_by(id=director_id).delete()
    db.session.commit()
    response = {"message": 'Director with Id "{id}" deleted successfully'}
    return jsonify(response)


def update_director(director_id: int) -> Response:
    director = Director.query.filter_by(id=director_id).update(
        request.get_json()["director"]
    )
    db.session.commit()
    response = {"director": director}
    return jsonify(response)
