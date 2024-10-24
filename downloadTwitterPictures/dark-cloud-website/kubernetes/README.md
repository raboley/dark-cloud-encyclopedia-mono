# The Dark cloud kubernetes cluster

This repo is going to store the code used to package and deploy the kubernetes cluster the dark cloud website will be built on.

## Deployments

To start the cluster from nothing you can use:

``` bash
make deploy
```

which under the covers runs the deploy command on our deploy.yml

``` bash
kubectl create -f deploy.yml
```

Once deployed, updates can be made using:

``` bash
make update
```

which will run:

``` bash
kubectl apply -f deploy.yml --record
```

you can watch the deployment as it happens by running

``` bash
kubectl rollout status deployment deployment-name
```

and then view the history of deployments by running:

``` bash
kubectl rollout history deployment deployment-name
```

since we have recorded the deployments we can easily rollback to the last or any other deployment using the rollout undo commands.

``` bash
kubectl rollout undo deployment deployment-name --to-revision=1
```

## Services

Now that we have some pods, it would be nice to be able to reach them. To do that it would be good to have a service. Services get a stable IP that can be referenced outside the cluster. This service is defined in the service.yml file.

One important note is that to match up with the pods the app selector of the service, needs to match the app label of the pod. If the pods are already up and running this can be retrieved by using

``` bash
kubectl describe pods | grep app
```

which will return all pods in the cluster with their associated value for the app label.

To create this service run

``` bash
kubectl create -f service.yml
```

to figure out what IP address to use if doing this on minikube use

``` bash
minikube ip
```

to get the ip address of the minikube pod. If you are running kubernetes on a vm or a ec2 it should be the public IP address of that node.

With the IP we just need the port, which will be the nodeport defined in the servvice.yml file, although 30000 is the default.

Got this to work by mapping the port of the container to 80. In my container documentation I use "-p 8080:80" which I thought mapped my host computer to port 80 and the container used 8080, but turns out it was the other way around.

## Connections between pods

There used to be an add on called coreDNS that create dns records for every service in the pod, now Kubernetes has coreDNS installed natively so no extra work!

With multiple services in a cluster you will still hit the minikube ip, and then whatever port the service is on. To figure out what port that should be you can run

``` kube
kubectl get services
```

and in the PORT(S) column, the one to navigate to with your browser is on the left of the colon, and what the container/pod is internally mapped to is on the left.