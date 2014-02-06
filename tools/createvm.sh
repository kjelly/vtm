#! /usr/bin/env bash
basedir=$1
vm=$2
vm_dir=$basedir/$vm
vm_size=$3
VBoxManage createvm --name $vm --ostype "Linux26_64" --register --basefolder=$basedir
VBoxManage createhd --filename $basedir/$vm/$vm.vdi --size $vm_size
#add disk
VBoxManage storagectl $vm --name "SATA Controller" --add sata --controller IntelAHCI
VBoxManage storageattach $vm_dir/$vm.vbox --storagectl "SATA Controller" --port 0 --device 0 --type hdd --medium $vm_dir/$vm.vdi
#misc
VBoxManage modifyvm $vm_dir/$vm.vbox --ioapic on
VBoxManage modifyvm $vm_dir/$vm.vbox --boot1 dvd --boot2 disk --boot3 none --boot4 none
VBoxManage modifyvm $vm_dir/$vm.vbox --memory 1024 --vram 128
VBoxManage modifyvm $vm_dir/$vm.vbox --nic1 nat

#add cd
VBoxManage storagectl $vm_dir/$vm.vbox --name "IDE Controller" --add ide
