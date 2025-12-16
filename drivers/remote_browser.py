import os

from selenium import webdriver

from utils.convert import str2bool


class RemoteBrowser(webdriver.Remote):
    def __init__(self, options):
        is_use_selenium_grid = str2bool(os.getenv('IS_USE_SELENIUM_GRID'))
        is_use_browser_stack = str2bool(os.getenv('IS_USE_BROWSER_STACK'))

        command_executor = str(os.getenv('SELENIUM_GRID_K8S_CONFIG_URL'))
        if is_use_selenium_grid and is_use_browser_stack:
            command_executor = str(os.getenv('REMOTEBROWSER_CONFIG_SELENIUM_GRID_URL'))

        print(command_executor)
        super().__init__(command_executor=command_executor, options=options)
