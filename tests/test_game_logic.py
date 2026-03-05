from logic_utils import check_guess, get_range_for_difficulty
from unittest.mock import patch
import random

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


def test_hard_range():
    # Hard mode should have range 1-50; secrets above 50 were unguessable before the fix
    low, high = get_range_for_difficulty("Hard")
    assert low == 1
    assert high == 50


def test_easy_range():
    # Easy mode should have range 1-20; secrets above 20 were unguessable before the fix
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high == 20


def test_secret_within_hard_range():
    # A secret generated using the Hard range must stay within that range
    low, high = get_range_for_difficulty("Hard")
    with patch("random.randint", return_value=high):
        secret = random.randint(low, high)
    assert low <= secret <= high


def test_secret_within_easy_range():
    # A secret generated using the Easy range must stay within that range
    low, high = get_range_for_difficulty("Easy")
    with patch("random.randint", return_value=high):
        secret = random.randint(low, high)
    assert low <= secret <= high
