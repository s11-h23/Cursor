#!/usr/bin/env python3
"""
Game of Life Demo - Automatic Animation
=======================================
This script runs the Game of Life with different patterns automatically.
"""

import os
import time
from game_of_life import GameOfLife, GamePatterns, clear_screen


def demo_pattern(game, pattern_func, pattern_name, duration=10):
    """Demo a specific pattern."""
    game.clear_grid()
    
    if pattern_name == "Multiple Patterns":
        # Add multiple patterns
        game.add_pattern(GamePatterns.glider(), 2, 2)
        game.add_pattern(GamePatterns.blinker(), 15, 8)
        game.add_pattern(GamePatterns.block(), 25, 5)
        game.add_pattern(GamePatterns.beacon(), 35, 10)
        game.add_pattern(GamePatterns.toad(), 10, 15)
    elif pattern_name == "Random":
        game.randomize(0.25)
    else:
        pattern = pattern_func()
        # Center the pattern
        offset_x = game.width // 2 - 5
        offset_y = game.height // 2 - 5
        game.add_pattern(pattern, offset_x, offset_y)
    
    print(f"\n=== Demonstrating: {pattern_name} ===")
    time.sleep(2)
    
    start_time = time.time()
    while time.time() - start_time < duration:
        clear_screen()
        print(f"=== {pattern_name} ===")
        print(game.display())
        print(f"Living cells: {game.count_living_cells()}")
        print(f"Time remaining: {duration - int(time.time() - start_time)}s")
        
        if game.count_living_cells() == 0:
            print("Pattern died out!")
            time.sleep(2)
            break
            
        game.next_generation()
        time.sleep(0.3)


def main():
    """Run the demo."""
    # Get terminal size
    try:
        columns, rows = os.get_terminal_size()
        width = min(columns // 2 - 2, 60)
        height = min(rows - 5, 20)
    except OSError:
        width, height = 30, 15
    
    game = GameOfLife(width, height)
    
    print("Conway's Game of Life - Automatic Demo")
    print("=" * 50)
    print("This demo will show different patterns automatically.")
    print("Press Ctrl+C to stop at any time.")
    time.sleep(3)
    
    patterns = [
        (GamePatterns.glider, "Glider"),
        (GamePatterns.blinker, "Blinker"),
        (GamePatterns.beacon, "Beacon"),
        (GamePatterns.toad, "Toad"),
        (None, "Multiple Patterns"),
        (None, "Random")
    ]
    
    try:
        for pattern_func, name in patterns:
            demo_pattern(game, pattern_func, name, duration=15)
            time.sleep(2)
        
        clear_screen()
        print("Demo completed! Thanks for watching!")
        
    except KeyboardInterrupt:
        clear_screen()
        print("Demo stopped. Thanks for watching!")


if __name__ == "__main__":
    main()