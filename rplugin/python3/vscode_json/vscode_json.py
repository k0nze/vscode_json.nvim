import pynvim
import os

from pynvim import Nvim
from .launch_json import LaunchJSON


@pynvim.plugin
class VSCodeJSON:
    def __init__(self, nvim: Nvim) -> None:
        self.nvim = nvim
        self.vscode_dir_path = None
        self.vscode_dir_exists()

        self.launch_json_path = None
        self.launch_json = None

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

    @pynvim.function("VSCodeJSONReadLaunch")
    def read_launch_json(self, _=None) -> None:
        if self.launch_json_exists():
            self.launch_json = LaunchJSON(str(self.launch_json_path))

    @pynvim.function("VSCodeJSONListLaunchConfigurations")
    def list_launch_json_configurations(self, _=None) -> None:
        if self.launch_json is not None:
            # list all launch configuration names in a scratch buffer in a split
            self.nvim.api.command("split")
            self.nvim.api.command("wincmd l")
            buffer = self.nvim.api.create_buf(True, True)
            self.nvim.api.set_current_buf(buffer)

            self.nvim.api.buf_set_lines(
                buffer, 0, -1, False, list(self.launch_json.configurations.keys())
            )

    @pynvim.command("VSCodeJSONRun", nargs="0")
    def run(self, _):
        self.launch_json_exists()
        self.nvim.current.line = f"cwd: {self.launch_json_path}"
