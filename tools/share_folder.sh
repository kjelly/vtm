#! /usr/bin/env bash
basedir=$1
vm=$2
vm_dir=$basedir/$vm
share_name=$3
host_path=$4

VBoxManage sharedfolder add $vm_dir/$vm.vbox --name "$share_name" --hostpath "$host_path"

