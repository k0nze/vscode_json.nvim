from enum import Enum, unique
from typing import List


@unique
class LaunchConfigurationType(Enum):
    PYTHON = "python"


@unique
class LaunchConfigurationRequest(Enum):
    LAUNCH = "launch"


class LaunchConfiguration:
    def __init__(
        self,
        name: str,
        type: LaunchConfigurationType,
        request: LaunchConfigurationRequest,
        module: str,
        args: List[str],
    ):
        self.name = name
        self.type = type
        self.request = request
        self.module = module
        self.args = args
