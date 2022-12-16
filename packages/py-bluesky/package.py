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
#     spack install py-bluesky
#
# You can edit this file again by typing:
#
#     spack edit py-bluesky
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PyBluesky(PythonPackage):
    """Experiment specification & orchestration.."""

    homepage = "https://blueskyproject.io/bluesky"
    pypi = "bluesky/bluesky-1.10.0.tar.gz"

    maintainers = ["valmar"]

    version("1.10.0", sha256="c66d3754bc1423419aae686d57f40d5a3f4c720976303e26714f4c4477032653")

    depends_on("py-setuptools", type="build")
    depends_on("py-cycler", type=("build", "run"))
    depends_on("py-event-model", type=("build", "run"))
    depends_on("py-historydict", type=("build", "run"))
    depends_on("py-msgpack", type=("build", "run"))
    depends_on("py-msgpack-numpy", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-super-state-machine", type=("build", "run"))
    depends_on("py-toolz", type=("build", "run"))
    depends_on("py-tqdm", type=("build", "run"))
    depends_on("py-zict", type=("build", "run"))

