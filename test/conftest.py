from selenium.webdriver.chrome.options import Options


# See https://community.plotly.com/t/dash-integration-testing-with-selenium-and-github-actions/43602
def pytest_setup_options():
    """Pytest setup options for the Chromedriver when using Selenium.

    Note: this is not a fixture!"""
    options = Options()
    # Uncomment the following if testing on GitHub actions
    # the browser needs to run in headless mode
    # options.add_argument("--disable-gpu")
    # options.add_argument("--headless")
    options.add_argument("--start-maximized")
    return options
