# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import re

from spack.package import *
from spack.pkg.builtin.rdma_core import RdmaCore as BuiltinRdmaCore


class RdmaCore(BuiltinRdmaCore):
    """RDMA core userspace libraries and daemons"""

    version("17.2", sha256="c8d6dfc6dce1488d82bf669f9f56dc630c5fb76fe8a457d85d007e527e14b784")
    
    patch("0001-redhat-kernel-init-ocrdma-is-tech-preview-too.patch", when="@17.2")
    patch("0002-redhat-kernel-init-libi40iw-no-longer-tech-preview.patch", when="@17.2")
    patch("0003-rdma-hw-modules.rules-i40iw-autoload-breaks-suspend.patch", when="@17.2")
    patch("0004-Revert-redhat-remove-files-that-we-no-longer-use.patch", when="@17.2")
    patch("0005-fix_mtu_limiting_for_ipoib.patch", when="@17.2")
    patch("0006-srp_daemon-Remove-unsupported-systemd-configurations.patch", when="@17.2")
    patch("0007-srp_daemon-srp_daemon.service-should-be-started-afte.patch", when="@17.2")
