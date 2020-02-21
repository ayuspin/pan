def GenerateConfig(context):

    resources = [{
        'name': context.env['name'] + "-network",
        'type': 'compute.v1.network',
        'properties': {
            'routingConfig': {
                'routingMode': 'REGIONAL'
          },
          'autoCreateSubnetworks': False
        }
    },
    {
    'name': context.env['name'] + "-subnetwork",
    'type': 'compute.v1.subnetwork',
    'properties': {
          'network': '$(ref.' +context.env['name'] + '-network.selfLink)',
          'region': context.properties['region'],
          'ipCidrRange': context.properties['ipcidrrange']
          }

    },
    {
    'name': context.env['name'] + "-firewall-icmp",
    'type': 'compute.v1.firewalls',
    'properties': {
          'network': '$(ref.' +context.env['name'] + '-network.selfLink)',
          "allowed": [
                        {
                          "IPProtocol": 'icmp'
                        }
                      ]
          }

    },
    {
    'name': context.env['name'] + "-firewall-ssh",
    'type': 'compute.v1.firewalls',
    'properties': {
          'network': '$(ref.' +context.env['name'] + '-network.selfLink)',
          "allowed": [
                        {
                          "IPProtocol": 'tcp',
                          "ports" : ['22']
                        }
                      ]
          }

    }
    ]
    return {'resources': resources}
