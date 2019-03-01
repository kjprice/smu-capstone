const app = require('express')();
const fs = require('fs');

let server = null;
let port = null;
if (process.env.NODE_ENV === 'production') {
  server = require('https').createServer({
    key: fs.readFileSync('/etc/letsencrypt/live/asl-dictionary.net/privkey.pem', 'utf8'),
    cert: fs.readFileSync('/etc/letsencrypt/live/asl-dictionary.net/cert.pem', 'utf8'),
  }, app);
  port = 443;
} else {
  server = require('http').Server(app);
  port = 3000;
}

const io = require('socket.io')(server);
const spawn = require('child_process').spawn;

// https://www.sohamkamani.com/blog/2015/08/21/python-nodejs-comm/
let getClassificationPy = null;

function initPython() {
  getClassificationPy = spawn('python3', ['get_classification.py']);
  // note that we are reading from stderr because it emits data once,
  // while stdout emits multiple times
  getClassificationPy.stderr.on('data', (buffer) => {
    const data = buffer.toString();
    console.log(data);

    // check if the data format is a json array
    if (/^.+\|\|\[.*\]$/.test(data)) {
      sendClassifications(data);
    }
  });
  // also read from stdout for logging purposes
  getClassificationPy.stdout.on('data', (buffer) => {
    console.log(buffer.toString());
  });
}

initPython();

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/index.html');
});

function sendClassifications(data) {
  const response = data.split('||');
  const socketId = response[0];
  const classifications = JSON.parse(response[1]);
  io.to(socketId).emit('classification', classifications);
}

io.on('connection', (socket) => {
  socket.on('get-classification', (image) => {
    getClassificationPy.stdin.write(`${socket.id}||${image}\n`);
  });
});

server.listen(port, () => {
  console.log(`Server listening on *:${port}`);
});
