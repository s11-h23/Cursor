#!/usr/bin/env python3
"""
Conway's Game of Life - Console Animation
==========================================

Rules:
1. Any live cell with 2-3 live neighbors survives
2. Any dead cell with exactly 3 live neighbors becomes alive
3. All other live cells die, all other dead cells stay dead
"""

import os
import time
import random
import sys
from typing import List, Tuple, Optional


class GameOfLife:
    def __init__(self, width: int = 80, height: int = 24):
        """Initialize the Game of Life grid."""
        self.width = width
        self.height = height
        self.grid = [[False for _ in range(width)] for _ in range(height)]
        self.generation = 0
    
    def clear_grid(self) -> None:
        """Clear all cells in the grid."""
        self.grid = [[False for _ in range(self.width)] for _ in range(self.height)]
        self.generation = 0
    
    def set_cell(self, x: int, y: int, alive: bool = True) -> None:
        """Set a cell's state."""
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[y][x] = alive
    
    def get_cell(self, x: int, y: int) -> bool:
        """Get a cell's state."""
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.grid[y][x]
        return False
    
    def count_neighbors(self, x: int, y: int) -> int:
        """Count live neighbors around a cell."""
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if self.get_cell(nx, ny):
                    count += 1
        return count
    
    def next_generation(self) -> None:
        """Evolve the grid to the next generation."""
        new_grid = [[False for _ in range(self.width)] for _ in range(self.height)]
        
        for y in range(self.height):
            for x in range(self.width):
                neighbors = self.count_neighbors(x, y)
                current_cell = self.grid[y][x]
                
                # Apply Game of Life rules
                if current_cell:  # Cell is alive
                    new_grid[y][x] = neighbors in [2, 3]
                else:  # Cell is dead
                    new_grid[y][x] = neighbors == 3
        
        self.grid = new_grid
        self.generation += 1
    
    def randomize(self, density: float = 0.3) -> None:
        """Randomly populate the grid."""
        self.clear_grid()
        for y in range(self.height):
            for x in range(self.width):
                self.grid[y][x] = random.random() < density
    
    def add_pattern(self, pattern: List[Tuple[int, int]], offset_x: int = 0, offset_y: int = 0) -> None:
        """Add a pattern to the grid at the specified offset."""
        for x, y in pattern:
            self.set_cell(x + offset_x, y + offset_y, True)
    
    def display(self) -> str:
        """Return a string representation of the grid."""
        lines = []
        lines.append("═" * (self.width + 2))
        for row in self.grid:
            line = "║" + "".join("██" if cell else "  " for cell in row) + "║"
            lines.append(line)
        lines.append("═" * (self.width + 2))
        lines.append(f"Generation: {self.generation}")
        return "\n".join(lines)
    
    def count_living_cells(self) -> int:
        """Count the number of living cells."""
        return sum(sum(row) for row in self.grid)


class GamePatterns:
    """Collection of interesting Game of Life patterns."""
    
    @staticmethod
    def glider() -> List[Tuple[int, int]]:
        """Classic glider pattern."""
        return [(1, 0), (2, 1), (0, 2), (1, 2), (2, 2)]
    
    @staticmethod
    def blinker() -> List[Tuple[int, int]]:
        """Simple oscillator."""
        return [(0, 1), (1, 1), (2, 1)]
    
    @staticmethod
    def block() -> List[Tuple[int, int]]:
        """Still life block."""
        return [(0, 0), (1, 0), (0, 1), (1, 1)]
    
    @staticmethod
    def beacon() -> List[Tuple[int, int]]:
        """Beacon oscillator."""
        return [(0, 0), (1, 0), (0, 1), (3, 2), (2, 3), (3, 3)]
    
    @staticmethod
    def toad() -> List[Tuple[int, int]]:
        """Toad oscillator."""
        return [(1, 0), (2, 0), (3, 0), (0, 1), (1, 1), (2, 1)]
    
    @staticmethod
    def glider_gun() -> List[Tuple[int, int]]:
        """Gosper glider gun (partial - simplified version)."""
        return [
            (24, 0), (22, 1), (24, 1), (12, 2), (13, 2), (20, 2), (21, 2), (34, 2), (35, 2),
            (11, 3), (15, 3), (20, 3), (21, 3), (34, 3), (35, 3), (0, 4), (1, 4), (10, 4),
            (16, 4), (20, 4), (21, 4), (0, 5), (1, 5), (10, 5), (14, 5), (16, 5), (17, 5),
            (22, 5), (24, 5), (10, 6), (16, 6), (24, 6), (11, 7), (15, 7), (12, 8), (13, 8)
        ]


def clear_screen():
    """Clear the console screen."""
    os.system('clear' if os.name == 'posix' else 'cls')


def main():
    """Main game loop."""
    # Get terminal size
    try:
        columns, rows = os.get_terminal_size()
        width = min(columns // 2 - 2, 80)  # Account for double-width characters
        height = min(rows - 5, 24)  # Leave space for UI
    except OSError:
        width, height = 40, 20
    
    game = GameOfLife(width, height)
    
    print("Conway's Game of Life")
    print("=" * 50)
    print("Choose initial pattern:")
    print("1. Random")
    print("2. Glider")
    print("3. Multiple patterns")
    print("4. Glider gun")
    print("5. Custom random density")
    
    try:
        choice = input("Enter choice (1-5, default 1): ").strip()
        if not choice:
            choice = "1"
        
        if choice == "1":
            game.randomize(0.3)
        elif choice == "2":
            game.add_pattern(GamePatterns.glider(), 5, 5)
        elif choice == "3":
            # Add multiple interesting patterns
            game.add_pattern(GamePatterns.glider(), 2, 2)
            game.add_pattern(GamePatterns.blinker(), 15, 8)
            game.add_pattern(GamePatterns.block(), 25, 5)
            game.add_pattern(GamePatterns.beacon(), 35, 10)
            game.add_pattern(GamePatterns.toad(), 10, 15)
        elif choice == "4":
            if width >= 40 and height >= 20:
                game.add_pattern(GamePatterns.glider_gun(), 2, 5)
            else:
                print("Terminal too small for glider gun, using random instead...")
                game.randomize(0.3)
        elif choice == "5":
            try:
                density = float(input("Enter density (0.0-1.0, default 0.3): ") or "0.3")
                density = max(0.0, min(1.0, density))
                game.randomize(density)
            except ValueError:
                game.randomize(0.3)
        else:
            game.randomize(0.3)
        
        print(f"\nStarting simulation... Press Ctrl+C to stop")
        time.sleep(2)
        
        # Animation loop
        while True:
            clear_screen()
            print(game.display())
            print(f"Living cells: {game.count_living_cells()}")
            print("Press Ctrl+C to stop")
            
            # Check for extinction
            if game.count_living_cells() == 0:
                print("\nAll cells died! Simulation ended.")
                break
            
            game.next_generation()
            time.sleep(0.2)  # Adjust speed here
            
    except KeyboardInterrupt:
        clear_screen()
        print(f"\nSimulation stopped at generation {game.generation}")
        print(f"Final living cells: {game.count_living_cells()}")
        print("Thanks for playing!")
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()