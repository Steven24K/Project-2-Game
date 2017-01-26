import psycopg2, psycopg2.extras, sys

try:
    conn = psycopg2.connect("dbname='pygame' user='postgres' password='root'")
except:
    print ("no connection")

ccp = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
try:
    ccp.execute("""SELECT p_id, p_name, p_score FROM player""")
except:
    print("I can't select players")

cch = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
try:
    cch.execute("""SELECT h_id, h_name, h_score FROM highscore""")
except:
    print("I can't select highscore")

# fetch all of the rows from the query
data_p = ccp.fetchall()
data_h = cch.fetchall()

# get player rows
for row in data_p:
    if row[0] == 1:
        player1_name = row[1]
        player1_score = row[2]
    elif row[0] == 2:
        player2_name = row[1]
        player2_score = row[2]
    elif row[0] == 3:
        player3_name = row[1]
        player3_score = row[2]
    elif row[0] == 4:
        player4_name = row[1]
        player4_score = row[2]

# get highscore rows
for row in data_h:
    if row[0] == 1:
        h_player1_name = row[1]
        h_player1_score = row[2]
    elif row[0] == 2:
        h_player2_name = row[1]
        h_player2_score = row[2]
    elif row[0] == 3:
        h_player3_name = row[1]
        h_player3_score = row[2]
    elif row[0] == 4:
        h_player4_name = row[1]
        h_player4_score = row[2]

# update score
def update_score(name, score):
    try:
        ccp.execute("""UPDATE player SET p_score=%s WHERE p_name=%s""", (score, name))
    except Exception as error:
        print(error)
    conn.commit()

# check name
def check_name(name):
    try:
        ccp.execute("""SELECT count(p_name) FROM player WHERE p_name=%s""", (name))
    except Exception as error:
        return(error)

# insert player name
def insert_name(name):
    try:
        ccp.execute("""insert into player(p_name) values (%s)""", (name))
    except Exception as error:
        print(error)
    conn.commit()

# update player name
def update_name(name, id):
    try:
        ccp.execute("""UPDATE player SET p_name='%s' WHERE p_id = %s""", (name, id))
    except Exception as error:
        print(error)
    conn.commit()

#reset score
def reset():
    try:
        cc.execute("""UPDATE player SET score=%s WHERE name=%s""", (0, 'player1'))
    except Exception as error:
        print(error)
    conn.commit()
#reset()