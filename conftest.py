import pytest


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chromium")


@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")


def pytest_runtest_makereport(item, call):
    if not item.rep_call.failed:
        return
    with open("BUGS.md", "a") as bug_file:
        bug_file.write(f"{item.nodeid} - {item.rep_call.outcome}\n")


pytest_plugins = [
    'fixtures.page'
]
