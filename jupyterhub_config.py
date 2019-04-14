# Generic
c.JupyterHub.admin_access = True

# Bitbucket Authenticator.
c.JupyterHub.authenticator_class = 'oauthenticator.bitbucket.BitbucketOAuthenticator'
c.Authenticator.admin_users = {'katie_jones_rr'}


# Docker spawner.
import os
c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
c.DockerSpawner.image = os.environ['DOCKER_NOTEBOOK_IMAGE']
c.DockerSpawner.network_name = os.environ['DOCKER_NETWORK_NAME']
c.JupyterHub.hub_ip = os.environ['HUB_IP']

# User data persistence.
notebook_dir = os.environ.get('DOCKER_NOTEBOOK_DIR') or '/home/jovyan/work'
c.DockerSpawner.notebook_dir = notebook_dir
c.DockerSpawner.volumes = { 'jupyterhub_{username}': notebook_dir }

# Hardware limits.
c.Spawner.cpu_limit = 1
c.Spawner.mem_limit = '1G'


## Services
c.JupyterHub.services = [
    {
        'name': 'cull_idle',
        'admin': True,
        'command': 'python /srv/jupyterhub/cull_idle_servers.py --timeout=3600'.split(),
    },
]
