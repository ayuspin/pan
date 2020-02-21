COMPUTE_URL_BASE = 'https://www.googleapis.com/compute/v1/'

def GenerateConfig(context):
  resources = [{
      'name': context.env['name'],
      'type': 'compute.v1.instance',
      'properties': {
          'zone': context.properties['zone'],
          'machineType': ''.join([COMPUTE_URL_BASE, 'projects/', context.env['project'],
                                  '/zones/', context.properties['zone'],
                                  '/machineTypes/', context.properties['machineType']]),
          'canIpForward': True,
          'disks': [{
              'deviceName': 'boot',
              'type': 'PERSISTENT',
              'boot': True,
              'autoDelete': True,
              'initializeParams': {
                  'sourceImage': ''.join([COMPUTE_URL_BASE, 'projects/',
                                          'paloaltonetworksgcp-public','/global/',
                                          'images/',context.properties['image']])
              }
          }],

          'networkInterfaces': [
          {
              'network': '$(ref.' + context.properties['mgmt-network']+ '-network.selfLink)',
              'accessConfigs': [{
                  'name': 'MGMT Access',
                  'type': 'ONE_TO_ONE_NAT'
              }],
              'subnetwork': '$(ref.' + context.properties['mgmt-network'] + '-subnetwork.selfLink)',
              'networkIP': context.properties['mgmt-ip'],
          },
          {
              'network': '$(ref.' + context.properties['untrust-network']+ '-network.selfLink)',
              'accessConfigs': [{
                  'name': 'UNTRUST Access',
                  'type': 'ONE_TO_ONE_NAT'
              }],
              'subnetwork': '$(ref.' + context.properties['untrust-network'] + '-subnetwork.selfLink)',
              'networkIP': context.properties['untrust-ip'],
          },
          {
              'network': '$(ref.' + context.properties['trust-network']+ '-network.selfLink)',
              'subnetwork': '$(ref.' + context.properties['trust-network'] + '-subnetwork.selfLink)',
              'networkIP': context.properties['trust-ip'],
          }
          ]
      }
  }]
  return {'resources': resources}
