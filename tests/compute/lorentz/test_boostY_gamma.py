# Copyright (c) 2019-2021, Jonas Eschle, Jim Pivarski, Eduardo Rodrigues, and Henry Schreiner.
#
# Distributed under the 3-clause BSD license, see accompanying file LICENSE
# or https://github.com/scikit-hep/vector for details.

import pytest

import vector.backends.numpy_
import vector.backends.object_
import vector.geometry


def test():
    vec = vector.backends.object_.VectorObject4D(
        vector.backends.object_.AzimuthalObjectXY(2, 3),
        vector.backends.object_.LongitudinalObjectZ(1),
        vector.backends.object_.TemporalObjectT(4),
    )
    out = vec.boostY(gamma=-3)
    assert out.x == pytest.approx(2)
    assert out.y == pytest.approx(-2.313708498984761)
    assert out.z == pytest.approx(1)
    assert out.t == pytest.approx(3.5147186257614287)

    for t1 in (
        "xyzt",
        "xythetat",
        "xyetat",
        "rhophizt",
        "rhophithetat",
        "rhophietat",
        "xyztau",
        "xythetatau",
        "xyetatau",
        "rhophiztau",
        "rhophithetatau",
        "rhophietatau",
    ):
        tvec = getattr(vec, "to_" + t1)()
        out = tvec.boostY(gamma=-3)
        assert out.x == pytest.approx(2)
        assert out.y == pytest.approx(-2.313708498984761)
        assert out.z == pytest.approx(1)
        assert out.t == pytest.approx(3.5147186257614287)