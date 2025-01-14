"""

Åshild Telle / Simula Research Laboratory / 2022

Loads mesh + bc surfaces for pillars

"""

import numpy as np
import os
import dolfin as df
import dolfin_adjoint as da
from mpi4py import MPI
from pathlib import Path
from collections import namedtuple

Geometry = namedtuple("Geometry", ["mesh", "ds"])

def load_mesh_h5(filename: os.PathLike, save_pvd_file: bool = False) -> Geometry:

    comm = MPI.COMM_WORLD
    filename = Path(filename)
    if not filename.is_file():
        raise FileNotFoundError(f"File {filename} does not exist")
    if filename.suffix != ".h5":
        raise RuntimeError("File {filename} is not an HDF5 file")

    mesh = da.Mesh()
    with df.HDF5File(comm, filename.as_posix(), "r") as h5_file:
        h5_file.read(mesh, "mesh", False)

        pillar_bcs = df.MeshFunction("size_t", mesh, 1, 0)
        h5_file.read(pillar_bcs, "curves")

    nodes = mesh.num_vertices()
    cells = mesh.num_cells()

    if save_pvd_file:
        df.File("pillar_fun.pvd") << pillar_bcs

    print(f"Number of nodes: {nodes}, number of elements: {cells}")

    ds = df.Measure('ds', domain=mesh, subdomain_data=pillar_bcs)

    return Geometry(mesh=mesh, ds=ds)
