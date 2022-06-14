from invoke import Collection
from . import openapi
from . import service
from . import prod
from . import tests

ns = Collection()
ns.add_collection(openapi)
ns.add_collection(service)
ns.add_collection(prod)
ns.add_collection(tests)