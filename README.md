Ansible Role: Inotify
=====================

[![Build Status](https://travis-ci.com/gantsign/ansible-role-inotify.svg?branch=master)](https://travis-ci.com/gantsign/ansible-role-inotify)
[![Ansible Galaxy](https://img.shields.io/badge/ansible--galaxy-gantsign.inotify-blue.svg)](https://galaxy.ansible.com/gantsign/inotify)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/gantsign/ansible-role-inotify/master/LICENSE)

Role to configure the Inotify system settings.

The default value of `max_user_watches` is often too low for desktop users,
particularly when using IDEs.

Requirements
------------

* Ansible >= 2.8

    * Note: earlier versions of Ansible are likely to work but have not been
      tested.

* Linux Distribution

    * Debian Family

        * Debian

            * Jessie (8)
            * Stretch (9)

        * Ubuntu

            * Xenial (16.04)
            * Bionic (18.04)

    * RedHat Family

        * CentOS

            * 7

    * Note: other versions are likely to work but have not been tested.

Role Variables
--------------

The following variables will change the behavior of this role (default values
are shown below):

```yaml
# The upper limit on the number of events that can be queued to the corresponding inotify instance.
inotify_max_queued_events:

# The upper limit on the number of inotify instances that can be created per real user ID.
inotify_max_user_instances:

# The upper limit on the number of watches that can be created per real user ID.
inotify_max_user_watches:

# The file to save inotify config to.
inotify_sysctl_file: '/etc/sysctl.d/20-ansible-inotify.conf'
```

Example Playbook
----------------

```yaml
- hosts: servers
  roles:
    - role: gantsign.inotify
      inotify_max_user_watches: 524288
```

More Roles From GantSign
------------------------

You can find more roles from GantSign on
[Ansible Galaxy](https://galaxy.ansible.com/gantsign).

Development & Testing
---------------------

This project uses [Molecule](http://molecule.readthedocs.io/) to aid in the
development and testing; the role is unit tested using
[Testinfra](http://testinfra.readthedocs.io/) and
[pytest](http://docs.pytest.org/).

To develop or test you'll need to have installed the following:

* Linux (e.g. [Ubuntu](http://www.ubuntu.com/))
* [Docker](https://www.docker.com/)
* [Python](https://www.python.org/) (including python-pip)
* [Ansible](https://www.ansible.com/)
* [Molecule](http://molecule.readthedocs.io/)

Because the above can be tricky to install, this project includes
[Molecule Wrapper](https://github.com/gantsign/molecule-wrapper). Molecule
Wrapper is a shell script that installs Molecule and it's dependencies (apart
from Linux) and then executes Molecule with the command you pass it.

To test this role using Molecule Wrapper run the following command from the
project root:

```bash
./moleculew test
```

Note: some of the dependencies need `sudo` permission to install.

License
-------

MIT

Author Information
------------------

John Freeman

GantSign Ltd.
Company No. 06109112 (registered in England)
