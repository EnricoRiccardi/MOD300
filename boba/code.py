import matplotlib.pyplot as plt
from astropy import units as u
from mw_plot import MWFaceOn
from mw_plot import MWSkyMap

mw1 = MWFaceOn(
    radius=20 * u.kpc,
    unit=u.kpc,
    coord="galactocentric",
    annotation=True,
    figsize=(10, 8),
)

mw1.title = "Bird's Eyes View"
mw1.scatter(8 * u.kpc, 0 * u.kpc, c="r", s=2)
#%%

mw1 = MWSkyMap(
    center="M31",
    radius=(4000, 4000) * u.arcsec,
    background="Mellinger color optical survey",
)

fig, ax = plt.subplots(figsize=(5, 5))
mw1.transform(ax)
#%%

mw1 = MWSkyMap(
    center="M31",
    radius=(18000, 18000) * u.arcsec,
    background="Mellinger color optical survey",
)

fig, ax = plt.subplots(figsize=(5, 5))
mw1.transform(ax)
