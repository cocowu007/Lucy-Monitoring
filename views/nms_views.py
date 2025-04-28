from flask import Blueprint
import logging
from services.nms_service import nms_landing, nms_index

nms_bp = Blueprint('nms', __name__)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

@nms_bp.route('/')
def nms_landing_page():
    logging.info("-----------nms_landing in nms_views------")
    return nms_landing()


@nms_bp.route('/home')
def nms_index_page():
    logging.info("-----------nms_index in nms_views------")
    return nms_index()
