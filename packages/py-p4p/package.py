# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyP4p(PythonPackage):
    """PVAccess for Python."""

    homepage = "https://mdavidsaver.github.io/p4p"
    pypi = "p4p/p4p-4.1.5.tar.gz"

    maintainers = ["valmar"]

    version("4.1.5", sha256="25130597c4333590a4b2fc98fea2a0cd8615647d4e9454ddeddc6700112f8f04")

    depends_on("py-setuptools", type="build")
    depends_on("py-setuptools-dso", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-cython", type=("build", "run"))
    depends_on("py-epicscorelibs", type=("build", "run"))
    depends_on("py-pvxslibs", type=("build", "run"))
