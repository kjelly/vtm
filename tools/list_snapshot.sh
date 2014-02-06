#! /usr/bin/env bash
basedir=$1
vm=$2
vm_dir=$basedir/$vm

VBoxManage snapshot $vm_dir/$vm.vbox list $snapshot_name
