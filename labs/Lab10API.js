const http = require("http");
const os = require("os");
const ip = require('ip');
const data = require("./widgets.json");

const server = http.createServer((req, res) => {
    if (req.url === "/") {

        res.writeHead(200, {"Content-Type": "text/json"});
        res.end(JSON.stringify(data));        

      } else if (req.url === "/api") {
        res.writeHead(200, {"Content-Type": "text/html"});

        myHostName=os.hostname();
        serverUptime = os.uptime();        
        reducedDays = Math.floor(serverUptime / 86400);
        reducedHours = Math.floor(serverUptime / 3600) - reducedDays * 24;
        reducedMinutes = Math.floor(serverUptime / 60) - reducedDays * 1440 - reducedHours * 60;
        reducedSeconds = serverUptime - reducedDays * 86400 - reducedHours * 3600 - reducedMinutes * 60;
        totalMemory = (os.totalmem() / (1024**2)).toFixed(3);
        freeMemory = (os.freemem() / (1024**2)).toFixed(3);
        numCPUs = os.cpus().length;
        
        html=`    
        <!DOCTYPE html>
        <html>
        <head>
            <title>Node JS Response</title>
        </head>
        <body>
            <p>Hostname: ${myHostName}</p>
            <p>IP: ${ip.address()}</p>
            <p>Server Uptime: Days: ${reducedDays}, Hours: ${reducedHours}, Minutes: ${reducedMinutes}, Seconds: ${reducedSeconds}</p>
            <p>Total Memory: ${totalMemory} MB</p>
            <p>Free Memory: ${freeMemory} MB</p>
            <p>Number of CPUs: ${numCPUs}</p>
        </body>
        </html>`
        
        res.end(html);  

      } else {

        res.writeHead(404, {"Content-Type": "text/plain"});
        res.end("Data not found");       

      }    
});

server.listen(3000);
console.log("Server listening on port 3000");