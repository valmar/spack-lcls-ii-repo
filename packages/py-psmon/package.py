# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPsmon(PythonPackage):
    """Monitors and limits process resource."""

    homepage = "https://github.com/rkkautsar/psmon"
    pypi = "psmon/psmon-1.1.1.tar.gz"

    maintainers = ["valmar"]

    version("1.1.1", sha256="ecbd4e3a34b5f20ac5c62e4cd1e19f7384c6d72f2dd7d66c7b4bc36b529b8385")

    depends_on("py-poetry", type="build")
    depends_on("py-psutil", type=("build", "run"))
    depends_on("py-loguru", type=("build", "run"))