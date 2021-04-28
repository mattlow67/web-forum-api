#!/bin/sh

# Matthew Low
# Dev Role #2: Voting Microservice

# the database indentifies each post an integer ranging from 0 to 99
# GET a bunch of random posts and report their upvotes and downvotes
echo "\n\n\n**********GET several posts and dispaly their respective score**********"
curl -i http://localhost:2015/votes/id/74
curl -i http://localhost:2015/votes/id/89
curl -i http://localhost:2015/votes/id/56
curl -i http://localhost:2015/votes/id/47
curl -i http://localhost:2015/votes/id/23
# test ids that are out of range, and view 404 message
curl -i http://localhost:2015/votes/id/200
curl -i http://localhost:2015/votes/id/error

# fetch top votes in any community via GET
echo "\n\n\n**********GET votes for a community and limit the number fetched**********"
curl -i http://127.0.0.1:2015/votes/dolor/top/3
curl -i http://127.0.0.1:2015/votes/est/top/5
curl -i http://127.0.0.1:2015/votes/sit/top/2

# filter votes with specified arguments
echo "\n\n\n***************Filter votes by user-defined arguments***************"
curl -i http://localhost:2015/votes/filter?community=est&username=Dolorem
curl -i http://localhost:2015/votes/filter?community=adipisci
curl -i http://localhost:2015/votes/filter?date=180512

# send downvote and upvote requests via PUT requests
echo "\n\n\n**********Send upvote and downvote requests, and view their statuses**********"
curl -i -X PUT -d 'vote=upvote' http://localhost:2015/votes/id/56
curl -i -X PUT -d 'vote=downvote' http://localhost:2015/votes/id/56
curl -i -X PUT -d 'vote=downvote' http://localhost:2015/votes/id/56
curl -i -X PUT -d 'vote=upvote' http://localhost:2015/votes/id/23
curl -i -X PUT -d 'vote=downvote' http://localhost:2015/votes/id/47
curl -i -X PUT -d 'vote=upvote' http://localhost:2015/votes/id/89
curl -i -X PUT -d 'vote=upvote' http://localhost:2015/votes/id/74

# GET votes from above again, with their scores changed
echo "\n\n\n***************Votes for each post with their scores changed***************"
curl -i http://localhost:2015/votes/id/74
curl -i http://localhost:2015/votes/id/89
curl -i http://localhost:2015/votes/id/56
curl -i http://localhost:2015/votes/id/47
curl -i http://localhost:2015/votes/id/23

# view all upvotes and downvotes made, each of which has a unique vote_tracker id
echo "\n\n\n**********All downvotes and upvotes, each identified with a unique tracker id**********"
curl -i http://localhost:2015/votes/voteid/all
