**Note:** Needs for setup base settings/packages

Requirements
------------

- [x] Ansible version >= 2.14

Dependencies
------------

- [x] none (Ubuntu)

Installation
------------

- [x] git

Use `git@github.com:Trusty-Host/ansible-common.git` to pull the latest edge commit of the role from git.

Platforms
---------

```yaml

Ubuntu:
  versions:
    - focal
    - bionic
```

Role Variables
--------------

The descriptions and default settings for all variables can be found in the **`defaults/main.yml`** directory in the following file:

- **[defaults/main.yml](./defaults/main.yml)**

## Example

### Configuration

```yaml
# Install SSH password auth type
ssh_pasword_auth: (yes|no)
# Install SSH public key auth type
ssh_pasword_auth_pubkey: (yes|no)
```


### Playbook

Use it in a playbook as follows:

```yaml
- hosts: all
  become: yes
  roles:
    - common
```

License
-------

[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
