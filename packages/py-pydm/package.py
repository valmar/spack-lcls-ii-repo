# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPydm(PythonPackage):
    """PyDM: Python Display Manager."""

    homepage = "https://github.com/slaclab/pydm"
    pypi = "pydm/pydm-1.18.1.tar.gz"

    maintainers = ["valmar"]

    version("1.18.1", sha256="74dfae71e2e66dc6799efbe489c363a22597718cc0b32566823d643664e707fa")

    depends_on("py-setuptools", type="build")
    depends_on("py-entrypoints", type=("build", "run"))
    depends_on("py-numpy@1.11.0:", type=("build", "run"))
    depends_on("py-pyepics@3.2.7:", type=("build", "run"))
    depends_on("py-pyqtgraph@0.12.0:", type=("build", "run"))
    depends_on("py-qtpy", type=("build", "run"))
    depends_on("py-requests@1.1.0:", type=("build", "run"))
    depends_on("py-scipy@0.12.0:", type=("build", "run"))
    depends_on("py-six", type=("build", "run"))
