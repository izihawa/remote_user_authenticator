# Remote User Authenticator

Authenticate to Jupyterhub using header REMOTE_USER

## Installation

This package can be installed with pip:

```
pip install jupyterhub-remote-user-authenticator-v2
```

## Configuration

You should edit your :file:`jupyterhub_config.py` to set the authenticator class, the RemoteUserLocalAuthenticator provides features such as local user creation. If you already have local users then you may use the RemoteUserAuthenticator authenticator class:

##### For authentication and local user creation
```
c.JupyterHub.authenticator_class = 'remote_user_authenticator.RemoteUserLocalAuthenticator'
```

This class is derived from LocalAuthenticator and therefore provides features such as the ability to add local accounts through the admin interface if configured to do so.

##### For authentication of the token only

```
c.JupyterHub.authenticator_class = 'remote_user_authenticator.RemoteUserAuthenticator'
```

##### Required configuration

```
# Header with username
c.RemoteUserAuthenticator.header_name = 'REMOTE_USER'
```

You should be able to start jupyterhub. :)

## Issues

If you have any issues or bug reports, all are welcome in the issues section. I'll do my best to respond quickly.

## Contribution

If you want to fix the bugs yourself then raise a PR and I'll take a look :)
