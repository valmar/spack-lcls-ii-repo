# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *
from spack.pkg.builtin.libnl import Libnl as BuiltinLibnl


class Libnl(BuiltinLibnl):
    """libnl - Netlink Protocol Library Suite"""

    version("3.2.28", sha256="cd608992c656e8f6e3ab6c1391b162a5a51c49336b9219f7f390e61fc5437c41")

    def url_for_version(self, version):
        url_fmt = "https://github.com/thom311/libnl/releases/download/libnl{0}/libnl-{1}.tar.gz"
        return url_fmt.format(str(version).replace(".", "_"), version)
