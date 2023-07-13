#every item is contingent on the vm-name
#ensure that it is all lowercase and less than 15 characters
#for domainUser and domainPassword enter your admin credentials eg. user.admin and pwd
Connect-AzAccount
Write-Output "Ensure VMname is all lowercase < 15 characters, symbols only use - "
$vmname = Read-Host "Enter Your VM Name"

New-AzResourceGroupDeployment `
  -Name 'vm-deployment1' `
  -ResourceGroupName 'Resource-Group-Here' `
  -virtualMachines_template_vm_123_name $vmname `
  -TemplateFile '.\template.json' `
  -TemplateParameterFile '.\parameters.json'