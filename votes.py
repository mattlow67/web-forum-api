import flask, sqlite3, operator
from flask import request, jsonify, g
#from operator import itemgetter, attrgetter


app = flask.Flask(__name__)
# app.config.from_server('APP_CONFIG')
DATABASE = 'votes_posts.db'
RECORD = 'votes_db.sql'
COLUMNS = 'id, community, username, date, upvotes, downvotes, score'


def dict_factory(cursor, row):
	d = {}
	for idx, col in enumerate(cursor.description):
		d[col[0]] = row[idx]
	return d


def get_db():
	db = getattr(g, '_database', None)
	if db is None:
		db = g._database = sqlite3.connect(DATABASE)
		db.row_factory = dict_factory
	return db


# return a 200 OK response upon a successful operation
def make_OKresp(data):
	resp = jsonify(data)
	resp.status_code = 200
	resp.mimetype = "application/json"

	return resp


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
		with app.open_resource(RECORD, mode='r') as f:
			db.cursor().executescript(f.read())
		db.commit


@app.errorhandler(404)
def page_not_found(error=None):
	message = {
		'status' : 404,
		'message' : 'Not Found: ' + request.url,
	}
	resp = jsonify(message)
	resp.status_code = 404
	resp.mimetype = "application/json"

	return resp


@app.route('/votes', methods=['GET'])
def home():
	return '<h1>Home</h1>'


@app.route('/votes/all', methods=['GET'])
def api_all():
	all_posts = query_db(f'SELECT * FROM posts;')

	return make_OKresp(all_posts)


@app.route('/votes/id/<int:post_id>', methods=['GET', 'PUT'])
def api_post(post_id):
	query = f"SELECT {COLUMNS} FROM posts WHERE id=?;"
	args = []
	args.append(post_id)
	result = query_db(query, args)

	# requested post does not exist
	if result == []:
		return page_not_found(404)

	# put request for downvote/upvote
	if request.method == 'PUT':
		vote_parameter = request.form['vote']

		# track request downvotes/upvotes in db
		tracker_args = []
		tracker_args.append(post_id)
		tracker_args.append(vote_parameter)
		query_tracker = "INSERT INTO vote_tracker(post_id,vote_type) VALUES(?,?);"
		conn = sqlite3.connect(DATABASE)
		conn.execute(query_tracker,tracker_args)
		conn.commit()
		conn.close()

		# determine appropriate query
		if vote_parameter == 'upvote':
			query_vote = "UPDATE posts SET upvotes=upvotes+1, score=score+1 WHERE id=?;"
			result[0]['score'] += 1
			result[0]['upvotes'] += 1
		else:
			query_vote = "UPDATE posts SET downvotes=downvotes+1, score=score-1 WHERE id=?;"
			result[0]['score'] -= 1
			result[0]['downvotes'] += 1

		# increment score in db
		conn = sqlite3.connect(DATABASE)
		conn.execute(query_vote,args)
		conn.commit()
		conn.close()

		# message for successful post
		message = {
			'new score:' : result[0]['score'],
			'upvotes' : result[0]['upvotes'],
			'downvotes' : result[0]['downvotes'],
			'update status' : 200,
			'vote type' : vote_parameter,
		}
		resp = jsonify(message)
		resp.status_code = 200
		resp.mimetype = "application/json"
		
		return resp		

	return make_OKresp(result)


@app.route('/votes/<comm>/top/<int:max>', methods=['GET'])
def api_top(comm,max):
	query = f"SELECT {COLUMNS} FROM posts WHERE community=? ORDER BY score DESC LIMIT ?;"
	args = []
	args.append(comm)
	args.append(max)
	
	results = query_db(query, args)

	return make_OKresp(results)


@app.route('/votes/filter', methods=['GET'])
def api_filter():
	query_parameters = request.args

	id = query_parameters.get('id')
	community = query_parameters.get('community')
	username = query_parameters.get('username')
	date = query_parameters.get('date')

	query = f"SELECT {COLUMNS} FROM posts WHERE"
	to_filter = []

	if id:
		query += ' id=? AND'
		to_filter.append(id)
	if community:
		query += ' community=? AND'
		to_filter.append(community)
	if username:
		query += ' username=? AND'
		to_filter.append(username)
	if date:
		query += ' date=? AND'
		to_filter.append(date)
	if not (id or community or username or date):
		return page_not_found(404)

	query = query[:-4] + 'ORDER BY score DESC;'

	results = query_db(query, to_filter)

	return make_OKresp(results)


@app.route('/votes/voteid/all', methods=['GET'])
def api_voteid():
		query = "SELECT * FROM vote_tracker;"

		results = query_db(query)

		return make_OKresp(results)
