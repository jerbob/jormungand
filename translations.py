"""Main translator file: English <-> Elder Farthark."""

from tables import english_table, futhark_table


def translate(query, is_futhark=False):
    """Translate a string from Futhark <-> English."""
    if is_futhark is True:
        translation = query.translate(english_table)
    else:
        query = query.lower()
        translation = query.translate(futhark_table)
    return translation


def detect_translate(query):
    """Detect the language and translate accordingly."""
    average_codepoint = sum(
        ord(char) for char in query
    ) / len(query)
    if average_codepoint < 1000:
        return translate(query)
    else:
        return translate(query, is_futhark=True)
