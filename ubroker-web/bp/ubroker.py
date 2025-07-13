from flask import current_app
from flask import Blueprint, render_template

from ..lib.utils import set_menu

bp = Blueprint('bl_ubroker', __name__)

@bp.route('/')
@bp.route('/summary')
def summary():
    mc = set_menu('summary')
    return render_template('summary.html', mc=mc)

@bp.route('/monitors')
def monitors():
    mc = set_menu('monitors')
    return render_template('monitors.html', mc=mc)

@bp.route('/rules')
def rules():
    mc = set_menu('rules')
    return render_template('rules.html', mc=mc)


@bp.route('/status')
def status():
    mc = set_menu('status')
    return render_template('status.html', mc=mc)