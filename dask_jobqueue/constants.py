from enum import Enum
from .slurm import SLURMCluster
from .pbs import PBSCluster
from .sge import SGECluster
from .lsf import LSFCluster
from .oar import OARCluster
from .htcondor import HTCondorCluster
from .moab import MoabCluster


class SchedulingSystem(Enum):
    SLURM = SLURMCluster
    PBS = PBSCluster
    SGE = SGECluster
    LSF = LSFCluster
    OAR = OARCluster
    HTCONDOR = HTCondorCluster
    MOAB = MoabCluster
