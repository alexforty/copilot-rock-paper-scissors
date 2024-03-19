import pytest
from main import determine_winner

choices = ['rock', 'paper', 'scissors', 'lizard', 'spock']
expected_results = {
    ('rock', 'scissors'): 'You win!',
    ('rock', 'lizard'): 'You win!',
    ('rock', 'rock'): 'Draw!',
    ('rock', 'paper'): 'You lose!',
    ('rock', 'spock'): 'You lose!',
    ('paper', 'rock'): 'You win!',
    ('paper', 'spock'): 'You win!',
    ('paper', 'paper'): 'Draw!',
    ('paper', 'scissors'): 'You lose!',
    ('paper', 'lizard'): 'You lose!',
    ('scissors', 'paper'): 'You win!',
    ('scissors', 'lizard'): 'You win!',
    ('scissors', 'scissors'): 'Draw!',
    ('scissors', 'rock'): 'You lose!',
    ('scissors', 'spock'): 'You lose!',
    ('lizard', 'spock'): 'You win!',
    ('lizard', 'paper'): 'You win!',
    ('lizard', 'lizard'): 'Draw!',
    ('lizard', 'rock'): 'You lose!',
    ('lizard', 'scissors'): 'You lose!',
    ('spock', 'scissors'): 'You win!',
    ('spock', 'rock'): 'You win!',
    ('spock', 'spock'): 'Draw!',
    ('spock', 'paper'): 'You lose!',
    ('spock', 'lizard'): 'You lose!'
    # add the rest of the combinations here
}

@pytest.mark.parametrize('user_choice,computer_choice', expected_results.keys())
def test_determine_winner(user_choice, computer_choice):
    assert determine_winner(user_choice, computer_choice) == expected_results[(user_choice, computer_choice)]

    