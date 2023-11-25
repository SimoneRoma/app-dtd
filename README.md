# app-dtd

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


