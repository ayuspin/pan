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

    }
    ]
    return {'resources': resources}
