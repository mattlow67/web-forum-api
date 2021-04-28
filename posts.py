import flask
from flask import request, jsonify, g
import sqlite3


app = flask.Flask(__name__)
#app.config.from_envvar('APP_CONFIG')
DATABASE = 'posts.db'

def make_dicts(cursor, row):
    return dict((cursor.description[idx][0], value)
                for idx, value in enumerate(row))


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = make_dicts
    return db
    
    
#returns 200 OK response if successful  
def send_ok200(data):
	response = jsonify(data)
	response.status_code = 200
	response.mimetype = "application/json"
	return response
	
	
	
# error message
@app.errorhandler(404)	
def page_not_found(error = None):
	message = { 
	'status: ': 404,
	'message: ': 'Not Found: ' + request.url
	}
	response = jsonify(message)
	response.status_code = 404
	response.mimetype = "application/json"
	return response
	
	
# conflict message
def conflict_409():
	message = { 
	'status: ': 409,
	'message: ': 'Conflict: ' + request.url
	}
	response = jsonify(message)
	response.status_code = 409
	response.mimetype = "application/json"
	return response

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


@app.cli.command('init')
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('posts.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


@app.route('/posts', methods=['GET'])
def home():
    return '''<h1>HOME</p>'''

# returns all posts in database
@app.route('/posts/all', methods=['GET'])
def app_all():

	all_posts = query_db('SELECT * FROM posts;')
	return send_ok200(all_posts)
	if get_post == []:
			return page_not_found(404)

	
	
# --------------deleting post by ID------------------	
@app.route('/posts/delete_post', methods=['GET'])
def delete_post():
	query_parameters = request.args
	post_id = query_parameters.get('post_id')
	
	
	# checks for existance of post the user is trying to delete
	get_post = query_db('SELECT post_id FROM posts WHERE post_id =?;', (post_id,))
	if get_post == []:
			return page_not_found(404)

	conn = sqlite3.connect(DATABASE)
	conn.execute("DELETE FROM posts WHERE post_id =?;", (post_id,))
	conn.commit()
	conn.close()
	
	return send_ok200(get_post)


# -------------end of deleting post by ID----------------------	
	
	
	
	
# --------------RETRIEVING POST BY ID------------------	
@app.route('/posts/get_post', methods=['GET'])
def get_post():
	query_parameters = request.args
	post_id = query_parameters.get('post_id')
	get_post = query_db('SELECT post_id, post_title, post_community, post_user_name, post_date FROM posts WHERE post_id =?;', (post_id))
	# checks if post exists
	if get_post == []:
			return page_not_found(404)
	return send_ok200(get_post)



# ----------------END OF RETRIEVING POST BY ID---------------------------------------

# --------------LIST THE N MOST RECENT POSTS TO A TO A PARTICULAR COMMUNITY------------------	
@app.route('/posts/<comm>/top/<int:max>', methods=['GET', 'POST'])
def get_top(comm,max):
	query = "SELECT post_id, post_title, post_community, post_user_name, post_date FROM posts WHERE post_community = ? ORDER BY post_date DESC LIMIT ?;"
	
	args = []
	args.append(comm)
	args.append(max)
	get_post = query_db(query, args)
	# checks if empty
	if get_post == []:
			return page_not_found(404)
	return send_ok200(get_post)


# -------------end of LIST THE N MOST RECENT POSTS TO A TO A PARTICULAR COMMUNITY----------------------

# --------------LIST THE N MOST RECENT POSTS FROM ALL COMMUNITIES------------------	
@app.route('/posts/get_Recent', methods=['GET'])
def get_Recent():
	query_parameters = request.args
	n = query_parameters.get('n')
	get_post = query_db('SELECT post_id, post_title, post_community, post_user_name, post_date FROM posts ORDER BY post_date DESC LIMIT ?;', (n))
	# checks if empty
	if get_post == []:
			return page_not_found(404)
	return send_ok200(get_post)


# -------------end of LIST THE N MOST RECENT POSTS FROM ALL COMMUNITIES--------------------






#---------------------ADD POST TO DATABASE---------------------
@app.route('/posts/add_post', methods=['GET', 'POST'])
def add_post():
	if request.method == 'POST':
	
		post_id = request.form['post_id']
		post_title = request.form['post_title']
		post_text = request.form['post_text']
		post_community = request.form['post_community']
		post_url = request.form['post_url']
		post_user_name = request.form['post_user_name']
		post_date = request.form['post_date']
		
		# checks to see if post with this ID already exists
		query= "SELECT post_title FROM posts WHERE post_id =?;"
		check = query_db(query, (post_id,))
		if check == []:
			
	
			# add input to list
			input_args = []
			input_args.append(post_id)
			input_args.append(post_title)
			input_args.append(post_text)
			input_args.append(post_community)
			input_args.append(post_url)
			input_args.append(post_user_name)
			input_args.append(post_date)
			
			
			query= "INSERT INTO posts(post_id, post_title, post_text, post_community, post_url, post_user_name, post_date) VALUES(?,?,?,?,?,?,?);"
			conn = sqlite3.connect(DATABASE)
			conn.execute(query, input_args)
			conn.commit()
			conn.close()
		
		else: return conflict_409()
		
		# message for successful post upload
		message = {
			'Post ID: ' : post_id,
			'Post Title: ': post_title,
			'Post Text: ': post_text,
			'Post Community: ': post_community, 
			'Post URL: ': post_url,
			'Post User Name: ': post_user_name,
			'Post Date': post_date
		}
		

		return send_ok200(message)
#---------------------END OF ADD POST TO DATABASE---------------------
