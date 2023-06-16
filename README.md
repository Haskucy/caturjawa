# Javanese Chess (Catur Jawa)

Javanese Chess, also known as Catur Jawa, is a traditional game that hails from Indonesia. This game is popular among many Indonesian communities, particularly on the island of Java. The game is played on a 3x3 grid board and can be enjoyed by two players.

Each player starts the game with three pieces, which are placed horizontally on the board. Players take turns moving one piece at a time, with the objective of arranging their pieces horizontally, vertically, or diagonally before the other player. A win can also be achieved horizontally as long as the horizontal arrangement is different from the initial position.

This repository contains a website implementation of the game, an AI that can play the game, and an analysis of the game. The website allows for players to play the game online and the AI allows for playing against the computer. The analysis will give an insight of the game and its strategy. The goal of this project is to provide an interactive and educational experience for players to learn and enjoy Javanese Chess.

## Game Implementation Website
- TODO: Create Game Implementation Website
- WIP implementation code pen: https://codepen.io/haskucy/pen/GRwoxaR

## AI
- TODO: Create AI

## Analysis

In this analysis, we investigate the game state tree size of "Catur Jawa" using Depth-First Search (DFS), Breadth-First Search (BFS), and Random Play Sampling methodologies. The game state tree for "Catur Jawa" was found to be considerably large and complex.

### Estimation with DFS and BFS
- Estimated game state tree size using DFS: ${10}^{348}$ nodes.
- Upper bound estimation for the game tree size: ${10}^{753}$ nodes (using the maximum number of possible moves and maximum depth).
- More reasonable upper bound estimation: ${10}^{361}$ nodes (considering average branching factor with maximum depth).
- BFS was used for shallow node observations, with the maximum depth found in the first 1 million nodes in BFS search is to be 13.
- DFS may lead to biased depth measurements in certain situations, hence the need for an alternative approach.

### Estimation with Random Play Sampling
Random Play Sampling was used as a more balanced and feasible approach, yielding the following results:

- Number of games played: 100,000
- Average game depth: 51.351
- Maximum depth observed: 460
- Minimum depth observed: 6
- Average number of possible moves: 3.219
- Estimated game state tree size using Random Play Sampling: ${10}^{26}$ nodes.
- Upper bound estimation using Random Play Sampling: ${10}^{388}$ nodes (max branching factor raised to max depth achieved).

Game Outcomes:

| Player | Win Percentage | Lose Percentage | Draw Percentage |
|--------|----------------|-----------------|-----------------|
|   X    |    56.229%     |     35.432%     |     8.339%      |
|   O    |    35.432%     |     56.229%     |     8.339%      |

Player X, the first player, seems to have an advantage with win rates about 10% higher than player O.

Random Play Sampling is deemed a reasonable estimation approach despite its potential inability to capture the entire breadth of the game's complexity, given the impracticality of fully constructing the game state tree.

