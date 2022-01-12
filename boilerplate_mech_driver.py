from oslo_log import log as logger
from neutron_lib.plugins.ml2 import api

LOG = logger.getLogger(__name__)

def initialize(self):
    """Perform driver initialization.
        Called after all drivers have been loaded and the database has
        been initialized. No abstract methods defined below will be
        called prior to this method being called.
        """
    LOG.info("Hello, mydriver initialize")
