# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Rogue(CMakePackage):
    """SLAC Python Based Hardware Abstraction & Data Acquisition System."""

    homepage = "https://www.example.com"
    url = "https://github.com/slaclab/rogue/archive/refs/tags/v5.14.0.tar.gz"

    maintainers = ["valmar"]

    version("5.14.0", sha256="b0af5426e7f80f2949d929dc1bef79f8fcfeca234af799784502cd22120ccf12")

    depends_on("boost")
    depends_on("libzmq")
    depends_on("python")
    depends_on("py-pyyaml", type = ("build", "run"))
    depends_on("py-parse", type = ("build", "run"))
    depends_on("py-click", type = ("build", "run"))
    depends_on("py-coverage", type = ("build", "run"))
    depends_on("py-codecov", type = ("build", "run"))
    depends_on("py-pytest@3.6:", type = ("build", "run"))
    depends_on("py-pytest-cov", type = ("build", "run"))
    depends_on("py-sphinx", type = ("build", "run"))
    depends_on("py-sphinx-rtd-theme", type = ("build", "run"))
    depends_on("py-sphinxcontrib-napoleon", type = ("build", "run"))
    depends_on("py-breathe", type = ("build", "run"))
    depends_on("py-pyzmq", type = ("build", "run"))
    depends_on("py-pyepics", type = ("build", "run"))
    depends_on("py-p4p", type = ("build", "run"))
    depends_on("py-sqlalchemy", type = ("build", "run"))
    depends_on("py-pyserial", type = ("build", "run"))
    depends_on("py-numpy", type = ("build", "run"))
    depends_on("py-flake8", type = ("build", "run"))
    depends_on("py-gitpython", type = ("build", "run"))
    depends_on("py-pygithub", type = ("build", "run"))
    depends_on("py-pydm", type = ("build", "run"))

    def cmake_args(self):
        print("Version", self.version)
        args = ["-DROGUE_INSTALL=system", "-DROGUE_DIR={0}".format(self.prefix), "-DCMAKE_BUILD_TYPE=RelWithDebInfo", "-DROGUE_VERSION=v{0}".format(self.version)]
        return args
