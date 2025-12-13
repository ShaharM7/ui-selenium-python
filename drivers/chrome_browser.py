from selenium import webdriver


class ChromeBrowser(webdriver.Chrome):
    """
    A custom Chrome browser driver wrapper.

    Args:
        options (webdriver.ChromeOptions): ChromeOptions instance specifying browser configuration.
    """
    def __init__(self, options: webdriver.ChromeOptions):
        super().__init__(options=options)
