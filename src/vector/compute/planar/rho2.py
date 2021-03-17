# Copyright (c) 2019-2021, Jonas Eschle, Jim Pivarski, Eduardo Rodrigues, and Henry Schreiner.
#
# Distributed under the 3-clause BSD license, see accompanying file LICENSE
# or https://github.com/scikit-hep/vector for details.

import numpy

from vector.methods import AzimuthalRhoPhi, AzimuthalXY, _aztype


def xy(lib, x, y):
    return x ** 2 + y ** 2


def rhophi(lib, rho, phi):
    return rho ** 2


dispatch_map = {
    (AzimuthalXY,): (xy, float),
    (AzimuthalRhoPhi,): (rhophi, float),
}


def dispatch(v):
    function, *returns = dispatch_map[
        _aztype(v),
    ]
    with numpy.errstate(all="ignore"):
        return v._wrap_result(function(v.lib, *v.azimuthal.elements), returns)