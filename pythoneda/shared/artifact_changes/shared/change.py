"""
pythoneda/shared/artifact_changes/shared/changes.py

This file defines the Change class.

Copyright (C) 2023-today rydnr's pythoneda-shared-artifact-changes/shared

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
from pythoneda.entity import Entity
from pythoneda.value_object import primary_key_attribute
from unidiff import PatchSet

class Change(Entity):
    """
    Represents a change in source code.

    Class name: Change

    Responsibilities:
        - Represent a change unambiguously

    Collaborators:
        - None
    """
    def __init__(self, patchSet:PatchSet, repositoryUrl:str, branch:str):
        """
        Creates a new Change instance.
        :param patchSet: The files affected and how.
        :type patchSet: unidiff.PatchSet
        :param repositoryUrl: The url of the repository.
        :type repositoryUrl: str
        :param branch: The branch within the repository.
        :type branch: str
        """
        super().__init__()
        self._patch_set = patchSet
        self._repository_url = repositoryUrl
        self._branch = branch

    @property
    @primary_key_attribute
    def patch_set(self) -> PatchSet:
        """
        Retrieves the PatchSet.
        :return: Such instance.
        :rtype: unidiff.PatchSet
        """
        return self._patch_set

    @property
    @primary_key_attribute
    def repository_url(self) -> str:
        """
        Retrieves the url of the repository.
        :return: Such url.
        :rtype: str
        """
        return self._repository_url

    @property
    @primary_key_attribute
    def branch(self) -> str:
        """
        Retrieves the branch within the repository.
        :return: Such branch.
        :rtype: str
        """
        return self._branch

    @classmethod
    def from_unidiff_text(cls, unidiffText:str, repositoryUrl:str, branch:str): # -> Change:
        """
        Creates a new Change instance from given parameters.
        :param unidiffText: The unified diff.
        :type unidiffText: str
        :param repositoryUrl: The url of the repository.
        :type repositoryUrl: str
        :param branch: The branch the change applies to, within the repository.
        :type branch: str
        :return: A Change instance.
        :rtype: pythonedaartifactsharedchanges.change.Change
        """
        return cls(cls._parse_diff(unidiffText), repositoryUrl, branch)

    @classmethod
    def from_unidiff_file(cls, unidiffFile:str, repositoryUrl:str, branch:str): # -> Change:
        """
        Creates a new Change instance from given parameters.
        :param unidiffFile: The unified diff file.
        :type unidiffFile: str
        :param repositoryUrl: The url of the repository.
        :type repositoryUrl: str
        :param branch: The branch the change applies to, within the repository.
        :type branch: str
        :return: A Change instance.
        :rtype: pythonedaartifactsharedchanges.change.Change
        """
        result = None

        with open(unidiffFile, 'r') as file:
            result = cls(cls._parse_diff(file.read()), repositoryUrl, branch)

        return result

    @classmethod
    def _parse_diff(cls, unidiffText: str) -> PatchSet:
        """
        Parses given unidiff text.
        :param unidiffText: The text to parse.
        :type unidiffText: str
        :return: A PatchSet instance.
        :rtype: unidiff.PatchSet
        """
        return PatchSet(unidiffText)
