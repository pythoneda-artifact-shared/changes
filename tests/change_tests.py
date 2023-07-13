"""
tests/change_tests.py

This script contains tests for pythonedaartifactsharedchanges/change.py

Copyright (C) 2023-today rydnr's pythoneda-artifact-shared/changes

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import sys
from pathlib import Path
import pytest
import re
import tempfile
import unittest

base_folder = str(Path(__file__).resolve().parent.parent)
if base_folder not in sys.path:
    sys.path.append(base_folder)
from pythonedaartifactsharedchanges.change import Change

class ChangeTests(unittest.TestCase):
    """
    Defines tests for pythonedaartifactsharedchanges/change.py.

    Class name: ChangeTests

    Responsibilities:
        - Validates the functionality of the Change class.

    Collaborators:
        - Change
    """

    def test_from_unidiff_text(self):
        """
        Tests the behavior of Change.from_unidiff_text(str, str, str).
        """
        # given
        input = """
diff --git a/pyproject.toml b/pyproject.toml
index e0d9f0a..9a43d8f 100644
--- a/pyproject.toml
+++ b/pyproject.toml
@@ -16,10 +16,12 @@ pythoneda-artifact-changes = "^0.0.1a1"
 pythoneda-artifact-event-changes = "^0.0.1a1"
 pythoneda-artifact-event-infrastructure-changes = "^0.0.1a1"
 pythoneda-artifact-infrastructure-changes = "^0.0.1a1"
-pythoneda-base = "^0.0.1a16"
+pythoneda-artifact-shared-changes = "^0.0.1a1"
+pythoneda-base = "^0.0.1a18"
 pythoneda-infrastructure-base = "^0.0.1a12"
 pythoneda-shared-git = "^0.0.1a3"
 requests = "^2.28.1"
+unidiff = "^0.7.4"

 [tool.poetry.dev-dependencies]
 pytest = "^7.2.0"
        """

        # when
        result = Change.from_unidiff_text(input, "https://github.com/pythoneda-artifact-shared/changes", "main")

        # then
        assert result is not None


    def test_from_unidiff_file(self):
        """
        Tests the behavior of Change.from_unidiff_file(str, str, str).
        """
        # given
        text = """
diff --git a/pyproject.toml b/pyproject.toml
index e0d9f0a..9a43d8f 100644
--- a/pyproject.toml
+++ b/pyproject.toml
@@ -16,10 +16,12 @@ pythoneda-artifact-changes = "^0.0.1a1"
 pythoneda-artifact-event-changes = "^0.0.1a1"
 pythoneda-artifact-event-infrastructure-changes = "^0.0.1a1"
 pythoneda-artifact-infrastructure-changes = "^0.0.1a1"
-pythoneda-base = "^0.0.1a16"
+pythoneda-artifact-shared-changes = "^0.0.1a1"
+pythoneda-base = "^0.0.1a18"
 pythoneda-infrastructure-base = "^0.0.1a12"
 pythoneda-shared-git = "^0.0.1a3"
 requests = "^2.28.1"
+unidiff = "^0.7.4"

 [tool.poetry.dev-dependencies]
 pytest = "^7.2.0"
        """
        with tempfile.NamedTemporaryFile(delete=True, mode='w') as input:
            input.write(text)
        # when
            result = Change.from_unidiff_file(input.name, "https://github.com/pythoneda-artifact-shared/changes", "main")

        # then
        assert result is not None

if __name__ == '__main__':
    unittest.main()
