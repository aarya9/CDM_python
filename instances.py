"""Creates the virtual machine."""


COMPUTE_URL_BASE = 'https://www.googleapis.com/compute/v1/'

# out=[]
def GenerateConfig(context):
    # out=[]
# """Creates the instance for the compute engine."""
    for x in range(2):
        resources = [{
#   'name': context.env["deployment"]+'instanceone',
            'name': 'instance'+str(x+1),
            'type': 'compute.v1.instance',
            'properties': {
                'zone': context.properties['zone'],
                'machineType': ''.join([COMPUTE_URL_BASE, 'projects/', context.env["project"],
                                        '/zones/',context.properties['zone'],'/',
                                        'machineTypes/',context.properties["machineType"]]) ,
                'disks': [{
                    'deviceName': 'boot',
                    'type': 'PERSISTENT',
                    'boot': True,
                    'autoDelete': True,
                    'initializeParams': {
                            'diskName':'boot',
                            'sourceImage': ''.join([COMPUTE_URL_BASE, 'projects/',
                                                'debian-cloud/global',
                                                '/images/family/debian-9']),
                            'tags': {
                                # 'items':{
                                    'web',
                                    'data'
                                # }
                            }
                    }
                }],
                'networkInterfaces': [{
                    'network': '$(ref.'+context.env["deployment"]+'-network.selfLink)',
                    'subnetwork': '$(ref.'+context.properties["subnetwork"]+'.selfLink)',
                    'accessConfigs': [{
                        #   'name': 'External NAT',
                        #   'type': 'ONE_TO_ONE_NAT'
                    }]
                }]
            }
        }]
    # out.append(resources)
    # GenerateConfig(context)
    # return {'resources': out}
    return {'resources': resources}
