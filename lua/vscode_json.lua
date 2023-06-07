--[[
This is a dummy config buffer for a pynvim rplugin module.

The lua init scripts can set the config like a regular lua plugin:
    (require('vscode_json').setup(config_table))

The pynvim rplugin module can fetch the config like this:
        self.nvim.exec_lua('return require("vscode_json").getConfig()')
--]]

local config = {}

local function setup(c)
    require("toggleterm").setup()
    config = c
end

local function getConfig()
    return config
end

return {setup = setup, getConfig = getConfig}
