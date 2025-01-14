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

        # update default config with lua setup
        self.config_from_lua()

        # read .vscode/launch.json if it exists
        self.read_launch_json()

    def config_from_lua(self):
        self.config = {"selection_buffer_pos": "top"}

        # fetch lua config from lua/vscode_json.lua
        config = self.nvim.exec_lua("return require('vscode_json').getConfig()")

        self.config.update(config)

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
            self.launch_json.check_for_change()

            # list all launch configuration names in a scratch buffer in a split
            configuration_names = list(self.launch_json.configurations.keys())

            if self.config["selection_buffer_pos"] == "bottom":
                self.nvim.api.command("botright split")
            else:
                self.nvim.api.command("split")

            # resize scratch buffer to the size of available configurations
            self.nvim.api.command(f"resize {len(configuration_names)}")
            self.nvim.api.command("wincmd l")

            scratch_buffer = self.nvim.api.create_buf(True, True)
            self.nvim.api.set_current_buf(scratch_buffer)

            # print all launch configuration names in scratch buffer
            self.nvim.api.buf_set_lines(
                scratch_buffer,
                0,
                -1,
                False,
                configuration_names,
            )

            # highlight current line
            self.nvim.api.command("setlocal cursorline")

            # rename scratch buffer
            self.nvim.api.command(
                f"file VSCode launch configurations from: {self.launch_json_path}"
            )

            # remap enter in scratch buffer to call VSCodeJSONSelectLaunchConfiguration and close buffer
            self.nvim.api.command(
                "nnoremap <buffer> <CR> :call VSCodeJSONSelectLaunchConfiguration(getline('.'))<CR>:q!<CR>"
            )

    @pynvim.function("VSCodeJSONSelectLaunchConfiguration")
    def test(self, args) -> None:
        # check if args has one element
        if len(args) == 1:
            self.launch_json.select_configuration(args[0])

    @pynvim.command("VSCodeJSONRun", nargs="0")
    def run(self, _):
        if self.launch_json is not None:
            self.launch_json.check_for_change()
            self.nvim.api.command(
                f'TermExec cmd="{self.launch_json.get_selected_configuration_run_command()}"'
            )
