# Tic Tac Toe in Python

#### Video Demo: https://youtu.be/FxEypMb_FZc

#### Description:
This project is a Python-based Tic Tac Toe game designed to be played in the console between two players. Utilizing libraries such as `tabulate` for displaying the game board in a structured format, and `pyfiglet` for rendering stylized text, the game offers a visually appealing and interactive experience directly from the command line with necessary error handing capabilities.

### Features:
- **Interactive Console-Based UI:** The game leverages the console for input and output, making it faster and easier to access without the need for a graphical user interface (GUI).
- **Dynamic Game Board:** Utilizes a 3x3 matrix to simulate the tic tac toe grid, which updates after each player's turn. Each block of the 2D Matrix is predefinedly represents the position making it easier for players to choose in which box they want to select. 
- **Input Validation:** Ensures that the players' inputs are valid moves within the game board. It denies any invalid inputs and reprompts the user for valid input. For example, if non-numeric value inserted then denies it, there are 9 positions in 3x3 matrix, so if enters a number greater then 9 or less then 1 then denies it.
- **Clear and Concise UI:** Uses `tabulate` to render the main game board making it easier and more accessible for the users to play and `pyfiglet` for game banners, for instance, winner announchment for tie declaretion enhancing the user experience.
- **Win Detection:** Implements logic to check for a winner or a tie. As we all know, the player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row is the winner. SO, after total 4th move it checks for the winner because atleast 5 moves are needed to win a game. If no player succeeds to do that, then the game is a tie.

### How It Works:
1. **Starting the Game:** Upon launch, the game displays an introductory message using stylized text via `pyfiglet` and shows an empty tic tac toe board. The board is presented in a 3x3 grid format, with each position numbered from 1 to 9, corresponding to different slots on the board.

2. **Player Turns:** The game alternates between two players:
    - **Player 1** is assigned the 'X' marker.
    - **Player 2** is assigned the 'O' marker.
   Each player chooses a position on the board by entering a number from 1 to 9. The game checks if the chosen position is valid (i.e., not already taken) and updates the board accordingly.

3. **Input Validation:** After a player enters their choice, the game validates the input to ensure it is a number between 1 and 9 and that the chosen position is not already occupied. If the input is invalid, the game prompts the player to choose again.

4. **Updating the Board:** Once a valid input is received, the game updates the board by placing the player's marker ('X' or 'O') in the chosen position. The updated board is then displayed to both players.

5. **Checking for a Winner:** After each turn, the game checks for any winning conditions:
    - A player wins if their markers align horizontally, vertically, or diagonally.
    - The game also checks if the board is fully occupied without any player winning, indicating a tie.

6. **Game Conclusion:** The game ends when one player wins by aligning three of their markers or when all positions are filled, resulting in a tie. The game then displays a congratulatory message to the winner or a message indicating a tie.

7. **Restart or Exit:** After the game concludes, players are given the option to restart the game or exit. If they choose to restart, the game initializes a new empty board, and the process begins anew.

This sequential flow ensures that the game is interactive, fair, and straightforward, providing an engaging experience for both players involved.

### Project Structure:
- `tic_tac_toe_project.py`: Contains the main game logic, including the UI setup, game loop, and functions for handling player inputs, updating the game state, and determining the game outcome.
- `test_tic_tac_toe_project.py`: Includes tests for critical functions used in the game, ensuring reliability and correctness of the game mechanics.

### Testing:
The project employs unit tests to validate the functionality of its components, such as input handling, board updating, and win condition checking. These tests are crucial for maintaining the integrity of the game logic.

### Design Choices:
- **Console-Based Design:** Chosen for its simplicity and universal accessibility, allowing the game to be played on any system with Python and the necessary libraries installed.
- **Modular Functions:** The game logic is divided into several functions, facilitating easy testing and potential future enhancements.
- **External Libraries:** `tabulate` and `pyfiglet` were selected to enhance the UI/UX without complicating the game's core logic.

This project not only serves as an entertaining game but also as a demonstration of applying basic Python programming concepts, such as loops, conditionals, and function calls, in creating an interactive application.

### Installation and Running the Game:
To run this project, ensure you have Python installed along with the `tabulate` and `pyfiglet` libraries. You can start the game by executing `python tic_tac_toe_project.py` in your terminal.

Enjoy playing Tic Tac Toe!
