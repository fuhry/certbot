## Hurricane Electric DNS plugin for certbot

### Before you start

It's expected that the root hosted zone for the domain in question already
exists in your account.

### Setup

1. Create a virtual environment

2. Update its pip and setuptools (`VENV/bin/pip install -U setuptools pip`)
to avoid problems with cryptography's dependency on setuptools>=11.3.

3. Install this package.

### How to use it

Create a credentials file containing your Hurricane Electric account
credentials. Unfortunately they don't support DDNS for TXT records, so
you're stuck inputting your real credentials... for now.

```
dns_hurricane_username = jsample
dns_hurricane_password = secret123
```

Invoke `certbot` using the usual method, specifying the path to your
credentials file using the `--dns-hurricane-credentials` argument:

```
certbot certonly --staging --dns-hurricane \
	-d 'domain.tld' -d '*.domain.tld' \
	--dns-hurricane-credentials /etc/letsencrypt/conf/he.ini
```
