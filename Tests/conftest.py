

import pytest
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from utils.email_pytest_report import Email_Pytest_Report



driver = None

@pytest.fixture(scope="class")
def setup(request):
        global driver
        options = webdriver.ChromeOptions()
        # options.add_argument("headless")
        options.add_experimental_option("detach", True)
        chromepath = Service("C:/Users/DanielHasid/chromedriver.exe")
        driver = webdriver.Chrome(service=chromepath, options=options)
        driver.implicitly_wait(15)
        driver.maximize_window()
        driver.get("https://demo2.okoora.com")

        request.cls.driver = driver
        yield
        driver.close()

def email_pytest_report(request):
    "pytest fixture for device flag"
    return request.config.getoption("--email_pytest_report")

    # Command line options:
    # parser.addoption("--email_pytest_report",
    #                  dest="email_pytest_report",
    #                  help="Email pytest report: Y or N",
    #                  default="N")


def pytest_terminal_summary(terminalreporter, exitstatus = 0):
    "add additional section in terminal summary reporting."
    if not hasattr(terminalreporter.config,'workerinput'):
        if terminalreporter.config.getoption("–email_pytest_report").lower() == "y":
            email_obj = Email_Pytest_Report()
            # Send html formatted email body message with pytest report as an attachment
            email_obj.send_test_report_email(html_body_flag=True, attachment_flag=True, report_file_path='C:/Users/DanielHasid/PycharmProjects/Automation/Tests/pytest_report.html')






@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra



#
# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item):
#     outcome = yield
#     report = outcome.get_result()
#     extras = getattr(report, "extras", [])
#     if report.when == "call":
#         # always add url to report
#         extras.append(pytest_html.extras.url("http://www.example.com/"))
#         xfail = hasattr(report, "wasxfail")
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             # only add additional html on failure
#             extras.append(pytest_html.extras.html("<div>Additional HTML</div>"))
#         report.extras = extras
#
#
def _capture_screenshot(name):
    yield
    driver.get_screenshot_as_file(name)


# Contents of conftest.py


# Test arguments

# Contents of conftest.py

