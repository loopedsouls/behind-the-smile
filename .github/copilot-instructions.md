# Behind the Smile - AI Coding Guidelines

## Project Overview
This is a Ren'Py visual novel game implementing a horror psychological simulation. Players manage a convenience store employee who must wear a smile mask to hide from monstrous customers while handling bureaucratic tasks. The game combines visual novel elements with real-time simulation mechanics.

## Architecture
- **Engine**: Ren'Py (Python + Ren'Py script language)
- **Structure**: 
  - `script.rpy`: Main game flow, labels, and Python functions
  - `variables.rpy`: Game configuration, customer/danger types, and state variables
  - `screens_custom.rpy`: UI screens and game logic updates
  - `gui.rpy`: Interface styling with dystopian theme
- **Game Loop**: Timer-driven updates in `game_hud` screen calling `update_game_logic()`

## Key Patterns
- **State Management**: Use `store.` variables for global state (e.g., `store.game_state`, `store.mask_on`)
- **Screen Logic**: Custom screens handle both UI and game updates via timers
- **Customer System**: Random spawning based on rarity/severity with patience timers
- **Mask Mechanics**: Toggle `mask_on` state affects visibility and triggers events

## Development Workflow
- **Lint**: `python -m renpy lint game` (fix syntax errors like invalid `cps` parameter in text statements)
- **Run**: `python -m renpy .` from project root
- **Build**: Configure in `project.json` for PC/Web export
- **Debug**: Check `errors.txt`, `log.txt` for runtime issues

## Code Conventions
- **Python Blocks**: Use `init python:` for setup, functions in screens for updates
- **Text Tags**: Use `{cps=25}text{/cps}` for typewriter effects, not `cps` parameter
- **Screen Syntax**: Define UIs in `screen` blocks with proper indentation
- **Variable Defaults**: Declare with `default` for persistent state
- **Imports**: Access via `store.` or import in `init python`

## Common Fixes
- Replace `text "line" cps 25` with `text "{cps=25}line{/cps}"`
- Ensure timer actions call functions correctly (e.g., `Function(update_game_logic)`)
- Use absolute paths for assets in `images/` directory

## Key Files to Reference
- [game/script.rpy](game/script.rpy): Game flow and core functions
- [game/variables.rpy](game/variables.rpy): Configuration and data structures
- [game/screens_custom.rpy](game/screens_custom.rpy): UI and game logic
- [README.md](README.md): Game design and mechanics overview