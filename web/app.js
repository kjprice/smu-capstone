const app = require('express')();
const http = require('http').Server(app);
const io = require('socket.io')(http);

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/index.html');
});

function sendClassification() {
  const letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
  const randomLetter = () => letters[Math.floor(Math.random() * 26)];
  const randomProbability = (max, offset) => (Math.random() * max + offset).toFixed(2);

  const data =  [
    { value: randomLetter(), probability: randomProbability(33, 66) },
    { value: randomLetter(), probability: randomProbability(33, 33) },
    { value: randomLetter(), probability: randomProbability(33,  0) },
  ];

  io.sockets.emit('classification', data);
}

io.on('connection', (socket) => {
  socket.on('get-classification', (image) => {
    setTimeout(sendClassification, 1000);
  });
});

http.listen(3000, () => {
  console.log('Server listening on *:3000');
});
