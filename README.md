🤹‍♀️ Running Instructions: 

Open CMD on your computer
then copy the folder path
and use the command 'cd /d <game folder path here>',
then write "python main.py".
if it gives an error: "pygame is not defined" or something like that, it means pygame is not installed.
to install pygame write "pip install pygame" 

Overall Game Structure

This code lays the foundation for a simple game where the player navigates a character to collect items while avoiding obstacles.
Key Parts:

**Imports**
* **os:** provides tools to interact with the operating system (finding file paths).
* **pygame:** a popular library for creating games and multimedia applications.
* **uuid:** used for generating unique identifiers for game objects.
* **math:** for calculations regarding movement or positioning.
* **enums.GameState:** a custom file defining different game states (e.g., MAIN, PLAY, PAUSE).
* **classes...:** custom classes defining the behavior of in-game entities.
* **functions...:** custom functions containing reusable logic.
  
**Classes**
* **App:** core game class which manages the game loop, handles game states, and coordinates different elements.
* **Player:** represents the player-controlled character.
* **Timer:** keeps track of game time.
* **Collectable:** represents different items the player can collect.

**Key Functions**

* **controls:** processes player input for movement and actions.
* **random_spawn:** generates random positions for spawning items.
* **collect_collectable:** handles collision detection and the effects of collecting items.
* **render\_...:** functions for drawing various elements on the screen.
* **draw\_...:** additional drawing utility functions.

**The 'App' Class**

* **__init__(self):**
   - sets up initial game variables like  `running`, `game_state`.
   - loads assets (sounds) using paths generated with the `os` module.
   - initializes timers, player object, and containers for collectables.

* **on_init(self):**
  -  initializes Pygame, sets the window title, creates the display surface.
  -  starts the background music (`bgm`).

* **on_event(self, event):**
  -  handles events like keyboard presses, mouse clicks, and the closing of the window.
  -  calls the `controls` function to process player input.

* **on_loop(self):**
  -  the core game logic runs here, but only when `game_state` is set to 'PLAY'.
  -  manages background music.
  -  tracks game time using the timer.
  -  decreases player energy over time.
  -  spawns Collectables (`staggs` and `sambuccas`) at timed intervals.
  -  calls `collect_collectable` to check for collection events.

* **on_render(self):**
  -  calls various rendering functions to draw:
     - the main menu or play area, depending on the `game_state`.
     - a virtual 'gamepad' (directional controls).
     - debug text.

* **on_cleanup(self):**
  -  cleans up Pygame resources before the game quits.


🦸‍♀️Gameplay Scenarios

* **Main Menu:**  the game starts with a simple menu and the `game_state` would be 'MAIN' at this point.
* **Gameplay:** when the player starts, the `game_state` switches to 'PLAY'. user controls a character to move around.
* **Score/Energy:** the player could have an energy bar that decreases over time. collecting 'Stagg' items might increase energy, while 'Sambucca' items might decrease it.
* **Timed Challenge:** the timer could indicate a time limit for collecting items or achieving a goal.

**General Improvements**

1. **Comments and Docstrings:**  add explanatory comments within the code, especially for complex logic or non-obvious interactions. Use docstrings in classes and functions to outline their purpose and parameters.

2. **Descriptive Naming:** use more meaningful names for variables and functions. For example, instead of `sp`, you could use `spawn_position`.

3. **Code Restructure:** break down large functions into smaller, focused functions to improve readability and maintainability.

4. **Object-Oriented Design:** consider how to better leverage the principles of OOP. Refactor elements of the game logic into more cohesive classes? This might offer advantages for organization and extending the game later.

**Specific Optimization Points**

1. **Spawn Logic:** the spawning of 'Stagg' and 'Sambucca' items could use a more unified approach for efficiency and maintainability. Consider a single function with parameters to control spawnable item types and spawn rates.

2. **Collision Detection:** the `collect_collectable` function is likely where collision detection is handled. Use an efficient collision detection method suitable for game's collision complexity (e.g., simple rectangle checks vs. more precise methods).

3. **Rendering Optimization:** depending on how many elements are being drawn, rendering could become a bottleneck. Look into Pygame's `Sprite` class or rendering optimizations related to:
   - **Dirty Rects:** only updating portions of the screen that have changed.
   - **Batching Draw Calls:** reducing the number of individual calls to drawing functions.

**New Feature Ideas**

1. **Difficulty Progression:** the game could become progressively harder over time by increasing spawn rates of negative items, decreasing spawn rates of positive items, or even introducing new obstacle types.

2. **Power-Ups:** add special power-ups that give the player temporary abilities (e.g., speed boost, invincibility e.g., super mario from the 90s 😊).

3. **Levels:** implement a system to advance through multiple levels with varied layouts and challenges.

4. **High Scores:** store and display player high scores to add a competitive element.

**Debugging and Testing**

1. **Debug Mode:** improve the `debug_string` and `debug_string_2` to have more valuable information about the game state during development.

2. **Unit Tests:** consider writing unit tests (especially to refactor code into smaller functions) to ensure changes don't break existing functionality.


