# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyCaproto(PythonPackage):
    """A bring-your-own-IO implementation of the EPICS Channel Access protocol in pure Python."""

    homepage = "https://github.com/caproto/caproto"
    pypi = "caproto/caproto-1.0.0.tar.gz"

    maintainers = ["valmar"]

    version("1.0.0", sha256="52ad3bcc50c2998578f131bf8e761e0915a0736727307b6be1690bca26542a8f")

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-pip@9.0.1:", type="build")
    depends_on("py-setuptools", type="build")
