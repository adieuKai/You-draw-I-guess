# 项目根目录
from pathlib import Path

from src.server.utils.logger import log

BASE_DIR = Path(__file__).parent.parent
BANNER_FILE = BASE_DIR / 'banner.txt'

def worship() -> None:
    """
    获取项目启动Banner（优先读取 banner.txt）
    """
    if BANNER_FILE.exists():
        banner = BANNER_FILE.read_text(encoding='utf-8')
        banner = f"当前运行环境: \n{banner}"
        log.info(banner)