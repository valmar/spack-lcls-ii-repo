# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPyqode3Core(PythonPackage):
    """Source code editor widget for PyQt/PySide."""

    homepage = "https://github.com/pyQode/pyqode.core"
    pypi = "pyqode/pyqode3.core-3.2.35.tar.gz"

    maintainers = ["valmar"]

    version("3.2.35", sha256="2185613d0179c928f30b797fa104b92ff348194bde2eea64b7eef9efeecab044")

    depends_on("py-setuptools", type="build")
    depends_on("py-future", type=("build", "run"))
    depends_on("py-pygments", type=("build", "run"))
    depends_on("py-pyqode-qt", type=("build", "run"))
    depends_on("py-qtawesome", type=("build", "run"))
    depends_on("py-pathspec", type=("build", "run"))

    def url_for_version(self, version):
        url_fmt = "https://pypi.org/packages/source/p/pyqode3.core/pyqode3.core-{0}.tar.gz"
        return url_fmt.format(version)
