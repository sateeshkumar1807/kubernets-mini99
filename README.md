# Student Management Kubernetes Project (Beginner)

This project follows the uploaded guide: a small Flask web app packaged with Docker and deployed to a local Kubernetes cluster using Minikube.

## What you will learn
- Docker image and container
- Kubernetes Namespace, Deployment, ReplicaSet, Pod, and NodePort Service
- Labels/selectors, readiness/liveness probes, resource requests/limits
- Scaling, Pod replacement, logs, and rollout/rollback

## Prerequisites
Install and start Docker Desktop, kubectl, and Minikube on Windows 11. Open PowerShell after installation.

## 1. Open the project folder
Extract this ZIP, then open PowerShell in the `student-kubernetes-beginner` folder. Verify:
```powershell
dir
```
You should see `app.py`, `requirements.txt`, `Dockerfile`, and `k8s`.

## 2. Start Minikube
```powershell
minikube start --driver=docker
kubectl get nodes
```
Wait until the node status is `Ready`.

## 3. Build the image inside Minikube
Run this from the project root:
```powershell
minikube image build -t student-app:v1 .
minikube image ls
```
The image is built in Minikube's image environment, so no Docker Hub push is needed.

## 4. Create the namespace and application
```powershell
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

## 5. Check the resources
```powershell
kubectl get all -n student-app
kubectl get pods -n student-app -o wide
kubectl get replicasets -n student-app
kubectl get services -n student-app
kubectl rollout status deployment/student-deployment -n student-app
```
Wait for all three Pods to show `Running` and `1/1` Ready.

## 6. Open the website
```powershell
minikube service student-service -n student-app
```
Minikube should open the application URL in your browser. You can also test the health endpoint by opening `/health` at that URL; it should return `{"status":"healthy"}`.

## 7. Beginner practice exercises

### A. Delete one Pod (Kubernetes should replace it)
```powershell
kubectl get pods -n student-app
kubectl delete pod POD_NAME -n student-app
kubectl get pods -n student-app -w
```
Replace `POD_NAME` with a real Pod name. Press Ctrl+C to stop watching.

### B. Scale from three Pods to five
```powershell
kubectl scale deployment student-deployment --replicas=5 -n student-app
kubectl get pods -n student-app
```
Return to three afterward:
```powershell
kubectl scale deployment student-deployment --replicas=3 -n student-app
```

### C. View application logs
```powershell
kubectl logs deployment/student-deployment -n student-app
```

### D. Check why a Pod is not starting
```powershell
kubectl describe pods -n student-app
kubectl get events -n student-app --sort-by=.metadata.creationTimestamp
```

## Important concepts in simple words
- **Image:** packaged application template.
- **Container:** running instance of the image.
- **Pod:** Kubernetes unit that runs the container.
- **Deployment:** maintains the desired number of Pods and manages updates.
- **ReplicaSet:** helps maintain the number of replicas requested by the Deployment.
- **Service:** stable way to reach matching Pods.
- **Namespace:** logical area used to group project resources.
- **Label/selector:** matching key used by a Service/Deployment to find Pods.
- **Readiness probe:** checks whether the app is ready to receive traffic.
- **Liveness probe:** checks whether the app should be restarted.
- **Requests/limits:** describe expected and maximum CPU/memory for the container.

## Cleanup when finished
This deletes the project's Kubernetes resources:
```powershell
kubectl delete namespace student-app
```
Stop Minikube if you are done for now:
```powershell
minikube stop
```

## Troubleshooting
- **ImagePullBackOff:** make sure you ran `minikube image build -t student-app:v1 .` from the project root and that the image tag matches `deployment.yaml`.
- **Pods not Ready:** inspect `kubectl describe pod POD_NAME -n student-app` and `kubectl logs POD_NAME -n student-app`.
- **Website does not open:** try `minikube service student-service -n student-app`; check `kubectl get pods,svc -n student-app`.
- **YAML errors:** keep the spaces/indentation exactly as shown; use spaces, not tabs.

The project intentionally does not include AWS, Terraform, CI/CD, or a database, so you can focus on core Kubernetes concepts first.
