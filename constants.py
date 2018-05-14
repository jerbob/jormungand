"""Variables and functions required across multiple files."""

import logging

logger = logging.getLogger('Jormungand')
logger.setLevel('INFO')

console_handler = logging.StreamHandler()
console_handler.setLevel('INFO')

logger.addHandler(console_handler)
