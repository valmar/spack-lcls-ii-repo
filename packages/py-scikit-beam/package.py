# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyScikitBeam(PythonPackage):
    """Data analysis tools for X-Ray, Neutron and Electron sciences."""

    homepage = "https://github.com/scikit-beam/scikit-beam"
    pypi = "scikit-beam/scikit-beam-0.0.24.tar.gz"

    maintainers = ["valmar"]

    version("0.0.24", sha256="782009e47f2789f5c3ce3c8a8f3c6d702d7377c92f3cfd1d95cd0825efa25def")

    depends_on("py-setuptools", type="build")
    depends_on("py-fabio", type=("build", "run"))
    depends_on("py-lmfit", type=("build", "run"))
    depends_on("py-numpy@1.15:", type=("build", "run"))
    depends_on("py-pyfai", type=("build", "run"))
    depends_on("py-scikit-image", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-six", type=("build", "run"))
