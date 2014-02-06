#! /usr/bin/env bash
basedir=$1
vm=$2
vm_dir=$basedir/$vm
snapshot_name=$3

VBoxManage snapshot $vm_dir/$vm.vbox take $snapshot_name
