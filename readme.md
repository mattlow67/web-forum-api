## API for a Forum-Like Web Service
This project functions as a scalable API similar to those of large forum-style web applications such as Reddit. Throughout development, the team worked in a DevOps arrangement, with two members each handling a single microservice and one member acting as the operations role by tying everything together.

This API has a posting microservice and a voting microservice, the latter of which was my assignment. Both microservices were developed with **Python Flask** web framework and function similarly. Requested links given to the API (using CURL and the HTTP POST method) call certain functions in either program. In the posting microservice, POST methods can create new posts (with the values provided) and delete posts, while GET methods can retrieve existing posts. The voting microservice, on the other hand, only deals with existing posts by manipulating their scores (which are analogous to upvotes and downvotes on Reddit), retrieving scores for requested posts, and ordering requested posts by their scores. 

Using Flask and python’s sqlite3 library, HTTP requests are converted to SQL commands. For example,
>curl -i -X PUT -d 'vote=upvote' http://localhost:2015/votes/id/56
is converted to 
>UPDATE posts SET upvotes=upvotes+1, score=score+1 WHERE id=56

Separate databases are maintained for the microservices, and requested data is returned in the form of **JSON**, which can be easily parsed and manipulated on the web service’s end. In the event that a request cannot be fulfilled, an error message is returned (e.g., HTTP 404 Not Found).

Unlike in the development state wherein Flask is used to run and test code, the production stages deploys WSGI server (Gunicorn) to execute the microservices. Additionally, using Foreman, three separate instances of each microservice are instantiated for the purpose of load balancing. The Caddyfile assigns a unique port to either service, to which requests are sent after passing through the load balancer.

Team
- Developer 1: Jazmine Esqueda, Posting Microservice
- Developer 2: Matthew Low, Voting Microservice
- Operations: John Hernandez, Load Balancing

## How to Run
- output from the terminal can be viewed in the txt files in the project folder
1. Install Flask, Gunicorn, and Foreman, and Caddy
>https://palletsprojects.com/p/flask/
>https://docs.gunicorn.org/en/latest/install.html
>https://ddollar.github.io/foreman/
>https://github.com/caddyserver/caddy
2. Navigate to the folder containing the source files, and run the commands
>$ flask init
>$ flask run
**IMAGE GOES HERE**
3. Open another terminal, and run
>$ foreman start -m caddy=1,votes=3,posts=3
**IMAGE GOES HERE**
4. Run the test scripts
>$ ./test_posts.sh
>$ ./test_votes.sh
**IMAGE GOES HERE**
5. Exit at any time using ctrl + c
6. After the first successful run, you can reset the databases by using
>$ export FLASK_APP=posts
>$ flask init
>$ export FLASK_APP=votes
>$ flask init
and reconfigure the .env file using 
>$ FLASK_APP=<app>
>$ FLASK_ENV=development
>$ flask run <or> $ flask init