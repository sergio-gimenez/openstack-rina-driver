from oslo_log import log as logger
from neutron_lib.plugins.ml2 import api

LOG = logger.getLogger(__name__)

class MyDriver(api.MechanismDriver):

    def _log_network_information(self, method_name, current_context, prev_context):

        LOG.info("**** %s ****" % (method_name))

        # Print the Network Name using the context
        LOG.info("Current Network Name: %s" %
                 (current_context['name']))

        # For create operation prev_context will be None.
        if prev_context is not None:
            LOG.info("Previous Network Name: %s" %
                     (prev_context['name']))

        # Print the Network Type
        LOG.info("Current Network Type: %s" %
                 current_context['provider:network_type'])

        LOG.info("**** %s ****" % (method_name))

    def initialize(self):
        """Perform driver initialization.
        Called after all drivers have been loaded and the database has
        been initialized. No abstract methods defined below will be
        called prior to this method being called.
        """
        LOG.info("Hello, mydriver initialize")

    def create_network_postcommit(self, context):
        # Extract the current and the previous network context
        LOG.info("Hello, inside create_network_postcommit")
        current_network_context = context.current
        previous_network_context = context.original
        self._log_network_information(
            "Create Network PostCommit", current_network_context, previous_network_context)
