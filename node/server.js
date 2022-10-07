const http = require('http');
const fs = require('fs');
const { promisify } = require('util');

const server = http.createServer(async (req, res) => {
  //res.writeHead(200, {"Content-Type": "text/html"});
  res.statusCode = 200;
  res.setHeader("Content-Type", "text/html")

  const file = await promisify(fs.readFile)('$/public/Index.html')

  res.end(file)

}).listen(3000)

console.log("Server listening on port 3000")