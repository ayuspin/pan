region = "europe-west1"
zone = "europe-west1-c"

fwname = "fw"
fwimage = "vmseries-byol-904"
fwmachineType = "n1-standard-4"
fwmgmt_ip = "10.0.0.5"
mgmt_network_name ="mgmt"
mgmt_subnetwork_ipcidrrange="10.0.0.0/24"
fwuntrust_ip = "10.0.1.5"
untrust_network_name ="untrust"
untrust_subnetwork_ipcidrrange="10.0.1.0/24"
fwtrust_ip = "10.0.2.5"
trust_network_name ="trust"
trust_subnetwork_ipcidrrange="10.0.2.0/24"

srvname = "srv"
srvimage = "debian-10"
srvmachineType = "f1-micro"
srvmgmt_ip = "10.0.0.6"

def GenerateConfig(unused_context):
    resources = [
        {
        'name': fwname,
        'type': 'vm.py',
        'properties': {
            'zone': zone,
            'machineType': fwmachineType,
            'image': fwimage,
            'mgmt-network': mgmt_network_name,
            'mgmt-ip': fwmgmt_ip,
            'untrust-network': untrust_network_name,
            'untrust-ip': fwuntrust_ip,
            'trust-network': trust_network_name,
            'trust-ip': fwtrust_ip
            }
        },
        {
        'name': srvname,
        'type': 'srvvm.py',
        'properties': {
            'zone': zone,
            'machineType': srvmachineType,
            'image': srvimage,
            'mgmt-network': mgmt_network_name,
            'mgmt-ip': srvmgmt_ip,
            }
        },
        {
        'name': mgmt_network_name,
        'type': 'network.py',
        'properties': {
            'region': region,
            'ipcidrrange': mgmt_subnetwork_ipcidrrange
            }
        },
        {
        'name': untrust_network_name,
        'type': 'network.py',
        'properties': {
            'region': region,
            'ipcidrrange': untrust_subnetwork_ipcidrrange
            }
        },
        {
        'name': trust_network_name,
        'type': 'network.py',
        'properties': {
            'region': region,
            'ipcidrrange': trust_subnetwork_ipcidrrange
            }
        }
    ]
    return {'resources': resources}
