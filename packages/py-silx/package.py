# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PySilx(PythonPackage):
    """Software library for X-ray data analysis."""

    homepage = "http://www.silx.org/"
    pypi = "silx/silx-1.1.2.tar.gz"

    maintainers = ["valmar"]

    version("1.1.2", sha256="2c391d4c9fe92aefaba130a590b2183da2735efc1bfecced0fc8d02503f6f3d1")

    depends_on("python@3.7:", type=("build", "run"))
    depends_on("py-setuptools@:60.0.0", type="build")
    depends_on("py-numpy@1.12:", type=("build", "run"))
    depends_on("py-cython@0.21.1:", type=("build", "run"))
    depends_on("py-h5py", type=("build", "run"))
    depends_on("py-fabio@0.9:", type=("build", "run"))
    depends_on("py-pyopencl", type=("build", "run"))
    depends_on("py-mako", type=("build", "run"))
    depends_on("py-qtconsole", type=("build", "run"))
    depends_on("py-matplotlib@1.2.0:", type=("build", "run"))
    depends_on("py-pyopengl", type=("build", "run"))
    depends_on("py-python-dateutil", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-pillow", type=("build", "run"))
    depends_on("py-pint", type=("build", "run"))
    depends_on("py-pyqt5", type=("build", "run"))
