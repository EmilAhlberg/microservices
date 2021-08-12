docker pull mongo


docker run --name mongo-db -p 27017:27017 -d mongo:latest

#install go
wget??
sudo tar -C /usr/local -xzf go1.16.4.linux-amd64.tar.gz
export PATH=$PATH:/usr/local/go/bin


#init go
go mod init github.com/emilahlberg/todo-service

#install mongodb-go-driver: 'recommended'
go get go.mongodb.org/mongo-driver

# gorilla/mux popular and straightforward
go get -u github.com/gorilla/mux







# atom
go-plus
prettier-eslint
