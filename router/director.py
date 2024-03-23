from app import app
from service.director import (
    create_director,
    get_all_directors,
    get_director_by_id,
    update_director,
)


@app.route("/directors", methods=["POST"])
def post_director():
    return create_director(), 201


@app.route("/directors", methods=["GET"])
def get_directors():
    return get_all_directors()


@app.route("/directors/<id>", methods=["GET"])
def get_director(id: int):
    return get_director_by_id(id)


@app.route("/directors/<id>", methods=["PATCH"])
def patch_director(id: int):
    return update_director(id), 201
