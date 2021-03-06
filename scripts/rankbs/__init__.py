from .bandits import UCB1
from .bandits import KLUCB
from .bandits import Exp3
from .bandits import RelativeUCB1
from .bandits import CascadeUCB1
from .bandits import CascadeKL_UCB
from .bandits import CascadeThompsonSampler
from .bandits import CascadeLambdaMachine
from .bandits import CascadeExp3

from .bandits import get_kl_ucb
from .bandits import get_kl_lcb

try:
    __version__ = __import__('pkg_resources').get_distribution('rankbs').version
except:
    __version__ = '?'

__all__ = [
    'UCB1',
    'KLUCB',
    'Exp3',
    'RelativeUCB1',
    'CascadeUCB1',
    'CascadeKL_UCB',
    'CascadeThompsonSampler',
    'CascadeLambdaMachine',
    'CascadeExp3',
]
