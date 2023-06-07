# VS Code JSON interpreter for neovim

Work in Progress

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
require('k0nze/vscode_json.nvim').setup()
```

## Usage

Work in Progress

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
