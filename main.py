import flask from Flask, jsonify, request
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect("dbname='sportsteams' user='user' host='localhost')
cursor = conn.cursor()

@app.route('/team/add', methods=['POST'])
def add_team():
  form = request.form
  name = form.get('name')
  if name == '':
    return jsonify('name is required!'), 400
  mascot = form.get('mascot')
  if mascot == '':
    return jsonify('name is required!'), 400
  city = form.get('city')
  state = form.get('state')
  champions_won = form.get('championsWon', '0')
  if championships_won.isnumeric():
    championships_won = int(championships_won)
  else:
    return jsonify('championsWon must be an integer'), 401
  
  cursor.execute('INSERT INTO nflteams (name, mascot, city, state, championshipsWon) VALUES (%s, %s, %s, %s, %s), (name, mascot, city, state, championships_won)')
  cursor.commit()
  return jsonify('Team added'), 200
    
@app.route('/team/<team_name>')
def get_team_by_name(team_name):
  results = cursor.execute("SELECT id, name, mascot, city, state, championsWon FROM nflteams WHERE name LIKE %s", [f'%{team_name}%'])
  results = cursor.fetchall()
  print(team_name)
                        
  return jsonify('team'), 200
                        
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
                        
CREATE TABLE IF NOT EXISTS NFLTeams (
  id serial PRIMARY KEY,
  name VARCHAR NOT NULL,
  mascot VARCHAR NOT NULL,
  city VARCHAR,
  state VARCHAR (2),
  championshipsWon SMALLINT DEFAULT 0
);
