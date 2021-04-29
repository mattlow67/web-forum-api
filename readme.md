## API for a Forum-Like Web Service
This project functions as a scalable API similar to those of large forum-style web applications such as Reddit. Throughout development, the team worked in a DevOps arrangement, with two members each handling a single microservice and one member acting as the operations role.

This API has a posting microservice and a voting microservice, the latter of which was my assignment. Both microservices were developed with the **Python Flask** web framework and SQLite. Requested links given to the API (using CURL and the HTTP POST and GET methods) call certain functions that interact with the SQL databases. In the posting microservice, POST methods can create new posts (with the values provided in the request) and delete posts, while GET methods can retrieve existing posts. The voting microservice, on the other hand, only deals with existing posts by manipulating their scores (which are analogous to upvotes and downvotes on Reddit), retrieving scores for requested posts, and ordering posts by their scores. 

Using Flask and python’s sqlite3 library, HTTP requests are converted to SQL commands. For example,  
```curl -i -X PUT -d 'vote=upvote' http://localhost:2015/votes/id/56```

is converted to  
```UPDATE posts SET upvotes=upvotes+1, score=score+1 WHERE id=56```

Separate databases are maintained for the microservices, and requested data is returned in the form of **JSON**, which can be easily parsed and manipulated on the web service’s end. In the event that a request cannot be fulfilled, an error message is returned (e.g., HTTP 404 Not Found.)

Unlike in the development state wherein Flask is used to run and test code, the production stage deploys a WSGI server (Gunicorn) that runs the microservices. Additionally, using Foreman, three separate instances of each microservice are instantiated for the purpose of load balancing. The Caddyfile assigns a unique port to either service, to which requests are sent after passing through the load balancer.

Team
- Developer 1: Jazmine Esqueda, Posting Microservice
- Developer 2: Matthew Low, Voting Microservice
- Operations: Johnathan Hernandez, Load Balancing

## How to Run
* **Note:** output from the terminal can be viewed in the txt files in the project folder
1. Install Flask, Gunicorn, and Foreman, and Caddy
   >https://palletsprojects.com/p/flask/  
   >https://docs.gunicorn.org/en/latest/install.html  
   >https://ddollar.github.io/foreman/  
   >https://github.com/caddyserver/caddy  
2. Navigate to the folder containing the source files, and run the commands
   >$ flask init  
   >$ flask run
   
![Screenshot_2021-04-28_10-56-39](https://user-images.githubusercontent.com/69742757/116467350-6e6f2980-a824-11eb-9ed7-d318214dac4f.png)  
3. Open another terminal, and run
   >$ foreman start -m caddy=1,votes=3,posts=3

![Screenshot_2021-04-28_10-57-28](https://user-images.githubusercontent.com/69742757/116467355-6f07c000-a824-11eb-9bde-8c83a77ecf45.png)

4. Run the test scripts
   >$ ./test_posts.sh  
   >$ ./test_votes.sh

![Screenshot_2021-04-28_10-58-33](https://user-images.githubusercontent.com/69742757/116467356-6fa05680-a824-11eb-932f-f1a8d12b2939.png)
![Screenshot_2021-04-28_11-01-38](https://user-images.githubusercontent.com/69742757/116467357-7038ed00-a824-11eb-9366-c08ab979f255.png)

5. Exit at any time using ctrl + c
6. After the first successful run, you can reset the databases by using
   >$ export FLASK_APP=posts  
   >$ flask init  
   >$ export FLASK_APP=votes  
   >$ flask init

   and reconfigure the .env file using 
   >$ FLASK_APP=\<app\>  
   >$ FLASK_ENV=development  
   >$ flask run \<or\> $ flask init  
