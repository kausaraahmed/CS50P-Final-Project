
from tic_tac_toe_project import is_even, choice_position, clear_screen, found_winner

def test_is_even():
    assert is_even(0) == True
    assert is_even(1) == False
    assert is_even(2) == True
    assert is_even(3) == False


def test_choice_position():
    assert choice_position(1) == (0, 0)
    assert choice_position(2) == (0, 1)
    assert choice_position(3) == (0, 2)
    assert choice_position(5) == (1, 1)
    assert choice_position(6) == (1, 2)
    assert choice_position(7) == (2, 0)
    assert choice_position(10) == None

def test_clear_screen():
    assert clear_screen() == None

def test_found_winner():
    # Test cases for rows
    assert found_winner([['X', 'X', 'X'], ['4', '5', '6'], ['7', '8', '9']]) == 'X'
    assert found_winner([['1', '2', '3'], ['O', 'O', 'O'], ['7', '8', '9']]) == 'O'

    # Test cases for columns
    assert found_winner([['1', 'O', '3'], ['4', 'O', '6'], ['7', 'O', '9']]) == 'O'
    assert found_winner([['1', '2', 'X'], ['4', '5', 'X'], ['7', '8', 'X']]) == 'X'

    # Test cases for diagonals
    assert found_winner([['X', '2', '3'], ['4', 'X', '6'], ['7', '8', 'X']]) == 'X'
    assert found_winner([['1', '2', 'O'], ['4', 'O', '6'], ['O', '8', '9']]) == 'O'


