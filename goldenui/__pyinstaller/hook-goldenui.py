# "Hook" file for PyInstaller to easily pack the library with its resources.

from pathlib import Path

import goldenui

goldenui_path = Path(goldenui.__file__).parent

datas = [
    (goldenui_path / "resources" / "buttons", "goldenui_res/buttons"),
]
