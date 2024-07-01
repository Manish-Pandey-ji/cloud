After all this coding 
Make sure you install all neccesary plugin in jenkin.
Give the public ip in ansible/inventories/hosts.

At last run the code in your local system
ansible-playbook -i ansible/inventories/hosts deploy.yml --become

it run your docker file in your remote machine
