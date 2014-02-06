#! /usr/bin/env bash
basedir=$1
vm=$2
vm_dir=$basedir/$vm
port=$3

VBoxManage modifyvm $vm_dir/$vm.vbox --natpf1 $port
