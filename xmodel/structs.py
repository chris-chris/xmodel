import enum


class ModelState(enum.Enum):
    """State of a :class:`~xmodel.model.Model`.
    """

    TRAINING = 0
    TRAIN_FAIL = 1
    TRAIN_COMPLETE = 2
    LOSS_FAIL = 3
    LOSS_PASS = 4
    METRIC_FAIL = 5
    METRIC_PASS = 6
    STAGE = 7
    PRODUCTION = 8


class ProjectState(enum.Enum):
    """

    """
    EMPTY = 0
    TESTING = 1
    PRODUCTION = 2


class FrozenModel(object):
    """

    """
    pass
