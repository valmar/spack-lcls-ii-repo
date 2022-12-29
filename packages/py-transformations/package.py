# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyTransformations(PythonPackage):
    """Homogeneous Transformation Matrices and Quaternions."""

    homepage = "https://www.cgohlke.com/"
    pypi = "transformations/transformations-2022.9.26.tar.gz"

    maintainers = ["valmar"]

    version("2022.9.26", sha256="9141233392e768eb224b73059b60f19df748bb69493dfd16db7cac9f6e93a4ba")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-numpy@1.19.2:", type=("build", "run"))
