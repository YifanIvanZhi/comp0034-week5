from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from dash.testing.application_runners import import_app


def test_papa001_h1textequals(dash_duo):
    """
    GIVEN the app is running
    WHEN the home page is available
    THEN the H1 heading element shouldp include the text 'Paralympic History' (case insensitive)
    """
    app = import_app(app_file="paralympics_app.paralympics_dash_app")
    dash_duo.start_server(app)
    # dash_duo.driver.maximize_window()
    dash_duo.wait_for_element("h1", timeout=4)
    h1_text = dash_duo.find_element("h1").text
    assert h1_text.casefold() == "Paralympic History".casefold()


def test_papa002_dropdown_changes_chart(dash_duo):
    """
    GIVEN the Dashboard page has loaded
    WHEN the value Athletes is selected from the dropdown with the id 'type-dropdown'
    THEN the chart with the id `line-chart-time` should change so that the title includes the words 'participants'
    """
    app = import_app(app_file="paralympics_app.paralympics_dash_app")
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#type-dropdown", timeout=4)
    dropdown_input = dash_duo.find_element("#type-dropdown input")
    dropdown_input.send_keys("Athletes")
    dropdown_input.send_keys(Keys.RETURN)
    dash_duo.wait_for_element("#line-sports", timeout=None)
    graph_title = dash_duo.find_element(
        "#line-sports > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > svg:nth-child(3) > g:nth-child("
        "4) > g:nth-child(2) > text:nth-child(1)"
    )
    assert (
        "participants" in graph_title.text
    ), "'participants' should appear in the chart title"


def test_papa003_charts_hidden_when_unselected(dash_duo):
    """
    GIVEN the Dashboard page has loaded
    WHEN both the Winter and Summer options in the checklist with the id 'mf-ratio-checklist' are unselected
    THEN the divs with the ids of 'stacked-bar-gender-win' and 'stacked-bar-gender-sum' should have a
    `style="display: none"' attribute
    """
    app = import_app(app_file="paralympics_app.paralympics_dash_app")
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#mf-ratio-checklist", timeout=4)
    WebDriverWait(dash_duo.driver, 3).until(
        EC.element_located_to_be_selected(
            (
                By.CSS_SELECTOR,
                "#mf-ratio-checklist > "
                "label:nth-child(1) > "
                "input:nth-child(1)",
            )
        )
    )
    checkboxes = dash_duo.find_elements("#mf-ratio-checklist input")
    for c in checkboxes:
        # selenium click() method failed, used guidance here
        # https://stackoverflow.com/questions/46253566/selenium-cant-click-specific-checkbox and converted from Java
        # to Python as below
        dash_duo.driver.execute_script("arguments[0].click();", c)
    display_attribute_w = dash_duo.find_element(
        "#stacked-bar-gender-win"
    ).value_of_css_property("display")
    display_attribute_s = dash_duo.find_element(
        "#stacked-bar-gender-sum"
    ).value_of_css_property("display")
    assert display_attribute_w == "none"
    assert display_attribute_s == "none"


def test_papa001_table_heading_displayed(dash_duo):
    """
    GIVEN the Dashboard page has loaded
    WHEN the gold medals table with id 'table-top-ten-gold-dash' is displayed
    THEN the text value of the table heading (<th>) in the first column should be 'Country'
    """
    app = import_app(app_file="paralympics_app.paralympics_dash_app")
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#table-top-ten-gold-dash", timeout=4)
    th_col1_text = dash_duo.find_element(
        "th.dash-header:nth-child(1) > div:nth-child(1) > span:nth-child(2)"
    )
    assert th_col1_text.text == "Country"
