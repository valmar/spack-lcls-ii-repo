# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPyfai(PythonPackage):
    """Fast Azimuthal Integration in Python."""

    homepage = "https://github.com/silx-kit/pyFAI"
    pypi = "pyFAI/pyFAI-0.21.3.tar.gz"

    maintainers = ["valmar"]

    version("0.21.3", sha256="c999d57249af806012a2683be2204d81887de159ed48e4cabacf83860b3dedfd")

    depends_on("py-setuptools@:60", type="build")
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-cython@0.25:", type=("build", "run"))
    depends_on("py-fabio@0.5:", type=("build", "run"))
    depends_on("py-scipy", type=("build", "run"))
    depends_on("py-matplotlib", type=("build", "run"))
    depends_on("py-numexpr", type=("build", "run"))
    depends_on("py-h5py", type=("build", "run"))
    depends_on("py-silx@1.1:", type=("build", "run"))
    depends_on("py-pyopengl", type=("build", "run"))
    depends_on("py-pyqt5", type=("build", "run"))
    depends_on("py-hdf5plugin", type=("build", "run"))
    depends_on("py-transformations", type=("build", "run"))
    depends_on("py-nbsphinx", type=("build", "run"))

