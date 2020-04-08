package main

import (
	"flag"
	"github.com/grpc-ecosystem/grpc-gateway/runtime"
	"golang.org/x/net/context"
	"net/http"
)

var (
	echoEndPoint = flag.String("echo_endpoint", "localhost:50051", "endpoint of YourService")
)

func run() error {
	ctx := context.Background()
	ctx, cancel := context.WithCancel(ctx)
	defer cancel()

	mux := runtime.NewServeMux()
	return http.ListenAndServe(":8989", mux)

}

func main() {
	flag.Parse()
	run()
}
