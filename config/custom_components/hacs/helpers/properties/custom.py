# pylint: disable=missing-class-docstring,missing-module-docstring,missing-function-docstring,no-member
from abc import ABC


class RepositoryPropertyCustom(ABC):
    @property
    def custom(self):
        """Return flag if the repository is custom."""
        if str(self.data.id) in [str(x) for x in self.hacs.common.default]:
            return False
        return self.data.full_name != "hacs/integration"
