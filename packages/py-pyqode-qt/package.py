# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPyqodeQt(PythonPackage):
    """Source code editor for PyQt/PySide."""

    homepage = "https://github.com/pyQode/pyqode.qt"
    pypi = "pyqode.qt/pyqode.qt-2.10.0.tar.gz"

    maintainers = ["valmar"]

    version("2.10.0", sha256="cfe97d85b210f0d77663c9df47bcb25bbb7cbbe2d9f58c0a9fd94e5e1d7daa2f")

    depends_on("py-setuptools", type="build")
    depends_on("py-pyqt5", type=("build", "run"))
