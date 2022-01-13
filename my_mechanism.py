# Import neutron-server logger
from oslo_log import log as logger
# Import Neutron Database API
from neutron_lib.plugins.ml2 import api
# Import ML2 Database API
from neutron_lib.plugins.ml2 import db as ml2_db

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

    def _log_subnet_information(self, method_name, current_context, prev_context, full_context):
        LOG.info("**** %s ****" % (method_name))
        LOG.info("Current Subnet Name: %s" %
                 (current_context['name']))
        LOG.info("Current Subnet CIDR: %s" %
                 (current_context['cidr']))
        # Extract the Network ID from the Subnet Context
        network_id = current_context['network_id']
        # Get the Neutron DB Session Handle
        session = full_context._plugin_context.session
        # Using ML2 DB API, fetch the Network that matches the Network ID
        networks = ml2_db.get_network_segments(session, network_id)
        LOG.info(
            "Network associated to the Subnet: %s" % (networks))
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

    def update_network_postcommit(self, context):
        # Extract the current and the previous network context
        current_network_context = context.current
        previous_network_context = context.original
        self._log_network_information(
            "Update Network PostCommit", current_network_context, previous_network_context)

    def create_subnet_postcommit(self, context):
        # Extract the current and the previous Subnet context
        current_subnet_context = context.current
        previous_subnet_context = context.original
        self._log_subnet_information(
            "Create Subnet PostCommit", current_subnet_context, previous_subnet_context, context)
