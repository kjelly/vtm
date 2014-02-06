#! /usr/bin/env bash
basedir=$1
vm=$2
vm_dir=$basedir/$vm
iso_path=$3

VBoxManage storageattach $vm_dir/$vm.vbox --storagectl "IDE Controller" --port 0 --device 0 --type dvddrive --medium $iso_path
