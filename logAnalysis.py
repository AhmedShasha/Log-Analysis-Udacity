import psycopg2

# Most popular articles query:
fQuery = """create view popular_articles as
             select title, count(title) as num from articles join
             log on log.path = concat('/article/', articles.slug)
             group by title order by num desc limit 3;
             select * from popular_articles;
          """

# Most popular authors:
sQuery = """ create view top_authors as
              select name, count(name) as num from articles join
              authors on articles.author = authors.id join
              log on log.path = concat('/article/', articles.slug)
              group by name
              order by num desc limit 4;
              select * from top_authors;
          """

# Erorr:
tQuery = """create view error_percent as
             select main.date,(100.0*main.error/main.num)
             from (SELECT date_trunc('day', time) as date,
             count(id) as num,
             sum(case when status='404 NOT FOUND' then 1 else 0 end)
             as error from log group by date) as main
             where (100.0*main.error/main.num) >1;
             select * from error_percent;
          """

# Connect Function:
def connection(dbname="news"):
    """Connect to the PostgreSQL database and returns a database connection."""
    try:
        db = psycopg2.connect("dbname={}".format(dbname)) # *** Connetion Objects ***
        c = db.cursor()
        return db, c  # *** When database connect ***
    except:
        print("can't connect to database") # .... If Database Exsit ....


# Execute SQL query:
def Excuite(query):
    db, c = connect()
    c = db.cursor()
    c.execute(query)
    return cursor.fetchall()
    db.close()

# Execute The first query:
def popular_articles():

    """Prints most popular three articles of all time"""
    results = Excuite(fQuery)
    f.write(" Top popular articles : \n \n")
    for title, views in results:  #....... THE RESULT ........
        f.write("\t" + title + "--" + str(views) + " views \n")


# Execute first query:
def popular_authors():

    """Prints most popular article authors of all time"""
    results = excuite_queries(sQuery)
    f.write("\n Top three authors : \n \n")
    for author, views in results: #....... THE RESULT ........
        f.write("\t" + author + "--"+str(views) + " views \n")


# Execute third query:
def log_status():

    """Print days on which more than 1% of requests lead to errors"""
    results = excuite_queries(tQuery)
    f.write("\n Error > 1 % :\n \n")
    for date, error in results: #....... THE RESULT ........
        f.write("\t {0:%B %d, %Y} -- {1:.2f} % errors".format(date, error))

if __name__ == '__main__':

    popular_article()
    popular_authors()
    log_status()
