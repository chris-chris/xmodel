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


class BaseObject(object, metaclass=abc.ABCMeta):
    """Base class for storages.
    """

    @abc.abstractmethod
    def save_tf_saved_model(self, model):
        # type: (Any) -> int

        raise NotImplementedError

    @abc.abstractmethod
    def save_tf_h5(self, model):
        # type: (Any) -> int

        raise NotImplementedError
