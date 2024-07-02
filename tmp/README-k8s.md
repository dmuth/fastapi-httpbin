
# Kubernetes setup of FastAPI Httpbin

This doc contains commands on how to stand up FastAPI Httpbin in a Kubernetes cluster.  Additions and feedback welcome!

## Really Quick Setup

- `kubectl get node` - Make sure our cluster is ready
- `kubectl apply -f .` - Stand up everything
- `kubectl get pods,deployment,ingress` - Show everything
- `kubectl delete -f .` - Delete everything


## Detailed Setup

- Start by standing up 1 or more pods.  Pods in k8s hold your container(s) and multiple pods from the same app are grouped into Deployments.
  - `kubectl apply -f k8s-deployment.yml` - Create pods
  - `kubectl get pods` - List pods
  - `kubectl get deployment` - List the deployment you just created.
  - `kubectl get pods,deployment --show-labels` - Show the labels for pods and the deployment.
    - Labels in k8s are like tags, and can be used to select many resources at once.
  - `kubectl get pods,deployment -l app=httpbin` - Show just pods and deployments that match our app's label.
- Stand up a service - A service is an interface for a group of pods
  - `kubectl apply -f k8s-service-clusterip.yml` - Create the service
  - `kubectl get service -l app=httpbin` - List the service just created.
    - Note that "external IP" may be stuck at "<pending>".
- Stand up a different type of service
  - `kubectl apply -f k8s-service-nodeport.yml` 
    - A "nodeport" service is used when accessing services from within your Kubernetes cluster.
  - `kubectl get service -l app=httpbin` - List the service just created along with the previous service.
    - Its "external IP" field will be "<none>"
- Create an SSL key and add it to Kubernetes.
  - If you're on a Mac, use `mkcert`:
    - `mkcert httpbin.k8s.orb.local`
    - This will create the files `httpbin.k8s.orb.local.pem` and `httpbin.k8s.orb.local-key.pem`.
  - Now upload the files as a "secret" in k8s and then label it:
    - `kubectl create secret tls httpbin-secret --key httpbin.k8s.orb.local-key.pem --cert httpbin.k8s.orb.local.pem`
    - `kubectl label secret httpbin-secret app=httpbin`
  - `kubectl get secret` - View the secret listing
  - `kubectl get secret -o yaml` - View the secret listing with extra details
- Stand up an Ingress point.
  - Ingress is used for the outside world to talk to your service.
  - Install Nginx ingress controller
    - `kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/cloud/deploy.yaml`
  - `kubectl apply -f k8s-ingress.yml` - Create our ingress
  - `kubectl get ingress` - Show our ingress.
- View what we made
  - `kubectl get all -l app=httpbin` - This will show everything we creted with our labels



## Troubleshooting

- `kubectl get all` is a greate way to start.
- Logs
  - For a specific pod
    - `kubectl get pods` - to get pod ID
    - `kubectl logs POD_ID`
    - `kubectl logs -f POD_ID` - Stream logs in real-time
  - To view all logs from all pods, install the app `stern`:
    - `brew install stern`
    - `stern -l app=httpbin`
  - Generating logs
    - `curl -s -I SERVICE_EXTERNAL_IP/anything?$(date +%Y%m%dT%H%M%S) |grep hostname`
      - This will show a datestamp in the URL which should show up in the logs
      - This will show different hostnames in the `x-app-hostname` header in the response.
- Scaling deployments up or down
  - `kubectl scale deployment/DEPLOYMENT_NAME --replicas=5`
- SSH
  - `kubectl get pods` - to get pod ID
  - `kubectl exec -it POD_ID -- /bin/bash` - to SSH in


## Issues

- For some reason, sometimes external IPs don't get created.
  - Apparently for LoadBalancer this is "normal" when running k8s in a dev environment, such as [OrbStack](https://orbstack.dev/).
- For some reason, I haven't had any luck getting HTTPS to work
  - ...this is probably because I don't get an external IP...


