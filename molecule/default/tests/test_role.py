import pytest
import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_inotify_defaults(host):
    kb = host.file('/etc/sysctl.d/10-ansible-inotify.conf')

    assert not kb.exists


def test_inotify_file_permisions(host):
    kb = host.file('/etc/sysctl.d/20-ansible-inotify.conf')

    assert kb.exists
    assert kb.is_file
    assert kb.user == 'root'
    assert kb.group == 'root'
    assert oct(kb.mode) == '0644'


@pytest.mark.parametrize('setting', [
    'fs.inotify.max_queued_events=16384',
    'fs.inotify.max_user_instances=128',
    'fs.inotify.max_user_watches=524288'
])
def test_inotify_file_contents(host, setting):
    kb = host.file('/etc/sysctl.d/20-ansible-inotify.conf')

    assert kb.exists
    assert kb.is_file

    assert kb.contains(setting)
