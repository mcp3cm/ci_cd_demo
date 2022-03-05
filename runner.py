import pytest

class Plugin:
    def __init__(self):
        self.passed_tests = set()
        self.failed_tests = set()

    def pytest_runtest_logreport(self, report):
        print('here')
        if report.passed:
            self.passed_tests.add(report.nodeid)
        else:
            self.failed_tests.add(report.nodeid)
    
    def score(self):
        print(f'Got {len(self.passed_tests)} right and {len(self.failed_tests)} wrong.')
        print(f'{(len(self.passed_tests)*100/(len(self.failed_tests)+len(self.passed_tests)))}')

plugin = Plugin()
pytest.main(['.', '-p', 'no:terminal'], plugins=[plugin])

plugin.score()