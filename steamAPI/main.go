package main

import (
	"log"
	"net/http"

	"github.com/rs/cors"
)

func main() {
	router := Router()
	client = Connect()

	c := cors.New(cors.Options{
		AllowedOrigins: []string{"*"},
		AllowedHeaders: []string{"*"},
		AllowedMethods: []string{"GET", "POST", "PUT", "DELETE", "OPTIONS"},
	})
	log.Fatal(http.ListenAndServe(":9100", c.Handler(router)))
}
