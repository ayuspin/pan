region = "europe-west1"
zone = "europe-west1-c"

fwname = "fw"
fwimage = "vmseries-byol-904"
fwmachineType = "n1-standard-4"
fwmgmt_ip = "10.0.0.5"
mgmt_network_name ="mgmt"
mgmt_subnetwork_ipcidrrange="10.0.0.0/24"

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
            'mgmt-ip': fwmgmt_ip
            }
        },
        {
        'name': mgmt_network_name,
        'type': 'network.py',
        'properties': {
            'region': region,
            'ipcidrrange': mgmt_subnetwork_ipcidrrange
            }
        }
    ]
    return {'resources': resources}
