# Basic Install of Kubernetes and Contiv Networking
## standalone kubeadm deployment
### Orignal code credit goes to https://github.com/ben-st/ansible-kubeadm. I used it as a base and changed the CNI to Contiv (by Cisco).

- Requires Ansible 2.4 or newer
- Expects 3 ubuntu nodes (at least 16.04)
- Expects passwordless sudo

These playbooks deploy a very basic installation of kubeadm.
To use them, first edit the "inventory" file to contain the
hostnames of the machines on which you want kubeadm deployed, and edit the
group_vars/ file to set any kubeadm configuration parameters you need.

Then run the playbook, like this:

	`ansible-playbook -i inventory site.yml`

This is a very simple playbook. It deploys the following:

1. Installs basic components (docker, kubeadm, contiv) 
2. Basic kubernetes cluster using kubeadm (3 nodes is recommended)
3. Contiv CNI in vxlan mode
4. Adds three networks (see group_vars/all)
5. Adds two sample applications (guestbook and wordpress)

## My changes

### One time local setup

1. Create an ansible config file to trust all hosts
1. Get the primary key setup for your /.ssh folder

#### Setup trusted hosts

The ansible ssh settings need to be setup to accept all thumbprints for ssh machines. You can create an ansible config file locally, in project scope or globally. I made a file in the path `/private/etc/ansible/ansible.cfg` where it expects the global file to be. Once the file is created add

``` config
[defaults]
host_key_checking = False
```

to not check the host key trust. Otherwise it will be a big pain.

#### Setup Private key for ssh

the second part is you need to have the private key in the `~/.ssh` directory. The current configuration is to use the `terraform.pem` file so make sure
the ssh private key setup by terraform is in `~/.ssh/terraform.pem`

### Deploying the cluster

Steps to deploy to the cluster:

1. use terraform project to create the cluster nodes
1. download the inventory file from the dark-cloud-bucket-terraform-prod:/inventory
1. Start an ssh-agent session adding the terraform.pem private key
1. Run the ansible playbook by executing `make run`

### Reminder

To get the ssh for ansible to work I need to **run this in ssh-agent~~!!!!**

to do that use

``` bash
ssh-agent bash
ssh-add ~/.ssh/terraform.pem
ansible-playbook -i inventory site.yml
```

If I do that it *should* work. Any commands using ansible need to be in the bash
shell created by ssh-agent, not in the normal shell~!

before I was doing ssh-agent bash, then ssh-add and then exit and trying to do things.
**That does not work!**
Gotta set the ssh key every session, and it is only for that specific session.

### How to access the cluster

I changed the networking to be simpler and no longer work. All pods only get setup on master node. Have to  enable other nodes, probably the join command is wrong.

To view the website:

1. Find the IPv4 Public IP of a node in amazon ec2 browser
1. figure out the port we need that to hit based on the service (website is defaulted to 30001 in the service.yaml file in the tempaltes folder for hte deploy)
1. navigate to (ip:port) ex. http://34.214.114.215:30001/

To hit the api server it is different because port 5000 isn't in the range it uses for ports so it gets converted to a different port. View the services by sshing into one of the master or worker nodes and using:

``` bash
kubectl get services
```

and find the service you want, and under PORT(S) you should see something like 5000:31012 for the service you want to hit. The right hand side of the port is the one we want to use, so to hit the books service navigate to: http://34.214.114.215:31012/books

and you should see all the books json return.

then to check network between the two pods find the port for that and navigate to: http://34.214.114.215:31470/steal

and you should get just green eggs and ham book.

### TODO

1. Fix networking so that pods are created  on more than just the master node. *Seems like it may be due to the other nodes not being ready in time for the deployment, so all pods get deployed on the master (which is the only ready node)*
1. Make it so kubernetes installs the network before waiting for the network pods to come up.
1. Decouple the deployment of the app and the cluster
1. Clean up the ansible code
1. Get something to run the ansible code after the instances spin up (maybe just do local exec in terraform?)
1. Make the DNS route to the cluster so I can get to the website using my  darkcloudencyclopedia.com domain

### Done

1. Add a step to install dynatrace on each node (added to provisioning on the terraform template)