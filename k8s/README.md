

# k3d Deployment

This will set up a 3-node k3s cluster, and 2 2-node pods running FastAPI httpbin.

Not gonna lie, this is mostly for me to play around with and learn k8s, so my k8s
config isn't gonna be quite as robust at the main FastAPI Httpbin product itself.


## Pre-requisites

- Set up `/etc/hosts` entry for `httpbin.localdomain` -> `127.0.0.1`
  - I recommend the utility [xwmx/hosts](https://github.com/xwmx/hosts) for this.


## Quickest Instructions

- Create the cluster (with both sets of ports open)
  - `./manage-k3s-cluster.sh create`
  - This will also import the `fastapi-httpbin` docker image.
- Create Kubernetes deployment, services, and ingress.
  - `kubectl apply -f .`
- Getting traffic in
  - `curl httpbin.localdomain:8000/`
  - OR `./curl-k8s.sh`
- Getting stats
  `./watch-k8s.sh`

## Quicker instructions

- Create the cluster (with both sets of ports open)
  - `k3d cluster create -p "8080:80@loadbalancer" -p "8082:30080@agent:0" --agents 2`
- Import the image from your Docker installation into the k3s cluster:
  - `k3d image import dmuth1/fastapi-httpbin`
  - You can skip this step, but creating the deployment will download the image, which is over a gig, and you may not want to repeatedly do that.
- Create Kubernetes deployment, services, and ingress.
  - `kubectl apply -f .`
- Getting traffic in
  - ClusterIP (Preferred, goes through a load balancer)
    - `curl localhost:8080/`
  - NodePort (less preferred, connects to a specific Kubernetes node)
    - `curl localhost:8082/`
- Monitor the logs
  - `stern .* --tail 1`
- Delete the cluster
  - `k3d cluster delete`


## Stock instructions

### With Ingress

- Create the cluster
  - `k3d cluster create -p "8080:80@loadbalancer" --agents 2`
    - This will map port 8080 from the Mac host to port 80 on the contained named "loadbalancer".
  - `kubectl create deployment nginx --image=nginx`
    - Or deploy multiple copies:
      - `kubectl create deployment nginx --image=nginx --replicas=3`
  - `kubectl create service clusterip nginx --tcp=80:80`
    - Create a service which points to nginx
  - `kubectl apply -f ingress.yml`
    - Create an ingress object which points to the loadbalancer
- Test out the webserver
  - `curl localhost:8080/`
- Monitor the logs
  - `stern .* --tail 1`
- Delete the cluster
  - `k3d cluster delete`


### With NodePort

- Create the cluster
  - `k3d cluster create mycluster -p "8082:30080@agent:0" --agents 2`
- Create the deployment
  - `kubectl create deployment nginx --image=nginx`
- Standup Nodeport service
  - `kubectl apply -f nodeport.yml`
- `curl localhost:8082/`
- Monitor the logs
  - `stern .* --tail 1`
- Delete the cluster
  - `k3d cluster delete`



