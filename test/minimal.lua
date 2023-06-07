-- function that returns the diretory path to the current lua script
function plugin_path()
    local str = debug.getinfo(2, "S").source:sub(2)
    str = str:match("(.*/)")
    local r_str = string.reverse(str)
    r_str = string.gsub(r_str, "/tset/", "", 1)
    str = string.reverse(r_str)
    return str
end

-- ignore default config and plugins
vim.opt.runtimepath:remove(vim.fn.expand('~/.config/nvim'))
vim.opt.packpath:remove(vim.fn.expand('~/.local/share/nvim/site'))

-- append test directory
local test_dir = '/tmp/nvim-config'
vim.opt.runtimepath:append(vim.fn.expand(test_dir))
vim.opt.packpath:append(vim.fn.expand(test_dir))

-- install packer
local install_path = test_dir .. '/pack/packer/start/packer.nvim'
local install_plugins = false

if vim.fn.empty(vim.fn.glob(install_path)) > 0 then
    vim.cmd('!git clone https://github.com/wbthomason/packer.nvim ' .. install_path)
    vim.cmd('packadd packer.nvim')
    install_plugins = true
end

local packer = require('packer')

packer.init({
    package_root = test_dir .. '/pack',
    compile_path = test_dir .. '/plugin/packer_compiled.lua'
})

packer.startup(function(use)
    -- Packer can manage itself
    use('wbthomason/packer.nvim')

    use({plugin_path(), requires = {
        {"akinsho/toggleterm.nvim"}
    }, run=":UpdateRemotePlugins"})

    if install_plugins then
        packer.sync()
    end
end)

-- set leader key
vim.g.mapleader = " "

local status, vscode_json = pcall(require, "vscode_json")
if not status then
    return
end

vscode_json.setup({
    selection_buffer_pos = "bottom"
})

-- select launch configuration
vim.keymap.set("n", "<leader>s", ":call VSCodeJSONListLaunchConfigurations()<CR>")

-- run selected launch configuration
vim.keymap.set("n", "<leader>r", ":VSCodeJSONRun<CR>")

vim.keymap.set("n", "<leader>t", ":ToggleTerm<CR>")

-- TODO autocmd on change .vscode dir trigger re-reading of .vscode
