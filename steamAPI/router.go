package main

import (
	"encoding/json"
	"net/http"

	"github.com/gorilla/mux"
)

func fetchDocumenHandler(w http.ResponseWriter, r *http.Request) {
	payload := getAllDocuments()
	json.NewEncoder(w).Encode(payload)
}

// Route declaration
func Router() *mux.Router {
	r := mux.NewRouter()
	r.HandleFunc("/gameData", fetchDocumenHandler).Methods("GET")
	return r
}
