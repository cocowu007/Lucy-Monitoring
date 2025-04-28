from flask import Blueprint
import logging
from services.iot_service import iot_landing, iot_index

iot_bp = Blueprint('iot', __name__)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

@iot_bp.route('/')
def iot_landing_page():
    logging.info("-----------iot_landing in iot_views------")
    return iot_landing()


@iot_bp.route('/home')
def iot_index_page():
    logging.info("-----------iot_index in iot_views------")
    return iot_index()
