from flask import jsonify
from werkzeug.exceptions import HTTPException

from app import app


class RatingValidationException(ValueError):
    pass


class YearValidationException(ValueError):
    pass


@app.errorhandler(Exception)
def handle_exception(e: Exception):
    if isinstance(e, HTTPException):
        return e
    return jsonify({"status": 500, "reason": str(e)}), 500
