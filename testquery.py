import psycopg2

# This function tests to make sure that you can connect to the database
def test_connection():
    
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="yangl4",
        user="yangl4",
        password="stars929bond")

    if conn is not None:
        print( "Connection Worked!" )
    else:
        print( "Problem with Connection" )

    conn.commit()
    conn.close()
    return None

def test_query_one():

    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="yangl4",
        user="yangl4",
        password="stars929bond")

    cur = conn.cursor()

    sql = """SELECT county, state, trump16 FROM elections WHERE trump16 IS NOT NULL AND trump16 > 0.75 ORDER BY trump16 DESC;"""

    cur.execute( sql )

    row = cur.fetchone()

    if row == None:
        print("No counties voted for Trump in 2016 by more than 75%")
    else:
        print("The county {}, {} voted the most for Trump in 2016 by {:.2f}%.".format(row[0], row[1], round(row[2], 4)*100))
    
    conn.commit()
    cur.close()
    conn.close()
    return None

def test_query_two():

    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="yangl4",
        user="yangl4",
        password="stars929bond")

    cur = conn.cursor()

    sql = """SELECT county, state, trump20, biden20, totalpop FROM elections WHERE trump20 IS NOT NULL AND biden20 IS NOT NULL AND totalpop IS NOT NULL ORDER BY totalpop DESC;"""
    
    cur.execute( sql )

    row = cur.fetchone()

    if row == None:
        print("Something went wrong...")
    else:
        print("In 2020, the county {}, {} had the highest population of {}. They voted for Tump by {:.2f}% and Biden by {:.2f}%.".format(row[0], row[1], row[4], round(row[2], 4)*100, round(row[3], 4)*100))
   
    conn.commit()
    cur.close()
    conn.close()
    return None
    
def test_query_three():

    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="yangl4",
        user="yangl4",
        password="stars929bond")

    cur = conn.cursor()

    sql = """SELECT county, state, trump16, clinton16, totalvote16 FROM elections WHERE trump16 IS NOT NULL AND clinton16 IS NOT NULL AND totalvote16 IS NOT NULL ORDER BY totalvote16 DESC;"""
    
    cur.execute( sql )

    row = cur.fetchone()

    if row == None:
        print("Something went wrong...")
    else:
        print("In 2016, the county {}, {} voted the most in total number of {}. They voted for Trump by {:.2f)% and Clinton by {:.2f}%.".format(row[0], row[1], row[4], round(row[2], 4)*100, round(row[3], 4)*100))

    conn.commit()
    cur.close()
    conn.close()
    return None    

def test_query_four():

    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="yangl4",
        user="yangl4",
        password="stars929bond")

    cur = conn.cursor()

    sql = " SELECT * FROM elections WHERE trump16 IS NOT NULL AND clinton16 IS NOT NULL ORDER BY black DESC"
    
    cur.execute( sql )

    row = cur.fetchone()

    if row == None:
        print("Something went wrong...")
    else:
        print("The county with the highest percentage of Black people voted for Trump", row[2], "and Clinton", row[3], "in 2016.")

    conn.commit()
    cur.close()
    conn.close()
    return None
    
def test_query_five():

    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="yangl4",
        user="yangl4",
        password="stars929bond")

    cur = conn.cursor()

    sql = " SELECT * FROM elections WHERE state = 'NY' ORDER BY trump20 ASC "
    
    cur.execute( sql )

    row = cur.fetchone()

    if row == None:
        print("Something went wrong, try again")
    else:
        print( " The county", row[0],"had the lowest number of votes towards Trump in New York by", row[2])

    conn.commit()
    cur.close()
    conn.close()
    return None

test_connection()
test_query_one()
test_query_two()
test_query_three()
'''test_query_four()
test_query_five()'''
