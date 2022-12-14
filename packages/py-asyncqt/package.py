# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install py-asyncqt
#
# You can edit this file again by typing:
#
#     spack edit py-asyncqt
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PyAsyncqt(PythonPackage):
    """An implementation of the PEP 3156 event-loop with Qt."""

    homepage = "https://github.com/gmarull/asyncqt"
    pypi = "asyncqt/asyncqt-0.8.0.tar.gz"

    maintainers = ["valmar"]

    version("0.8.0", sha256="07aa993c7a4b1d4edbd35acced44d1be01da149ba3f7c9a7fa984be4ceca883f")

    depends_on("py-setuptools", type="build")

    depends_on("py-pyqt5", type=("build", "run"))
