# OpenStack ML2 RINA driver implememtation

# Load a ML2 driver to OpenStack

1. Copy the driver file into `/opt/stack/neutron/neutron/plugins/ml2/drivers`

2. Update the `/etc/neutron/plugins/ml2/ml2_conf.ini` configuration file
    * In the `[ml2]` section of the file, configure mechanism_drivers, as follows:
    ```
    [ml2]
    ... 
    mechanism_drivers = ovn,logger,cookbook
    ```
3. Open the `/opt/stack/neutron/neutron.egg-info/entry_points.txt`
4. In the [neutron.ml2.mechanism_drivers] section of the file, configure the Python class that needs to be loaded for the mechanism driver named `cookbook`.
  ```
  [neutron.ml2.mechanism_drivers]
  ...
  cookbook = neutron.plugins.ml2.drivers.ch10_ml2_mech_driver:CookbookMechanismDriver
  ```
5. Restart the Neutron services in your DevStack setup.
  ```
  python3 $(which neutron-server) --config-file /etc/neutron/neutron.conf --config-file /etc/neutron/plugins/ml2/ml2_conf.ini --log-file ./server.log
  ```

  * Here we are passing the neutron config default file, the modified `ml2/ml2_conf.ini` and we are keeping a log of all this info in server.log`
  


### Code samples for OpenStack Networking Cookbook
#### Author(s): Sriram Subramanian and Chandan Dutta Chowdhury
#### Published by: Packt Publishing

#### https://www.packtpub.com/virtualization-and-cloud/openstack-networking-cookbook

#### Files
1. ch10_ml2_mech_driver.py - the main ML2 mechanism driver file. We will use this file as the starting point and will be updating it for the recipes in Chapter 10.
2. ch10_ml2_mech_driver_network.py - this file contains Network related mechanism driver methods
3. ch10_ml2_mech_driver_subnet.py - this file contains Subnet related mechanism driver methods
4. ch10_ml2_mech_driver_port.py - this file contains Port related mechanism driver methods 
5. ch10_ml2_mech_driver_final.py - This file represents the final mechanism driver that includes Network, Subnet and Port driver methods.
6. local.conf - The conf file can be used in your DevStack setup
