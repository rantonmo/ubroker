import logging
import logging.config
import os
import yaml


from flask import Flask

from .lib.error_handlers import *

from .bp import main

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY=os.environ['SESSION_SECRET'],
    )
    # logging config
    with open(os.path.join(app.instance_path, 'logging.yaml')) as lcf:
        logging.config.dictConfig(yaml.safe_load(lcf.read()))
    logger = logging.getLogger("init")

    # config_file = "config.yaml"
    # logger.info("reading app config from file %s", config_file)
    # app.config.from_file(config_file, load=yaml.safe_load)

    # if not os.path.isfile(os.path.join(app.instance_path, config_file)):
    #     logger.error("Config file %s not found", config_file)
    #     raise RuntimeError(f"No config file found: {config_file}")


    logger.info("registering main blueprints")
    app.register_blueprint(main.bp)

    logger.info("registering error handlers")
    app.register_error_handler(500, error_500)
    app.register_error_handler(404, error_404)

    logger.info("app ready... starting...")
    return app