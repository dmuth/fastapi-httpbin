

# k3d Deployment

## Httpbin

- Create the cluster (with both sets of ports open)
  - `k3d cluster create -p "8081:80@loadbalancer" -p "8082:30080@agent:0" --agents 2`
- Create deployment
  - `kubectl apply -f deployment.yml`
- Getting traffic in
  - ClusterIP (Preferred, goes through a load balancer)
    - `kubectl apply -f service-clusterip.yml`
    - `kubectl apply -f ingress-clusterip.yml`
    - `curl localhost:8081/`
  - NodePort (less preferred, connects to a specific Kubernetes node)
    - `kubectl apply -f service-nodeport.yml`
    - `curl localhost:8082/`
- Monitor the logs
  - `stern .* --tail 1`
- Delete the cluster
  - `k3d cluster delete`



## Stock instructions

### With Ingress

- Create the cluster
  - `k3d cluster create -p "8081:80@loadbalancer" --agents 2`
    - This will map port 8081 from the Mac host to port 80 on the contained named "loadbalancer".
  - `kubectl create deployment nginx --image=nginx`
    - Or deploy multiple copies:
      - `kubectl create deployment nginx --image=nginx --replicas=3`
  - `kubectl create service clusterip nginx --tcp=80:80`
    - Create a service which points to nginx
  - `kubectl apply -f ingress.yml`
    - Create an ingress object which points to the loadbalancer
- Test out the webserver
  - `curl localhost:8081/`
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



