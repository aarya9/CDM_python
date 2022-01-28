"""Creates the virtual machine."""


COMPUTE_URL_BASE = 'https://www.googleapis.com/compute/v1/'


def GenerateConfig(context):

    resources_one = [{
        'name': context.env["deployment"]+'-network',
        'type': 'compute.v1.network',
        'properties': {
            'autoCreateSubnetworks':False}}]

    # for x  in context.properties['subnets'] :
    y=[x for x in context.properties["subnets"]]
    for p in y:
            resources_two=[{
                'type': 'compute.v1.subnetwork',
                'name': p['name'],
                'properties': {
                    'network':'$(ref.'+context.env["deployment"]+'-network.selfLink)',
                    'ipCidrRange':p['range'],
                    'region': context.properties["region"],
                }
            }]

    # resources = list(map(add, resources_one, resources_two))
    resources=[*resources_one,*resources_two]
    return {'resources': resources}