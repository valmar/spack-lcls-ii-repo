# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PySetuptoolsDso(PythonPackage):
    """setuptools extension for building non-Python Dynamic Shared Objects."""

    homepage = "https://mdavidsaver.github.io/setuptools_dso"
    pypi = "setuptools_dso/setuptools_dso-2.6.tar.gz"

    maintainers = ["valmar"]

    version("2.6", sha256="d061c0bc2a9b9d784e42d6ef71c6cd5bf5e1b5c3ab2aa43e940ee687ea2c6e23")

    depends_on("py-setuptools", type="build")
