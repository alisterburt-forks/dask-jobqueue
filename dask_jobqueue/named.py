from typing import Type

import dask

from .constants import SchedulingSystem
from .core import JobQueueCluster


def _create_named_cluster(name: str) -> Type[JobQueueCluster]:
    """Create a JobQueueCluster for a named cluster in the dask config.

    Parameters
    ----------
    name : str
        name of cluster in config file

    Returns
    -------
    cluster : JobQueueCluster
        cluster created
    """
    config = dask.config.get(key=name)
    scheduling_system = str(config["job-scheduling-system"]).upper()
    cluster_cls = getattr(SchedulingSystem, scheduling_system).value
    return cluster_cls(**config)


NamedCluster = _create_named_cluster
