"""
"""

import os
import oemof.tabular.datapackage

from oemof.solph import EnergySystem, Model
from oemof.tabular.facades import TYPEMAP
import oemof.tabular.tools.postprocessing as pp


# create  path for results (we use the datapackage_dir to store results)
results_path = 'results'
if not os.path.exists(results_path):
    os.makedirs(results_path)

# create energy system object
es = EnergySystem.from_datapackage(
    os.path.join("./datapackage", "datapackage.json"),
    attributemap={},
    typemap=TYPEMAP,
)

# create model from energy system (this is just oemof.solph)
m = Model(es)

# if you want dual variables / shadow prices uncomment line below
# m.receive_duals()

# select solver 'gurobi', 'cplex', 'glpk' etc
m.solve("glpk")

# get the results from the the solved model(still oemof.solph)
m.results = m.results()

# now we use the write results method to write the results in oemof-tabular
# format
pp.write_results(m, results_path)
print("process completed")


