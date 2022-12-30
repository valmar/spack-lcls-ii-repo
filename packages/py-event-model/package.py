# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyEventModel(PythonPackage):
    """Data model used by the bluesky ecosystem."""

    homepage = "https://github.com/bluesky/event-model"
    pypi = "event-model/event-model-1.19.1.tar.gz"

    maintainers = ["valmar"]

    version("1.19.1", sha256="c76ae7616148eb0f27fa77fab3a46790671ad97dd3bc5017130867090fb1b4e2")

    depends_on("python@3.6:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-jsonschema", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
