# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyEpixHrSingle10k(PythonPackage):
    """LCLS-II Epix HR Singe 10k software and firmware.."""

    homepage = "https://github.com/slaclab/epix-hr-single-10k"
    url = "https://pswww.slac.stanford.edu/swdoc/tutorials/epix-hr-single-10k-1.0.0.tar.gz"

    maintainers = ["valmar"]

    version("1.0.0", sha256="f540dba15f400818d5eaca1580a78910f9e4c45256c30f5ff892bdde1592f98c")
    
    patch("setup.patch")

    depends_on("py-setuptools", type="build")
