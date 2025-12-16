import os

from selenium.webdriver.chrome.options import Options

from utils.convert import str2bool


class BrowserOptions(Options):
    def __init__(self):
        super().__init__()

        arguments = str(os.getenv('BROWSER_OPTIONS_CONFIG_ARGUMENTS')).split(',')
        for argument in arguments:
            print(argument)
            self.add_argument(str(argument))
            self.set_capability("browserName", str(os.environ.get("BROWSER_NAME_CONFIG")))

            is_use_selenium_grid = str2bool(os.getenv('IS_USE_SELENIUM_GRID'))
            is_use_browser_stack = str2bool(os.getenv('IS_USE_BROWSER_STACK'))
            if is_use_selenium_grid and is_use_browser_stack:
                self.set_capability('bstack:options', {
                    "os": os.getenv('REMOTEBROWSER_CONFIG_OS_NAME'),
                    "osVersion": os.getenv('REMOTEBROWSER_CONFIG_OS_VERSION'),
                    "browserVersion": os.getenv('REMOTEBROWSER_CONFIG_BROWSER_VERSION')
                })
