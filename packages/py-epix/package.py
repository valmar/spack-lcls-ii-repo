# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyEpix(PythonPackage):
    "LCLS-II epix firmware and software."""

    homepage = "https://github.com/slaclab/epix"
    url = "https://pswww.slac.stanford.edu/swdoc/tutorials/epix-0.0.3.tar.gz"

    maintainers = ["valmar"]

    version("0.0.3", sha256="259b8fe2977e91a02b7185f2738dca389ee92ea6dd86fce551bed8c4d489de3d")

    depends_on("py-setuptools", type="build")
