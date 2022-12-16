# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyOphyd(PythonPackage):
    """Ophyd is Python library for interfacing with hardware."""

    homepage = "https://blueskyproject.io/ophyd"
    pypi = "ophyd/ophyd-1.7.0.tar.gz"

    maintainers = ["valmar"]

    version("1.7.0", sha256="e7ead46e8ead9bba7d2a2212d4883c98f41be5c83c855ac7026e867ac83609ca")

    depends_on("py-setuptools", type="build")
    depends_on("py-setuptools-scm", type="build")
