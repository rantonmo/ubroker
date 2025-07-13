import logging
import traceback

from flask import render_template

def handle_error(e):
    logger = logging.getLogger('error')
    logger.info("code: %s - name: %s - desc: %s", e.code, e.name, e.description)
    # mc is for the menu highlighting, which in this case should not be set
    return render_template(f'errorpages/error{e.code}.html', mc="",
                           tb=traceback.format_exc()), e.code
