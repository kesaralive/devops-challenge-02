package main

import (
    "log"
    "net/http"
	"encoding/json"
    "github.com/gorilla/mux"
)

func HelloWorldHandler(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
    response := map[string]string{"message": "Hello from gorilla-mux-service!"}
    json.NewEncoder(w).Encode(response)
}

func main() {
    router := mux.NewRouter()
    router.HandleFunc("/", HelloWorldHandler).Methods("GET")

    log.Println("Starting server on :8080...")
    log.Fatal(http.ListenAndServe(":8080", router))
}
