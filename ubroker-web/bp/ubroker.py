from flask import current_app
from flask import Blueprint, render_template

from ..lib.utils import set_menu

bp = Blueprint('bl_ubroker', __name__)

@bp.route('/')
@bp.route('/index')
def index():
    mc = set_menu('home')
    return render_template('index.html', mc=mc, the_title='This is the index page')

@bp.route('/summary')
def summary():
    mc = set_menu('summary')
    return render_template('summary.html', mc=mc, the_title='This is the summary page', test_var='first session with Fernando')
