PLAYWRIGHT_OPTIONS = {
    "headless": False,
    "slow_mo": 50,
    "browser_type": "chromium",
    "viewport": {"width": 1920, "height": 1080}
}

BASE_URL = ""
COMPRESS_URL = f"{BASE_URL}/pages/compress.html"
MERGE_URL = f"{BASE_URL}/pages/merge.html"
SPLIT_URL = f"{BASE_URL}/pages/split.html"