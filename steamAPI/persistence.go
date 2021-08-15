package main

import (
	"log"

	"context"
	"fmt"

	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/bson/primitive"

	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
)

var client *mongo.Client

type GameStat struct {
	ID        primitive.ObjectID `bson:"_id"`
	Developer string
	GameTitle string
	Publisher string
	SteamData []SteamData
}

type SteamData struct {
	ID             primitive.ObjectID `bson:"_id"`
	CurrentUsers   string
	DailyPeakUsers string
	ListRank       int
	Timestamp      primitive.DateTime
}

func getAllDocuments() []GameStat {
	collection := client.Database("steamstore").Collection("game")

	cur, err := collection.Find(context.TODO(), bson.D{{}})
	if err != nil {
		log.Fatal(err)
	}
	var results []GameStat

	for cur.Next(context.TODO()) {
		//Create a value into which the single document can be decoded
		var gameStat GameStat
		err := cur.Decode(&gameStat)
		if err != nil {
			log.Fatal(err)
		}

		results = append(results, gameStat)
	}
	cur.Close(context.TODO())

	return results
}

func Connect() *mongo.Client {
	// Set client options
	clientOptions := options.Client().ApplyURI(
		//TODO: env configuration
		//fmt.Sprintf("mongodb://%s:%s", os.Getenv("MONGODB_HOST"), os.Getenv("MONGODB_PORT")))
		fmt.Sprintf("mongodb://%s:%s", "localhost", "27017"))

	// Connect to MongoDB
	client, err := mongo.Connect(context.TODO(), clientOptions)

	if err != nil {
		log.Fatal(err)
	}

	// Check the connection
	err = client.Ping(context.TODO(), nil)
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println("Connected to MongoDB!")
	return client
}
