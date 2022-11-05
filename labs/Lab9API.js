const http = require("http");
const data = require("./widgets.json");

const server = http.createServer((req, res) => {
    if (req.url === "/") {
        res.writeHead(200, {"Content-Type": "text/json"});
        res.end(JSON.stringify(data));        
      } else {
        res.writeHead(404, {"Content-Type": "text/plain"});
        res.end("Data not found");        
      }    
});

server.listen(3000);
console.log("Server listening on port 3000");