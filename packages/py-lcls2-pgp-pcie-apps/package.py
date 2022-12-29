# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------

from spack.package import *


class PyLcls2PgpPcieApps(PythonPackage):
    """LCLS-II PGP-PCIE-Apps firmware and software."""

    homepage = "https://www.example.com"
    url = "https://pswww.slac.stanford.edu/swdoc/tutorials/lcls2-pgp-pcie-apps-2.2.0.tar.gz"

    maintainers = ["valmar"]

    version("2.2.0", sha256="cb690869c5253c5626ecc83ba978044e3fbd37e1ec33c2fd0ff8747cb53e7a44")

    patch("setup.patch")

    depends_on("py-setuptools", type="build")
