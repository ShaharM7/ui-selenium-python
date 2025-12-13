from abc import ABC, abstractmethod

from selenium.webdriver.remote.webdriver import BaseWebDriver

from drivers.awaiter import Awaiter


class AbstractPage(ABC):
    @abstractmethod
    def __init__(self, browser: BaseWebDriver, awaiter: Awaiter):
        self.browser = browser
        self.awaiter = awaiter
