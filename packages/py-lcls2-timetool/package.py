# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyLcls2Timetool(PythonPackage):
    """LCLS-II timetool software and firmware."""

    homepage = "https://github.com/slaclab/lcls2-timetool"
    url = "https://pswww.slac.stanford.edu/swdoc/tutorials/lcls2_timetool-3.3.0.tar.gz"

    maintainers = ["valmar"]

    version("3.3.0", sha256="fa9fea8ea77ea2c68239db99e168c055c90174a78a894275fa458b9905fb371c")

    patch("pip.patch")

    depends_on("py-setuptools", type="build")
