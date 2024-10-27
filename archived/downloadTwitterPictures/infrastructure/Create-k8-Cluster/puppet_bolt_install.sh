bolt plan run kubernetes::install_cluster master=34.222.125.247 \
worker_nodes=18.236.192.92,34.220.240.0 \
--user root \
--private-key ~/.ssh/terraform.pem  \
--modulepath ~/.puppetlabs/etc/code/modules -k --sudo

bolt plan run kubernetes::install_cluster master=34.222.125.247 worker_nodes=18.236.192.92,34.220.240.0 --user root --private-key ~/.ssh/terraform.pem --modulepath ~/.puppetlabs/etc/code/modules -insecure --sudo

34.222.125.247
18.236.192.92
34.220.240.0

# master_ip = 34.222.125.247
# worker_ips = [
#     18.236.192.92,
#     34.220.240.0
# ]