import re

NUMERIC_PATTERN = r'^-?\d+(\.\d+)?$'
INTEGER_PATTERN = r'^-?\d+$'
STRING_PATTERN = r'^[a-zA-Z_]+$'
STRING_WITH_SPACE_PATTERN = r'^[a-zA-Z_ ]+$'
STRING_WITH_SPACE_AND_SPECIAL_CHARS = r'^[a-zA-Z\s_\-ñáéíóúÁÉÍÓÚ]+$'
OPTIONS_PATTERN = r'\b(?:{})\b'


def validate_number(string_integer: str) -> bool:
    return re.match(NUMERIC_PATTERN, string_integer) is not None

def validate_integer(string_integer: str) -> bool:
    return re.match(INTEGER_PATTERN, string_integer) is not None

def validate_string(word: str) -> bool:
    return re.match(STRING_PATTERN, word) is not None

def validate_string_with_space(word: str) -> bool:
    return re.match(STRING_WITH_SPACE_PATTERN, word) is not None

def validate_string_with_space_and_special_chars(word: str) -> bool:
    return re.match(STRING_WITH_SPACE_AND_SPECIAL_CHARS, word) is not None

# this is from chatgpt, emergency use only (?)
def validate_option(word: str, valid_options: list) -> bool:
    return re.search(OPTIONS_PATTERN.format('|'.join(map(re.escape, [o.lower() for o in valid_options]))), word.lower())

# this is from chatgpt, emergency use only (?)
def validate_option_not_strict(word: str, valid_options: list) -> bool:
    return len(re.findall(OPTIONS_PATTERN.format('|'.join(map(re.escape, valid_options))), word, flags=re.IGNORECASE)) > 0