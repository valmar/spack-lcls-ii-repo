# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPyqtgraph(PythonPackage):
    """Scientific Graphics and GUI Library for Python."""

    homepage = "https://www.pyqtgraph.org/"
    pypi = "pyqtgraph/pyqtgraph-0.13.1.tar.gz"

    maintainers = ["valmar"]

    version("0.13.1", sha256="698f87f59db965727b33602a0b29058de21291d8b143dea878b50578aec0dc08")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-pyqt5", type=("build", "run"))
    depends_on("py-numpy@1.20.0:", type=("build", "run"))
