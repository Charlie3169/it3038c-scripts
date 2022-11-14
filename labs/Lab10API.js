const http = require("http");
const data = require("./widgets.json");
const os = require("os");
const ip = require('ip');

const config = require('config')
var express = require('express')
var app = express()

app.set('port', (process.env.PORT || 5000))
app.use(express.static(__dirname + '/public'))

app.get('/', function(request, response) {
    response.send
    (
        '<b>Hello World! My name is:<em>' + process.env.MYNAME + '</em> <br /> My Node Environment is:<em>' 
        + config.util.getEnv('NODE_ENV') + '</em></b>'
        + '<br/><br/>' +'<b><a href="/sysinfo">Get system info!</a></b>'
    )
})



app.get('/api', (request, response) => {
    response.send(JSON.stringify(data))    
})

app.get('/sysinfo', (request, response) => {   

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
    
    response.send(html);      
})

app.listen(app.get('port'), function() {
    console.log("Node app is running at localhost:" + app.get('port'))
})

