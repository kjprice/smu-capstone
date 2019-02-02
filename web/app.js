const app = require('express')();
const http = require('http').Server(app);
const io = require('socket.io')(http);
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
    if (/^\[.*\]$/.test(data)) {
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
  io.sockets.emit('classification', JSON.parse(data));
}

io.on('connection', (socket) => {
  socket.on('get-classification', (image) => {
    getClassificationPy.stdin.write(`${image}\n`);
  });
});

http.listen(3000, () => {
  console.log('Server listening on *:3000');
});
