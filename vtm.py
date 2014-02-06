#! /usr/bin/env python
import os
import os.path
import sys
import pickle


TOOLS_PATH = os.path.abspath(os.path.dirname(__file__)) + '/tools'
WORKSPACE = os.getcwd()


def check_vtm_folder():
    return os.path.exists('.vtm')


def run_cmd(cmd):
    return os.system('{0}/{1}'.format(TOOLS_PATH, cmd))


def load_metadata():
    with open('.vtm/metadata', 'r') as ftr:
        return pickle.load(ftr)


def write_metadata(metadata):
    with open('.vtm/metadata', 'w') as ftr:
        pickle.dump(metadata, ftr)


def init():
    if check_vtm_folder():
        print 'Error. .vtm exists already'
        return
    vm = sys.argv[2]
    size = sys.argv[3]
    cmd = 'createvm.sh {0} {1} {2}'.format(WORKSPACE, vm, size)
    if run_cmd(cmd) != 0:
        return
    os.mkdir('.vtm')
    metadata = {'name': vm}
    write_metadata(metadata)


def share():
    if not check_vtm_folder():
        print 'Error. .vtm not exists.'
        return
    metadata = load_metadata()
    vm = metadata['name']
    share_name = sys.argv[2]
    host_path = sys.argv[3]
    cmd = 'share_folder.sh {0} {1} {2} {3}'.format(WORKSPACE, vm, share_name, host_path)
    run_cmd(cmd)


def setcd():
    if not check_vtm_folder():
        print 'Error. .vtm not exists.'
        return
    metadata = load_metadata()
    vm = metadata['name']
    iso_path = sys.argv[2]
    cmd = 'setcd.sh {0} {1} {2}'.format(WORKSPACE, vm, iso_path)
    run_cmd(cmd)


def port():
    if not check_vtm_folder():
        print 'Error. .vtm not exists.'
        return
    metadata = load_metadata()
    vm = metadata['name']
    if len(sys.argv) < 3:
        print 'Usage: guestssh,tcp,,2222,,22'
        return
    port = sys.argv[2]
    cmd = 'port.sh {0} {1} {2}'.format(WORKSPACE, vm, port)
    run_cmd(cmd)


def run():
    if not check_vtm_folder():
        print 'Error. .vtm not exists.'
        return
    metadata = load_metadata()
    vm = metadata['name']
    cmd = 'startvm.sh {0} {1}'.format(WORKSPACE, vm)
    run_cmd(cmd)


def register():
    if not check_vtm_folder():
        print 'Error. .vtm not exists.'
        return
    metadata = load_metadata()
    vm = metadata['name']
    cmd = 'register.sh {0} {1}'.format(WORKSPACE, vm)
    run_cmd(cmd)


def stop():
    if not check_vtm_folder():
        print 'Error. .vtm not exists.'
        return
    metadata = load_metadata()
    vm = metadata['name']
    cmd = 'stopvm.sh {0} {1}'.format(WORKSPACE, vm)
    run_cmd(cmd)


def commit():
    if not check_vtm_folder():
        print 'Error. .vtm not exists.'
        return
    metadata = load_metadata()
    vm = metadata['name']
    snapshot_name = sys.argv[2]
    cmd = 'take_snapshot.sh {0} {1} {2}'.format(WORKSPACE, vm, snapshot_name)
    run_cmd(cmd)


def restore():
    if not check_vtm_folder():
        print 'Error. .vtm not exists.'
        return
    metadata = load_metadata()
    vm = metadata['name']
    snapshot_name = sys.argv[2]
    cmd = 'restore_snapshot.sh {0} {1} {2}'.format(WORKSPACE, vm, snapshot_name)
    run_cmd(cmd)


def switch():
    stop()
    restore()
    run()


def list():
    if not check_vtm_folder():
        print 'Error. .vtm not exists.'
        return
    metadata = load_metadata()
    vm = metadata['name']
    cmd = 'list_snapshot.sh {0} {1}'.format(WORKSPACE, vm)
    run_cmd(cmd)


if __name__ == '__main__':
    func = globals().get(sys.argv[1], None)
    if func:
        func()
    else:
        print 'No such command'
