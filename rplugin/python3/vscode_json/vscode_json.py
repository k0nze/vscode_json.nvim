import pynvim
import os

from pynvim import Nvim


@pynvim.plugin
class VSCodeJSON:
    def __init__(self, nvim: Nvim) -> None:
        self.nvim = nvim
        self.vscode_dir_path = None
        self.vscode_dir_exists()

        self.launch_json_path = None

    @pynvim.function("VSCodeJSONCheckDirExists")
    def vscode_dir_exists(self, _=None) -> bool:
        current_dir_path = self.nvim.command_output("pwd")
        vscode_dir_path = str(current_dir_path) + "/.vscode"

        if os.path.isdir(vscode_dir_path):
            self.vscode_dir_path = vscode_dir_path
            return True

        return False

    @pynvim.function("VSCodeJSONLaunchExists")
    def launch_json_exists(self, _=None) -> bool:
        if not self.vscode_dir_exists():
            return False

        launch_json_path = str(self.vscode_dir_path) + "/launch.json"

        if os.path.isfile(launch_json_path):
            self.launch_json_path = launch_json_path
            return True

        return False

    @pynvim.command("VSCodeJSONRun", nargs="0")
    def run(self, _):
        self.launch_json_exists()
        self.nvim.current.line = f"cwd: {self.launch_json_path}"
