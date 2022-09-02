"""Top-level package for verdant."""
# Core Library modules
import logging.config
from importlib import resources

# Third party modules
import toml  # type: ignore
import yaml  # type: ignore

LOGGING_CONFIG = """
version: 1
disable_existing_loggers: False
handlers:
  console:
    class: logging.StreamHandler
    level: INFO
    stream: ext://sys.stdout
    formatter: basic
  file:
    class: logging.FileHandler
    level: DEBUG
    filename: verdant.log
    encoding: utf-8
    formatter: timestamp

formatters:
  basic:
    style: "{"
    format: "{levelname:s}:{name:s}:{message:s}"
  timestamp:
    style: "{"
    format: "{asctime} - {levelname} - {name} - {message}"

loggers:
  init:
    handlers: [console, file]
    level: DEBUG
    propagate: False
"""

logging.config.dictConfig(yaml.safe_load(LOGGING_CONFIG))
logger = logging.getLogger("init")

_toml_text = resources.read_text("verdant", "config.toml")
toml_config = toml.loads(_toml_text)


__title__ = "verdant"
__version__ = "0.1.0"
__author__ = "Stephen R A King"
__description__ = "placeholder"
__email__ = "stephen.ra.king@gmail.com"
__license__ = "MIT"
__copyright__ = "Copyright 2022 Stephen R A King"
