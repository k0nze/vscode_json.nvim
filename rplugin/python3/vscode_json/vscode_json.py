import pynvim
import os

from pynvim import Nvim


@pynvim.plugin
class VSCodeJSON:
    def __init__(self, nvim: Nvim) -> None:
        self.nvim = nvim
        self.vscode_dir_path = None

        self.check_dir_exists(None)

    @pynvim.function("VSCodeJSONCheckDirExists")
    def check_dir_exists(self, _) -> None:
        current_dir_path = self.nvim.command_output("pwd")
        vscode_dir_path = str(current_dir_path) + "/.vscode"

        if os.path.isdir(vscode_dir_path):
            self.vscode_dir_path = vscode_dir_path

    @pynvim.command("VSCodeJSONRun", nargs="0")
    def run(self, _):
        self.nvim.current.line = f"cwd: {self.vscode_dir_path}"
