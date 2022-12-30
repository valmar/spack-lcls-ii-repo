# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPvxslibs(PythonPackage):
    """FIXME: PVXS client/server for PVA protocol."""

    homepage = "https://mdavidsaver.github.io/pvxs"
    pypi = "pvxslibs/pvxslibs-1.1.0.tar.gz"

    maintainers = ["valmar"]

    version("1.1.0", sha256="04113e92617645d915bfeef933fadf1d569aa82d64eb2cdd150192c24e21ae2f")

    depends_on("python@2.7:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-setuptools-dso@2.1a3:", type=("build", "run"))
    depends_on("py-epicscorelibs@7.0.3.99.2.0a1:", type=("build", "run"))
