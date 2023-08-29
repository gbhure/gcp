# pip install google-cloud-compute

from google.cloud import compute_v1
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/ganesh/Downloads/gcp-key.json'

SUBNETWORK = 'projects/lustrous-oasis-381317/regions/us-central1/subnetworks/default'
SOURCE_IMAGE = 'projects/debian-cloud/global/images/debian-11-bullseye-v20230814'
NETWORK_INTERFACE = {
    'subnetwork': SUBNETWORK,
    'access_configs': [
        {
            'name': 'External NAT'
        }
    ]
}

compute_client = compute_v1.InstancesClient()
config = {
    'name': 'demo-instance',
    'machine_type': 'projects/lustrous-oasis-381317/zones/us-central1-a/machineTypes/e2-micro',
    'disks': [
        {
            'boot': True,
            'auto_delete': True,
            'initialize_params': {
                'source_image': SOURCE_IMAGE,
            }
        }
    ],
    'network_interfaces': [NETWORK_INTERFACE]
}

operation = compute_client.insert(project='lustrous-oasis-381317', zone='us-central1-a', instance_resource=config)
operation.result()

