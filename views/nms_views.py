from flask import Blueprint, render_template

nms_bp = Blueprint('nms', __name__)

@nms_bp.route('/')
def nms_index():
    return render_template('index.html', mode='nms')
