# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PySuperStateMachine(PythonPackage):
    """Super State Machine gives you utilities to build finite state machines."""

    homepage = "https://github.com/beregond/super_state_machine"
    pypi = "super_state_machine/super_state_machine-2.0.2.tar.gz"

    maintainers = ["valmar"]

    version("2.0.2", sha256="e038a4c573ab80f157bf726c3036367919704f62cd166eb46837143165035958")

    depends_on("py-setuptools", type="build")
    depends_on("py-six", type=("build", "run"))
