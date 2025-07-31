# Conway's Game of Life - Console Animation

A Python implementation of Conway's Game of Life with animated console output.

## Features

- **Animated Console Display**: Watch the evolution in real-time with smooth console animation
- **Multiple Patterns**: Choose from classic patterns like gliders, oscillators, and more
- **Adaptive Terminal Size**: Automatically adjusts to your terminal dimensions
- **Interactive Controls**: Choose initial patterns and control the simulation
- **Pattern Library**: Includes famous patterns like the Gosper Glider Gun

## Game Rules

Conway's Game of Life follows these simple rules:

1. **Survival**: Any live cell with 2-3 live neighbors survives
2. **Birth**: Any dead cell with exactly 3 live neighbors becomes alive  
3. **Death**: All other live cells die, all other dead cells stay dead

## Usage

### Interactive Mode

Run the main script for an interactive experience:

```bash
python3 game_of_life.py
```

Choose from these initial patterns:
1. **Random** - Randomly populated grid
2. **Glider** - Classic moving pattern
3. **Multiple patterns** - Various interesting patterns at once
4. **Glider gun** - Pattern that generates gliders (requires larger terminal)
5. **Custom random density** - Specify your own randomization density

### Demo Mode

Run the automatic demo to see different patterns:

```bash
python3 demo.py
```

This will automatically cycle through different patterns, showing:
- Glider (moves diagonally)
- Blinker (simple oscillator)
- Beacon (period-2 oscillator)
- Toad (period-2 oscillator)
- Multiple patterns simultaneously
- Random configurations

## Controls

- **Ctrl+C**: Stop the simulation at any time
- The simulation will automatically stop if all cells die

## Requirements

- Python 3.6+
- Works on Linux, macOS, and Windows
- No external dependencies required

## Pattern Details

### Included Patterns

- **Glider**: A 5-cell pattern that moves diagonally across the grid
- **Blinker**: A 3-cell oscillator with period 2
- **Block**: A stable 4-cell still life
- **Beacon**: A 6-cell oscillator with period 2
- **Toad**: A 6-cell oscillator with period 2
- **Glider Gun**: Generates gliders continuously (simplified version)

## Technical Details

The implementation uses:
- Double-width Unicode characters (██) for better visibility
- Terminal size detection for optimal display
- Efficient neighbor counting algorithm
- Clean object-oriented design with separate pattern library

## Customization

You can easily add new patterns by extending the `GamePatterns` class:

```python
@staticmethod
def my_pattern() -> List[Tuple[int, int]]:
    """My custom pattern."""
    return [(0, 0), (1, 0), (2, 0)]  # Three cells in a row
```

Adjust animation speed by changing the `time.sleep()` value in the main loop. 
