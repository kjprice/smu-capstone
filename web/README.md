### Installation
```
npm install or yarn install
```
### Setup data directory
Make sure to add the labels in the `class_labels` directory.
And put the hdf5 models in the `models` directory.
Update `get_classification.py` for the path to the label and model.

### Running
```
node app.js
```
The app will then be accessible at `http://localhost:3000`

### EC2 deployment
Zip the whole directory and upload to ec2 server via scp
Install the python and dependencies
```
sudo yum install python36
sudo python3 -m pip install opencv-python
sudo python3 -m pip install keras
sudo python3 -m pip install --no-cache-dir tensorflow
```
Install nodejs and pm2
```
curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.32.0/install.sh | bash
. ~/.nvm/nvm.sh
nvm install 6.11.4
npm install -g pm2
```
Link the binaries so that it is accessible when running on `sudo`
```
sudo ln -s "$NVM_DIR/versions/node/$(nvm version)/bin/node" "/usr/bin/node"
sudo ln -s "$NVM_DIR/versions/node/$(nvm version)/bin/npm" "/usr/local/bin/npm"
sudo ln -s "$NVM_DIR/versions/node/$(nvm version)/bin/pm2" "/usr/local/bin/pm2"
```
Run the app via pm2
```
sudo pm2 start app.js
```
Stop the app on pm2
```
sudo pm2 stop app
```
