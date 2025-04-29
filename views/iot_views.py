from flask import Blueprint
import logging
from services.iot_service import iot_landing, iot_index

iot_bp = Blueprint('iot', __name__)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

@iot_bp.route('/', methods=['GET'])
def iot_landing_page():
    return iot_landing()


@iot_bp.route('/home', methods=['GET', 'POST'])
def iot_index_page():
    return iot_index()
