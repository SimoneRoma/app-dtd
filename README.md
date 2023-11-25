# app-dtd

Download the repo and build your image
sudo docker build --network=host -t app .

Run your image
sudo docker run -e USER=<your-user> -e PASS=<your-user-password> -e HOST=<mysql-host> -p 5000:5000 app
