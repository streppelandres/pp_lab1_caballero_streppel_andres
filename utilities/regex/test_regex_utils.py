from regex_utils import *

def test_validate_number():
    assert validate_number("123") is True
    assert validate_number("-45.67") is True
    assert validate_number("-789") is True
    assert validate_number("12.34.56") is False
    assert validate_number("abc") is False

def test_validate_integer():
    assert validate_integer("123") is True
    assert validate_integer("123,23") is False
    assert validate_integer("-45.67") is False
    assert validate_integer("-789") is True
    assert validate_integer("12.34.56") is False
    assert validate_integer("abc") is False


def test_validate_string():
    assert validate_string("HolaMundo") is True
    assert validate_string("text") is True
    assert validate_string("abc123") is False
    assert validate_string("¡Hello!") is False


def test_validate_string_with_space():
    assert validate_string_with_space("Hello World") is True
    assert validate_string_with_space("text with space") is True
    assert validate_string_with_space("abc123") is False
    assert validate_string_with_space("¡Hola!") is False

def test_validate_string_with_space_and_special_chars():
    assert validate_string_with_space_and_special_chars("Hello World") is True
    assert validate_string_with_space_and_special_chars("text with spácé") is True
    assert validate_string_with_space_and_special_chars("abc_defg") is True
    assert validate_string_with_space_and_special_chars("Hola señora") is True


def test_validate_option():
    valid_options = ["Pomelo", "Mora", "Uva"]
    assert validate_option("Pomelo", valid_options) is not None
    assert validate_option("mora", valid_options) is not None
    assert validate_option("Manzana", valid_options) is None
    assert validate_option("Morado", valid_options) is None
    assert validate_option("Uva!", valid_options) is not None

def test_validate_options_not_strict():
    valid_options = ["Pomelo", "Mora", "Uva"]
    assert validate_option_not_strict('uv', valid_options) is False
    assert validate_option_not_strict('uva', valid_options) is True
    assert validate_option_not_strict('uVa', valid_options) is True
    assert validate_option_not_strict('Manzana', valid_options) is False
    assert validate_option_not_strict('POMELO', valid_options) is True
    assert validate_option_not_strict('mora', valid_options) is True
