from pathlib import Path
from typing import Optional

from pinaxai.tools import Toolkit
from pinaxai.tools.duckduckgo import DuckDuckGoTools
from pinaxai.tools.file import FileTools
from pinaxai.tools.shell import ShellTools

cwd = Path(__file__).parent.resolve()
tmp_dir = cwd.joinpath("tmp")
tmp_dir.mkdir(exist_ok=True, parents=True)


def get_toolkit(tool_name: str) -> Optional[Toolkit]:
    if tool_name == "ddg_search":
        return DuckDuckGoTools(fixed_max_results=3)
    elif tool_name == "shell_tools":
        return ShellTools()
    elif tool_name == "file_tools":
        return FileTools(base_dir=cwd)

    return None
