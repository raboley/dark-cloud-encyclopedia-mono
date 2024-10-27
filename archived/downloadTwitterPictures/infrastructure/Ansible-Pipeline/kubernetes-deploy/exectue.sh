#!/usr/bin/env bash
docker run --rm -it \
  -v ~/.ssh/terraform.pem:/root/.ssh/id_rsa \
  -v ~/.ssh/terraform.pub:/root/.ssh/id_rsa.pub \
  -v $(pwd):/ansible_playbooks \
  -v /var/log/ansible/ansible.log \
  raboley/ansible "$@"

  #
docker run --rm -it \
    -v ~/.ssh/terraform.pem:/root/.ssh/id_rsa \
    -v ~/.ssh/terraform.pub:/root/.ssh/id_rsa.pub \
    -v $(pwd):/ansible/playbooks \
    raboley/ansible site.yml -i inventory