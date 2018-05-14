"""Main translator file: Functions to translate and detect runes."""

from constants import logger
from tables import english_table, futhark_table


def translate(query, is_futhark=False):
    """Translate a string from Futhark to and from English."""
    log_message = 'Translating to {}...'
    if is_futhark is True:
        log_message = log_message.format('English')
        translation = query.translate(english_table)
    else:
        log_message = log_message.format('Futhark')
        query = query.lower()
        translation = query.translate(futhark_table)
    logger.info(log_message)
    return translation


def detect_translate(query):
    """Detect the language and translate accordingly."""
    log_message = 'Detected {} text.'
    average_codepoint = sum(
        ord(char) for char in query
    ) / len(query)
    if average_codepoint < 1000:
        log_message = log_message.format('English')
        logger.info(log_message)
        translation = translate(query)
    else:
        log_message = log_message.format('Futhark')
        logger.info(log_message)
        translation = translate(query, is_futhark=True)
    return translation
