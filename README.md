Ansible Role: Inotify
=====================

[![Build Status](https://travis-ci.org/gantsign/ansible-role-inotify.svg?branch=master)](https://travis-ci.org/gantsign/ansible-role-inotify)
[![Ansible Galaxy](https://img.shields.io/badge/ansible--galaxy-gantsign.inotify-blue.svg)](https://galaxy.ansible.com/gantsign/inotify)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/gantsign/ansible-role-inotify/master/LICENSE)

Role to configure the Inotify system settings.

The default value of `max_user_watches` is often too low for desktop users,
particularly when using IDEs.

Requirements
------------

* Ansible >= 2.4

    * Note: earlier versions of Ansible are likely to work but have not been
      tested.

* Linux Distribution

    * Debian Family

        * Debian

            * Wheezy (7)
            * Jessie (8)
            * Stretch (9)

        * Ubuntu

            * Trusty (14.04)
            * Xenial (16.04)

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
    - role: gantsign.maven
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

To test this role run the following command from the project root:

```bash
molecule test
```

License
-------

MIT

Author Information
------------------

John Freeman

GantSign Ltd.
Company No. 06109112 (registered in England)
