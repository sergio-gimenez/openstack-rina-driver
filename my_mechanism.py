from oslo_log import log as logger
from neutron_lib.plugins.ml2 import api
LOG = logging.getLogger(__name__)

LOG = logger.getLogger(__name__)


class MyDriver(api.MechanismDriver):

    def initialize(self):
        LOG.info("Hello, mydriver initialize")
