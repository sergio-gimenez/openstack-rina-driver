from oslo_log import log as logger
from neutron_lib.plugins.ml2 import api

LOG = logger.getLogger(__name__)


class MyDriver(api.MechanismDriver):

    def initialize(self):
        """Perform driver initialization.
        Called after all drivers have been loaded and the database has
        been initialized. No abstract methods defined below will be
        called prior to this method being called.
        """
        LOG.info("Hello, mydriver initialize")

    def create_network_postcommit(self, context):
        # Extract the current and the previous network context
        LOG.info("Hello, mydriver create_network_postcommit")
        current_network_context = context.current
        previous_network_context = context.original
        LOG.info("Create Network PostCommit: " +
                 current_network_context + previous_network_context)
