# Import neutron-server logger
from oslo_log import log as logger
# Import Neutron Database API
from neutron_lib.plugins.ml2 import api
# Import ML2 Database API
from neutron_lib import db as ml2_db

LOG = logger.getLogger(__name__)


class MyDriver(api.MechanismDriver):

    def _log_port_information(self, method_name, context):
        LOG.info("**** %s ****" % (method_name))
        # Extract the current Port context
        current_port_context = context.current
        # Extract the associated Network Context
        network_context = context.network
        LOG.info("Port Type: %s" % (current_port_context['device_owner']))
        LOG.info("IP Address of the Port: %s" % ((current_port_context['fixed_ips'][0])['ip_address']))
        LOG.info("Network name for the Port: %s" % (network_context.current['name']))
        LOG.info("Network type for the Port: %s" % (network_context.current['provider:network_type']))
        LOG.info("Segmentation ID for the Port: %s" % (network_context.current['provider:segmentation_id']))
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

        # TODO Using ML2 DB API, fetch the Network that matches the Network ID
        # network_segments = full_context.network_segments
        # LOG.info(
        #     "Network associated to the Subnet: %s" % (network_segments))

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

    def create_port_postcommit(self, context):
        self._log_port_information("Create Port PostCommit", context)
