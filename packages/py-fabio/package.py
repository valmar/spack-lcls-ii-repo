# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyFabio(PythonPackage):
    """I/O library for images produced by 2D X-ray detector."""

    homepage = "https://github.com/silx-kit/fabio"
    pypi = "fabio/fabio-2022.12.1.tar.gz"

    maintainers = ["valmar"]

    version("2022.12.1", sha256="668287dbb4c7c3042a404c80617bd6be9861a3ff50118a5a2b385f8a285f62bc")

    depends_on("py-setuptools", type="build")
    depends_on("meson", type=("build", "run"))
    depends_on("py-meson-python", type=("build", "run"))
    depends_on("py-ninja", type=("build", "run"))
    depends_on("py-tomli", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-cython", type=("build", "run"))
    depends_on("py-lxml@4.6.3:", type=("build", "run"))
    depends_on("py-h5py", type=("build", "run"))
    depends_on("py-hdf5plugin", type=("build", "run"))
    depends_on("py-sphinx", type=("build", "run"))
    depends_on("py-sphinxcontrib-programoutput", type=("build", "run"))
