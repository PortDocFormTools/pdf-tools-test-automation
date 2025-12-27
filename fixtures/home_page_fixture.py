import pytest


@pytest.fixture
def home_page_data():
    return {
        "title": "PDF Tools",
        "header": "PDF Tools",
        "description": "Online PDF editor",
        "cards-titles": {
            "compress": "Compress PDF",
            "merge": "Merge PDF",
            "split": "Split PDF",
        }
    }
