# Setting up SSH for Ansible

I couldn't get this to work yesterday after like 2 hours so need to document it for when I do get it working and forget again later.
Following the [ansible documentation](https://docs.ansible.com/ansible/latest/user_guide/intro_getting_started.html) page.

## Hosts file

create or edit the file in `/etc/ansible/hosts`

this file should contain the host names of your machines which will be the *inventory*

``` bash
34.222.125.247
18.236.192.92
34.220.240.0
```

## Private key authentication setup

to setup ssh do:

``` bash
ssh-agent bash
ssh-add ~/.ssh/id_rsa
```

## Test if it worked

Then ping the nodes to see if it worked

``` bash
ansible all -m ping
```

I got a bunch of errors saying `authenticiy of host can't be established. fingerprint is ...`

To fix that I added a file at `/etc/ansible/ansible.cfg`
to do that I used the `touch` command.

``` bash
cd /etc/ansible
sudo touch ansible.cfg
```

I was then able to edit the file in vscode after it would save it using sudo which was prompted as a retry option.

I eventually got it to run! I had to run the commands in ssh-agent. 

so I would do:

``` bash
ssh-agent bash
ssh-add ~/.ssh/terraform.pem
ansible all -m ping -u ubuntu -vvv
```

Once I did that I got past the thumbprint issue, but ran into another issue. It looks like the version of ubuntu I had didn't have python in the bin folder, only python 3. To fix that I made a symbolic link to python from python3. This makes it so when ansible tries to find python and execute it, it actually executes python3 instead.

``` bash
sudo ln -s /usr/bin/python3.6 /usr/bin/python
```

That line is in the provision script now, so final instructions should be:

``` bash
ssh-agent bash
ssh-add ~/.ssh/terraform.pem
ansible all -m ping -u ubuntu -vvv
```

and it should work, as long as the inventory file is correct (/etc/ansible/hosts)

didn't work. Turns out a symbolic link wasn't good enough or there was some permissions thing on how it did it. To fix it I installed python two as a setup step in the terraform template using a `setup.sh` script.

now the final commands to get the ping to work are

``` bash
ssh-agent bash
ssh-add ~/.ssh/terraform.pem
ansible all -m ping -u ubuntu
```

I should finally be able to run the playbooks.