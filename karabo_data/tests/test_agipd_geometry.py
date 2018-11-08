from matplotlib.figure import Figure
import numpy as np

from karabo_data.geometry2 import AGIPD_1MGeometry

def test_snap_assemble_data():
    geom = AGIPD_1MGeometry.from_quad_positions(quad_pos=[
        (-525, 625),
        (-550, -10),
        (520, -160),
        (542.5, 475),
    ])

    stacked_data = np.zeros((16, 512, 128))
    img, centre = geom.position_modules_fast(stacked_data)
    assert img.shape == (1256, 1092)
    assert tuple(centre) == (631, 550)
    assert np.isnan(img[0, 0])
    assert img[50, 50] == 0

def test_write_read_crystfel_file(tmpdir):
    geom = AGIPD_1MGeometry.from_quad_positions(quad_pos=[
        (-525, 625),
        (-550, -10),
        (520, -160),
        (542.5, 475),
    ])
    path = str(tmpdir / 'test.geom')
    geom.write_crystfel_geom(path)

    # We need to add some experiment details before cfelpyutils will read the
    # file
    with open(path, 'r') as f:
        contents = f.read()
    with open(path, 'w') as f:
        f.write('clen = 0.119\n')
        f.write('adu_per_eV = 0.0075\n')
        f.write(contents)

    loaded = AGIPD_1MGeometry.from_crystfel_geom(path)
    np.testing.assert_allclose(loaded.modules[0][0].corner_pos,
                               geom.modules[0][0].corner_pos)
    np.testing.assert_allclose(loaded.modules[0][0].fs_vec,
                               geom.modules[0][0].fs_vec)

def test_inspect():
    geom = AGIPD_1MGeometry.from_quad_positions(quad_pos=[
        (-525, 625),
        (-550, -10),
        (520, -160),
        (542.5, 475),
    ])
    # Smoketest
    fig = geom.inspect()
    assert isinstance(fig, Figure)