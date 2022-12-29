# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyAsyncqt(PythonPackage):
    """An implementation of the PEP 3156 event-loop with Qt."""

    homepage = "https://github.com/gmarull/asyncqt"
    pypi = "asyncqt/asyncqt-0.8.0.tar.gz"

    maintainers = ["valmar"]

    version("0.8.0", sha256="07aa993c7a4b1d4edbd35acced44d1be01da149ba3f7c9a7fa984be4ceca883f")

    depends_on('python@3.5:', type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-pyqt5", type=("build", "run"))
