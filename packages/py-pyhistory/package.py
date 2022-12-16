# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPyhistory(PythonPackage):
    """PyHistory maintains history entries for your project."""

    homepage = "https://github.com/beregond/pyhistory"
    pypi = "pyhistory/pyhistory-2.2.0.tar.gz"

    maintainers = ["valmar"]

    version("2.2.0", sha256="9979a8ab9f45eea04889fcb79151fa81451fe47e219ef96f28e9e2843b9a7650")

    depends_on("py-setuptools", type="build")
    depends_on("py-click", type=("build", "run"))
