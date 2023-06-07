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

require('vscode_json').setup({
    selection_buffer_pos = "bottom"
})

-- read .vscode/ at startup
vim.api.nvim_create_autocmd({"VimEnter"}, {
    pattern = {"*"},
    callback = function() print("test") end
})
