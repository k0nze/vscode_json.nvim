import pynvim

@pynvim.plugin
class VSCodeJSON(object):

    def __init__(self, nvim):
        self.nvim = nvim


    @pynvim.command('VSCodeJSONRun', nargs='0')
    def run(self, _):
        self.nvim.current.line = "Hello"
