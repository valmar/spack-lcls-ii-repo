# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyCameralinkGateway(PythonPackage):
    """LCLS-II cameralink gateway software and firmware."""

    homepage = "https://github.com/slaclab/lcls2-timetool"

    url = "https://pswww.slac.stanford.edu/swdoc/tutorials/cameralink-gateway-7.11.1.tar.gz"

    maintainers = ["valmar"]

    version("7.11.1", sha256="c4aec433edc8c32aa82cfd580da2af1d12fd0299673d9a1dca9123352479cc4d")

    depends_on("py-setuptools", type="build")
