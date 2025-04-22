from flask import Flask, render_template
from views.iot_views import iot_bp
from views.nms_views import nms_bp

app = Flask(__name__)
app.secret_key = 'your-secure-key'

# Register blueprints
app.register_blueprint(iot_bp, url_prefix='/iot')
app.register_blueprint(nms_bp, url_prefix='/nms')

@app.route('/')
def landing():
    return render_template('landing.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
