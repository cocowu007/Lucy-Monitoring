from flask import Blueprint, render_template

iot_bp = Blueprint('iot', __name__)

@iot_bp.route('/')
def iot_index():
    return render_template('index.html', mode='iot')
