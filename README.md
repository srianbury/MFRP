# MongoDB, Flask, React, Python
Super simple setup of with MongoDb, Flask, React, Python 3.6 Architecture

INTRODUCING THE MFRP STACK!

## Quickstart
0. In this repo directory run `npx create-react-app client` to make the react front end
0. `python -m virtualenv venv` (recommended but not required) to make a virtualenv
0. `venv\scripts\activate` to start the virtualenv
0. `pip install -r requirements.txt`
0. `python main.py` to start the server
0. `cd client` then `yarn start` to start client
0. Happy hacking!

### My application setup was taken mostly from Google Cloud's [Python/Flask docs](https://github.com/GoogleCloudPlatform/getting-started-python/tree/master/3-binary-data/bookshelf)
It's just enough to separate everything but still make it easy to read.
For any clarification check these two docs.  [GCP](https://cloud.google.com/python/getting-started/tutorial-app), [flask](http://flask.pocoo.org/docs/1.0/tutorial/layout/)

I really like their GCP's setup which is why I decided to use it.  Also if I decided to deploy to GCP it makes it really simple because it's already configure for it.

### Main differences between this setup and GCP's
0. I directly specify to use MongoDB.  In GCP's config.py file you set your db name string and in the code there is an if statement that loads the proper model for your db
0. I changed the name of `bookshelf` to `backend` to make it more generic

### MongoDB
[MongoDB Atlas](https://cloud.mongodb.com) has a free forever tier to get started!  It's an easy setup and you get 500MB to get your app started.


### Test