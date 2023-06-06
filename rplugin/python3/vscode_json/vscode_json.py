import pynvim

from pynvim import Nvim


@pynvim.plugin
class VSCodeJSON:
    def __init__(self, nvim: Nvim) -> None:
        self.nvim = nvim

    @pynvim.command("VSCodeJSONRun", nargs=0)
    def run(self, _):
        self.nvim.current.line = "Hello"
