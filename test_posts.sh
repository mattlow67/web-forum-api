#!/bin/sh

# Jazmin Esqueda
# Dev Role #1: Posting Microservice

flask init

# Creating new posts using POST
echo "\n\n\n**********Creating new posts**********"
curl -d 'post_id=50&post_title=hello+from+the+web1&post_text=lets+add+more+posts&post_community=Primitive+web+post&post_url=www.localdevice.com&post_user_name=web_user1&post_date=03/03/2020' http://localhost:2015/posts/add_post
curl -d 'post_id=60&post_title=hello+from+the+web2&post_text=lets+add+more+posts&post_community=Primitive+web+post&post_url=www.localdevice.com&post_user_name=web_user1&post_date=03/03/2020' http://localhost:2015/posts/add_post
curl -d 'post_id=70&post_title=hello+from+the+web3&post_text=lets+add+more+posts&post_community=Primitive+web+post&post_url=www.localdevice.com&post_user_name=web_user1&post_date=03/03/2020' http://localhost:2015/posts/add_post
curl -d 'post_id=80&post_title=hello+from+the+web4&post_text=lets+add+more+posts&post_community=Primitive+web+post&post_url=www.localdevice.com&post_user_name=web_user1&post_date=03/03/2020' http://localhost:2015/posts/add_post


echo "\n\n\n**********Testing Creating new posts**********"
# test creating new post
curl -d 'post_id=50&post_title=hello+from+the+web1&post_text=lets+add+more+posts&post_community=Primitive+web+post&post_url=www.localdevice.com&post_user_name=web_user1&post_date=03/03/2020' http://localhost:2015/posts/add_post

 Delete Existing post
echo "\n\n\n**********Deleting Post**********"
curl -i http://localhost:2015/posts/delete_post?post_id=1
curl -i http://localhost:2015/posts/delete_post?post_id=2
curl -i http://localhost:2015/posts/delete_post?post_id=3


# Retrieve Post Given ID
echo "\n\n\n**********Retrieve Post Given ID**********"
curl -i http://localhost:2015/posts/get_post?post_id=6
curl -i http://localhost:2015/posts/get_post?post_id=7
curl -i http://localhost:2015posts/get_post?post_id=8

# List the 2 most recent posts to particular community
echo "\n\n\n***************List the 5 most recent posts to particular community***************"
curl -i http://localhost:2015/posts/Math/top/5



# List the 5 most recent posts to any community
echo "\n\n\n***************List the 5 most recent posts to any community***************"
curl -i http://localhost:2015/posts/get_Recent?n=5

