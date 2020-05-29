import os

from oemof.tabular.datapackage import building

path = os.path.join(os.getcwd(), 'datapackage')
building.infer_metadata(path=path, package_name='Barbados')
