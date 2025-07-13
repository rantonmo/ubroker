from flask import current_app
from flask import Blueprint, render_template

bp = Blueprint('bl_ubroker', __name__)

@bp.route('/')
@bp.route('/index')
def index():
    return render_template('index.html', the_title='This is the index page')

@bp.route('/summary')
def summary():
    return render_template('summary.html', the_title='This is the summary page', test_var='first session with Fernando')
