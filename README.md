# How to: Standalone Installation

## Install MySQL
**As a requiriment you need a mysql installation.**
After the installation complete, issue the following commands providing _usr_ and *pass*:
```
mysql> CREATE DATABASE app;
mysql> CREATE USER '<usr>'@'%' IDENTIFIED WITH mysql_native_password BY 'pass';
mysql> GRANT ALL PRIVILEGES ON *.* TO 'usr'@'%' WITH GRANT OPTION;
mysql> CREATE TABLE app.item (
    -> item_id INT AUTO_INCREMENT,
    -> date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    -> name VARCHAR(255),
    -> description VARCHAR(255),
    -> PRIMARY KEY(item_id)
    -> );
```

## Download the repo and build your image
```
git clone https://github.com/SimoneRoma/app-dtd.git
cd app-dtd
sudo docker build --network=host -t app .
```
## Run your image
```
sudo docker run -e USER=<your-user> -e PASS=<your-user-password> -e HOST=<mysql-host> -p 5000:5000 app
```

## Test
### Insert new Item
```
curl -k -X POST http://localhost:5000/v1/items -H "Content-Type: application/json" -d '{"name":"bug42","description":"prova42"}'
{
  "message": "Item created successfully."
}
```
### Get Item
```
curl http://192.168.1.148:5000/v1/items/1
{
  "date": "Sat, 25 Nov 2023 15:54:08 GMT",
  "description": "prova42",
  "id": 1,
  "name": "bug42"
}
```
# How to: k8s Installation
## Install MySQL
**As a requiriment you need a mysql installation.** If you like to test everything within your k8s environment we suggest to use this guide to install your mysql server: https://phoenixnap.com/kb/kubernetes-mysql.
After the installation complete, create the database:
```
mysql> CREATE DATABASE app;
mysql> CREATE USER '<usr>'@'%' IDENTIFIED WITH mysql_native_password BY 'pass';
mysql> GRANT ALL PRIVILEGES ON *.* TO 'usr'@'%' WITH GRANT OPTION;
mysql> CREATE TABLE app.item (
    -> item_id INT AUTO_INCREMENT,
    -> date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    -> name VARCHAR(255),
    -> description VARCHAR(255),
    -> PRIMARY KEY(item_id)
    -> );
```
For the sake of simplicity, throughout this tutorial we are going to use root credential (never do that in PROD).

## Install your app on k8s
You can install your app on any k8s distribution you like. This solution has been tested on a vanilla distribution. 
**This repo has an action to automatically upload a new "latest" tagged image to dockerhub at every push on the master branch**.
Keep the _imagePullPolicy: Always_ in your container spec always ensure that you download the most up to date image.
### Deploy the secrets
These secrets are consumed as environment variable inside the pod.
```
git clone https://github.com/SimoneRoma/app-dtd.git
cd app-dtd/example/k8s
kubectl apply -f secrets.yaml
```
### Deploy the application
```
kubectl apply -f deployment.yaml
```
### Deploy the service
```
kubectl apply -f service.yaml
```
## Test
Deploy a test pod to issue some curl against the app service
```
curl -k -X POST http://app:5000/v1/items -H "Content-Type: application/json" -d '{"name":"bug42","description":"prova42"}'
```
```
curl http://app:5000/v1/items/1
```
