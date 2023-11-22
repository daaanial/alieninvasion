# Alien Invasion Game

This project implements the Alien Invasion game, a space-themed arcade game developed using Pygame and FastAPI.

## Overview

This game involves controlling a spaceship to shoot down alien invaders. The game integrates Pygame for the graphical interface and FastAPI to provide additional functionalities via an API.

## Getting Started

### Prerequisites

Ensure the following are installed:
- Python 3.x
- Pygame
- FastAPI
- uvicorn

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/alien_invasion_game.git
   
# Usage

- Use arrow keys (←, →) to control the spaceship.
- Press the spacebar to shoot bullets at aliens.
- Access the API at [http://127.0.0.1:8000](http://127.0.0.1:8000) for game-related information.

# Game Components

- **main.py**: Controls the main game loop, integrating Pygame and FastAPI.
- **ship.py**: Manages the player's spaceship.
- **alien.py**: Handles the behavior of alien invaders.
- **settings.py**: Stores game settings and configurations.
- **game_stats.py**: Tracks and updates game statistics.
- **bullet.py**: Manages bullets fired from the player's ship.
- **main_api.py**: Defines FastAPI routes and endpoints.
- **scoreboard.py**: Displays game information such as score, high score, level, and remaining ships.
- **button.py**: Manages the creation and display of buttons within the game.

# Credits

This project was created by [Danial Askarov]. Contributions are welcome to enhance the game experience!
