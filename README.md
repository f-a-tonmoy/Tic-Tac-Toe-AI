## 📝 Project Overview

This project implements a dynamic **Tic Tac Toe** game where a human player competes against an AI that uses the **Minimax algorithm with Alpha-Beta Pruning** for optimal moves. The game supports custom board sizes (`N x N`) and offers two difficulty modes: **Easy** and **Hard**. The AI adjusts its strategy based on the difficulty mode, leveraging random and estimated moves for faster gameplay in larger grids.

---

## 📂 Project Structure

```plaintext
├── TTT.py                         # Core game logic and AI implementation
├── CSE366 Project Report.pdf      # Detailed report on design and implementation
├── README.md                      # Project documentation
```

---

## 🚀 Features

1. **Game Modes**:
   - **Easy Mode**: AI makes random or estimated moves with a higher chance of human victory.
   - **Hard Mode**: AI uses Minimax with Alpha-Beta Pruning for optimal moves.

2. **Customizable Gameplay**:
   - Supports any board size (`N x N`) with adjustable complexity.
   - Provides clear instructions and feedback during gameplay.

3. **AI Strategy**:
   - **Alpha-Beta Pruning**:
     - Speeds up decision-making by pruning unnecessary branches of the game tree.
     - Balances computational efficiency and game performance.
   - **Random and Estimated Moves**:
     - Introduced for early-game scenarios in large grids to reduce computation time.
   - Dynamically blocks the player’s winning moves when possible.

4. **Interactive Gameplay**:
   - Visually engaging terminal interface with color-coded feedback using **Colorama**.
   - AI and player moves are highlighted for clarity.

5. **Error Handling**:
   - Ensures valid input and gracefully handles edge cases during gameplay.

---

## 🛠️ Dependencies

Install the required libraries using:
```bash
pip install -r requirements.txt
```

### `requirements.txt` Content:
```plaintext
colorama
```

---

## 🎮 How to Play

1. Clone the repository:
   ```bash
   git clone https://github.com/f-a-tonmoy/tic-tac-toe.git
   cd tic-tac-toe
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the game:
   ```bash
   python TTT.py
   ```

4. Follow the instructions to select the difficulty mode (`Easy` or `Hard`) and start playing!

---

## 🔍 AI Algorithm Overview

1. **Minimax Algorithm**:
   - Evaluates all possible moves to minimize the maximum loss for the AI player.
   - Recursive approach to explore all potential game states.

2. **Alpha-Beta Pruning**:
   - Enhances Minimax by eliminating branches that don't influence the final decision.
   - Parameters:
     - **α (Alpha)**: Best option for the human player.
     - **β (Beta)**: Best option for the AI player.

3. **Estimation and Random Moves**:
   - For larger boards, AI makes random or estimated moves in the early game to reduce computation time.

---

## 🧪 Testing Results

- **Easy Mode**:
  - AI occasionally makes suboptimal moves to give the human player a fair chance.
- **Hard Mode**:
  - AI optimally blocks winning moves and prioritizes its own victory using Alpha-Beta Pruning.

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 💬 Contact

For inquiries or feedback:
- **Fahim Ahamed**: [f.a.tonmoy00@gmail.com](mailto:f.a.tonmoy00@gmail.com)
- GitHub: [f-a-tonmoy](https://github.com/f-a-tonmoy)
```
