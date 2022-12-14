# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPyqode3Python(PythonPackage):
    """Source code editor widget for PyQt/PySide."""

    homepage = "https://github.com/pyQode/pyqode.python"
    pypi = "pyqode/pyqode3.python-3.2.4.tar.gz"

    maintainers = ["valmar"]

    version("3.2.4", sha256="5254a3c91c8710fd258bbb4647e13af32c9819698b106f1613281d4d36ba7aa2")

    depends_on("py-setuptools", type="build")
    depends_on("py-pyqode-qt", type=("build", "run"))
    depends_on("py-pyqode3-core", type=("build", "run"))
    depends_on("py-jedi", type=("build", "run"))
    depends_on("py-pycodestyle", type=("build", "run"))
    depends_on("py-pyflakes", type=("build", "run"))
    depends_on("py-docutils", type=("build", "run"))

    def url_for_version(self, version):
        url_fmt = "https://pypi.org/packages/source/p/pyqode3.python/pyqode3.python-{0}.tar.gz"
        return url_fmt.format(version)
