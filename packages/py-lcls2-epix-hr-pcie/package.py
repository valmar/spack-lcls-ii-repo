# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyLcls2EpixHrPcie(PythonPackage):
    """LCLS-II Epix HR PCIE software and firmware.."""

    homepage = "https://github.com/slaclab/lcls2-epix-hr-pcie"
    url = "https://pswww.slac.stanford.edu/swdoc/tutorials/lcls2-epix-hr-pcie-1.4.0.tar.gz"

    maintainers = ["valmar"]

    version("1.4.0", sha256="2de1f21e394792b2f2b6042814cc8fef29f7a71a964d55d8ba9f32e0a99dc511")

    depends_on("py-setuptools", type="build")
