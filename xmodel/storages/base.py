import abc
import copy

from xmodel import structs
from xmodel import type_checking

if type_checking.TYPE_CHECKING:
    from typing import Any  # NOQA
    from typing import Dict  # NOQA
    from typing import List  # NOQA
    from typing import Optional  # NOQA

    from optuna import distributions  # NOQA


class BaseStorage(object, metaclass=abc.ABCMeta):
    """Base class for storages.
    """

    @abc.abstractmethod
    def create_new_project(self, project_name=None):
        # type: (Optional[str]) -> int

        raise NotImplementedError

    @abc.abstractmethod
    def delete_project(self, project_id):
        # type: (int) -> None

        raise NotImplementedError

    @abc.abstractmethod
    def get_project_id_from_name(self, project_name):
        # type: (str) -> int

        raise NotImplementedError

    @abc.abstractmethod
    def get_project_id_from_model_id(self, model_id):
        # type: (int) -> int

        raise NotImplementedError

    @abc.abstractmethod
    def get_project_name_from_id(self, project_id):
        # type: (int) -> str

        raise NotImplementedError

    @abc.abstractmethod
    def set_project_user_attr(self, project_id, key, value):
        # type: (int, str, Any) -> None

        raise NotImplementedError

    @abc.abstractmethod
    def get_project_user_attr(self, project_id, key):
        # type: (int, str) -> Any

        raise NotImplementedError

    @abc.abstractmethod
    def create_new_model(self, model_name=None):
        # type: (Optional[str]) -> int

        raise NotImplementedError

    @abc.abstractmethod
    def set_model_user_attr(self, model_id, key, value):
        # type: (int, str, Any) -> None

        raise NotImplementedError

    @abc.abstractmethod
    def get_model_user_attr(self, model_id, key):
        # type: (int, str) -> Any

        raise NotImplementedError

    @abc.abstractmethod
    def get_model_params(self, model_id):
        # type: (int) -> Dict[str, Any]

        raise NotImplementedError

    @abc.abstractmethod
    def get_best_model(self, project_id):
        # type: (int) -> structs.FrozenModel

        raise NotImplementedError
