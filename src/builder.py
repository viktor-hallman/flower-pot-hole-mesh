# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.18.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
# %load_ext autoreload
# %autoreload 2
# %reload_ext autoreload

import cadquery as cq
from jupyter_cadquery import show as show_object
from cadquery import exporters
import numpy as np

# %%
import cadquery as cq

outer_diameter = 200
outer_thickness = 2
outer_height = 1

line_thickenss = 1
line_height = 0.5
gap_size = 3

# Generate point positions along X
positions_x = [(x, 0) for x in np.arange(-outer_diameter/2, outer_diameter/2, line_height + gap_size)]

# Create boxes at those positions
result_x = cq.Workplane("XY").pushPoints(positions_x).box(line_height, outer_diameter, line_height)



# %%
result = result_x.union(result_x.rotate((0,0,0),(0,0,1),90))

# Create a 2D circle with a 10 mm radius
circle = cq.Workplane("XY").circle(outer_diameter/2).circle(outer_diameter/2 - outer_thickness).extrude(outer_height)

result = result.union(circle)

cutter = cq.Workplane("XY").circle(outer_diameter/2).extrude(outer_height + line_height)

result = result.intersect(cutter)

# Display (if using a CadQuery viewer or Jupyter)
show_object(result)
