#!/usr/bin/env python

import importlib
from pathlib import Path
import pytest

# import diffpy.structure.tests
# assert diffpy.structure.tests.test().wasSuccessful()

if __name__ == "__main__":
    package_directory = 'diffpy.structure'
    module = importlib.import_module(package_directory)
    module_path = Path(module.__file__).parent
    test_location = module_path / 'tests'
    exit_code = pytest.main([str(test_location), "-v"])
    assert exit_code == 0
