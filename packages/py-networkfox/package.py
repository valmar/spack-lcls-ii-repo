# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyNetworkfox(PythonPackage):
    """Lightweight computation graphs for Python."""

    homepage = "https://github.com/slac-lcls/networkfox"

    url = "https://github.com/slac-lcls/networkfox/archive/refs/tags/v0.0.8.tar.gz"

    maintainers = ["valmar"]

    version("0.0.8", sha256="058d18f4eafb0b077aa832c724e4ac05159ae0aed0477f14b2bf25e705e3dc63")

    depends_on("py-setuptools", type="build")
    depends_on("py-networkx", type=("build", "run"))
    depends_on("py-pydot", type=("build", "run"))
    depends_on("py-matplotlib", type=("build", "run"))
