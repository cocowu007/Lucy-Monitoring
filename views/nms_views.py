from flask import Blueprint
import logging
from services.nms_service import nms_landing, nms_index

nms_bp = Blueprint('nms', __name__)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

@nms_bp.route('/', methods=['GET'])
def nms_landing_page():
    return nms_landing()


@nms_bp.route('/home', methods=['GET', 'POST'])
def nms_index_page():
    return nms_index()
