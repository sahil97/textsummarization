import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/igniton', methods=('GET', 'POST'))
def register():
    return '[Controller.py] Working'
