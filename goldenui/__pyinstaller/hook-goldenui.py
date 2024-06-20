from pathlib import Path

import goldenui

goldenui_path = Path(goldenui.__file__).parent
datas = [(goldenui_path / "resources", "goldenui_res")]
