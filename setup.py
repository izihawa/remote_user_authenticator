from setuptools import setup

setup(
    name='jupyterhub-remote-user-authenticator',
    version='1.0.0',
    description='Remote User Authenticator for JupyterHub',
    url='https://github.com/izihawa/remote_user_authenticator',
    author='ppodolsky',
    author_email='ppodolsky@me.com',
    license='Apache 2.0',
    packages=['remote_user_authenticator'],
    install_requires=[
        'jupyterhub',
    ]
)
