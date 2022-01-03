from neutron.openstack.common import log as logging
from neutron.plugins.ml2 import driver_api as api

LOG = logging.getLogger(__name__)

class MyDriver(api.MechanismDriver):

   def initialize(self):
        LOG.info("Hello, mydriver initialize)
