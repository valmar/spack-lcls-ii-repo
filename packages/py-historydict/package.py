# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyHistorydict(PythonPackage):
    """A persistent dictionary with history backed by sqlite."""

    homepage = "https://github.com/Nikea/historydict"
    pypi = "historydict/historydict-1.2.3.tar.gz"

    maintainers = ["valmar"]

    version("1.2.3", sha256="92705e463637e4d99204bbafce446a85eeb2dffd06413222ef28d52f5cfe229b")

    depends_on("py-setuptools", type="build")
