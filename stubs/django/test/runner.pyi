# Stubs for django.test.runner (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
import unittest

tblib = ...  # type: Any

class DebugSQLTextTestResult(unittest.TextTestResult):
    logger = ...  # type: Any
    def __init__(self, stream, descriptions, verbosity) -> None: ...
    debug_sql_stream = ...  # type: Any
    handler = ...  # type: Any
    def startTest(self, test): ...
    def stopTest(self, test): ...
    def addError(self, test, err): ...
    def addFailure(self, test, err): ...
    def printErrorList(self, flavour, errors): ...

class RemoteTestResult:
    events = ...  # type: Any
    failfast = ...  # type: bool
    shouldStop = ...  # type: bool
    testsRun = ...  # type: int
    def __init__(self) -> None: ...
    @property
    def test_index(self): ...
    def check_picklable(self, test, err): ...
    def stop_if_failfast(self): ...
    def stop(self): ...
    def startTestRun(self): ...
    def stopTestRun(self): ...
    def startTest(self, test): ...
    def stopTest(self, test): ...
    def addError(self, test, err): ...
    def addFailure(self, test, err): ...
    def addSubTest(self, test, subtest, err): ...
    def addSuccess(self, test): ...
    def addSkip(self, test, reason): ...
    def addExpectedFailure(self, test, err): ...
    def addUnexpectedSuccess(self, test): ...

class RemoteTestRunner:
    resultclass = ...  # type: Any
    failfast = ...  # type: Any
    def __init__(self, failfast: bool = ..., resultclass: Optional[Any] = ...) -> None: ...
    def run(self, test): ...

def default_test_processes(): ...

class ParallelTestSuite(unittest.TestSuite):
    init_worker = ...  # type: Any
    run_subsuite = ...  # type: Any
    subsuites = ...  # type: Any
    processes = ...  # type: Any
    failfast = ...  # type: Any
    def __init__(self, suite, processes, failfast: bool = ...) -> None: ...
    def run(self, result): ...

class DiscoverRunner:
    test_suite = ...  # type: Any
    parallel_test_suite = ...  # type: Any
    test_runner = ...  # type: Any
    test_loader = ...  # type: Any
    reorder_by = ...  # type: Any
    pattern = ...  # type: Any
    top_level = ...  # type: Any
    verbosity = ...  # type: Any
    interactive = ...  # type: Any
    failfast = ...  # type: Any
    keepdb = ...  # type: Any
    reverse = ...  # type: Any
    debug_sql = ...  # type: Any
    parallel = ...  # type: Any
    def __init__(self, pattern: Optional[Any] = ..., top_level: Optional[Any] = ..., verbosity: int = ..., interactive: bool = ..., failfast: bool = ..., keepdb: bool = ..., reverse: bool = ..., debug_sql: bool = ..., parallel: int = ..., **kwargs) -> None: ...
    @classmethod
    def add_arguments(cls, parser): ...
    def setup_test_environment(self, **kwargs): ...
    def build_suite(self, test_labels: Optional[Any] = ..., extra_tests: Optional[Any] = ..., **kwargs): ...
    def setup_databases(self, **kwargs): ...
    def get_resultclass(self): ...
    def run_suite(self, suite, **kwargs): ...
    def teardown_databases(self, old_config, **kwargs): ...
    def teardown_test_environment(self, **kwargs): ...
    def suite_result(self, suite, result, **kwargs): ...
    def run_tests(self, test_labels, extra_tests: Optional[Any] = ..., **kwargs): ...

def is_discoverable(label): ...
def dependency_ordered(test_databases, dependencies): ...
def reorder_suite(suite, classes, reverse: bool = ...): ...
def partition_suite_by_type(suite, classes, bins, reverse: bool = ...): ...
def partition_suite_by_case(suite): ...
def get_unique_databases_and_mirrors(): ...
def setup_databases(verbosity, interactive, keepdb: bool = ..., debug_sql: bool = ..., parallel: int = ..., **kwargs): ...
