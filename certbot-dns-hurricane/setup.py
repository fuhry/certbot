from setuptools import setup
from setuptools import find_packages

version = '0.38.0.dev0'

# Remember to update local-oldest-requirements.txt when changing the minimum
# acme/certbot version.
install_requires = [
    'acme>=0.29.0',
    'certbot>=0.34.0',
    'mock',
    'setuptools',
    'zope.interface',
]

setup(
    name='certbot-dns-hurricane',
    version=version,
    description="Hurricane Electric DNS Authenticator plugin for Certbot",
    url='https://github.com/certbot/certbot',
    author="Certbot Project",
    author_email='client-dev@letsencrypt.org',
    license='Apache License 2.0',
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Plugins',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Security',
        'Topic :: System :: Installation/Setup',
        'Topic :: System :: Networking',
        'Topic :: System :: Systems Administration',
        'Topic :: Utilities',
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    keywords=['certbot', 'hurricane', 'electric'],
    scripts=['he-dns'],
    entry_points={
        'certbot.plugins': [
            'dns-hurricane = certbot_dns_hurricane.dns_hurricane:Authenticator',
            'certbot-hurricane:auth = certbot_dns_hurricane.authenticator:Authenticator'
        ],
    },
    test_suite='certbot_dns_hurricane',
)
