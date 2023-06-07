# VS Code JSON interpreter for neovim

Switching from VS Code to Neovim has perks and pitfalls, mainly when your collaborators stick to VS Code and its project settings. The `.vscode/launch.json` is handy when you want to run your project with different input arguments and share those configurations with others. This plugin tries to bridge this gap by providing a parser for `.vscode/launch.json` files and letting you select and run the configurations listed in it.

## Limitation

Currently this plugin only supports running Python modules (no debugging).

## Installation

Python:
```bash
python3 -m pip install pynvim
```

packer:
```lua
 use({
    'k0nze/vscode_json.nvim',
     requires = {
        {"akinsho/toggleterm.nvim"}
     },
     run=':UpdateRemotePlugins'
 })
```

## Configuration

lua:
```lua
require('k0nze/vscode_json.nvim').setup({
    selection_buffer_pos = "bottom" -- "top" | "bottom" where will the buffer to select the launch configuration be opened
})
```

## Usage

### Functions and Commands

- `:call VSCodeJSONReadLaunch()` reads the `.vscode/launch.json` at the location `nvim` was opened at (is executed when opening `nvim`).
- `:call VSCodeJSONListLaunchConfigurations()` opens a scratch buffer which allows you to select a launch configuration from `.vscode/launch.json`.
- `:VSCodeJSONRun` opens a new embedded terminal with [akinsho/toggleterm.nvim](https://github.com/akinsho/toggleterm.nvim) and runs the selected launch configuration.

## Development

```
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
pre-commit install
```

## Credits

Based on [pynvimExample](https://github.com/jeff-dh/pynvimExample) by [@jeff-dh](https://github.com/jeff-dh)

## TODOs
- [ ] re-read .vscode/launch.json on change
