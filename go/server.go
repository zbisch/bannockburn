package main

import (
    "fmt"
    "net/http"
)

func handler(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintf(w, "Hi there, I love %s!", r.URL.Path[1:])
}

func main() {
    port := 8080
    fmt.Printf("Starting server on port %d...\n", port)

    http.HandleFunc("/", handler)
    http.ListenAndServe(":8080", nil)
}

