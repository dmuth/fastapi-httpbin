

# k3d Deployment

## With Ingress

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
    - `curl localhost:8081/`
  - Monitor the logs
    - `stern .* --tail 1`
  - Delete the cluster
    - `k3d cluster delete`

## With NodePort




