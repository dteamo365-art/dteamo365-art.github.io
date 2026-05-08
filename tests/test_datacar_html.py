import re
from pathlib import Path

HTML_FILE = Path(__file__).resolve().parents[1] / 'datacar.html'


def _load_html() -> str:
    return HTML_FILE.read_text(encoding='utf-8')


def test_anchor_targets_exist_and_are_unique():
    html = _load_html()

    ids = re.findall(r'id="([^"]+)"', html)
    assert ids, 'No id attributes found in datacar.html'

    duplicate_ids = sorted({value for value in ids if ids.count(value) > 1})
    assert not duplicate_ids, f'Duplicate ids found: {duplicate_ids}'

    href_targets = re.findall(r'href="#([^"]+)"', html)
    missing = sorted({target for target in href_targets if target not in ids})
    assert not missing, f'Anchor targets with no matching id: {missing}'
