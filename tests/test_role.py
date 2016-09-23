import pytest

from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_inotify_defaults(File):
    kb = File('/etc/sysctl.d/10-ansible-inotify.conf')

    assert not kb.exists


def test_inotify_file_permisions(File):
    kb = File('/etc/sysctl.d/20-ansible-inotify.conf')

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
def test_inotify_file_contents(File, setting):
    kb = File('/etc/sysctl.d/20-ansible-inotify.conf')

    assert kb.exists
    assert kb.is_file

    assert kb.contains(setting)
