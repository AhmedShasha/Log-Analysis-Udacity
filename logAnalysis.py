import psycopg2


# What are the most popular three articles of all time?

p_articles = """create view pep_articles as
                      select articles.title, count(articles.title)
                      as number from articles
                      join log on log.path like concat('%', articles.slug, '%')
                      group by articles.title
                      order by number DESC limit 8;
                      select * from pep_articles;
          """


# Who are the most popular article authors of all time?

p_authors = """ create view pep_authors as
                     select authors.name, count(*)
                     as number from articles
                     join authors on articles.author = authors.id
                     join log on log.path like concat('%', articles.slug, '%')
                     group by authors.name
                     order by number DESC;
                     select * from pep_authors;
          """


# On which days did more than 1% of requests lead to errors?
q_error = """create view que_error as
                  select main.date,(100.0*main.error/main.num)
                  from (select date_trunc('day', time) as date,
                  count(id) as num,
                  sum(case when status='404 NOT FOUND' then 1 else 0 end)
                  as error from log group by date) as main
                  where (100.0*main.error/main.num) >1;
                  select * from que_error;
          """


# Create file to send output

f = open('output.txt', 'w')


# Connection Function
def connection(dbname="news"):
    """Connect to the PostgreSQL database and returns a database connection."""
    try:
        db = psycopg2.connect(
            "dbname={}".format(dbname))   # ** Connetion Objects *
        c = db.cursor()
        return db, c    # ** When database connect *
    except:
        print("can't connect to database")   # ** If Database Not Exsit *


# # Execute SQL query:

def excuite_queries(query):
    db, c = connection()
    c = db.cursor()
    c.execute(query)
    return c.fetchall()
    db.close()


# Execute First query:

def p_articles_result(query):

    results = excuite_queries(query)  # ** Most 8 articles of all time *

    f.write("\n Most eight articles : \n \n")

    for title, views in results:   # ** THE RESULT *
        f.write("\t" + title + "--" + str(views) + " views \n")


# Execute Second query:

def p_authors_result(query):

    results = excuite_queries(query)
    f.write("\n Most authors : \n \n")
    for author, views in results:    # ** THE RESULT *
        f.write("\t" + author + "--"+str(views) + " views \n")


# Execute Third query :
def q_error_result(query):

    results = excuite_queries(query)
    f.write("\n Error percent more than 1 % :\n \n")
    for date, error in results:     # ** THE RESULT *
        f.write("\t {0:%B %d, %Y} -- {1:.2f} % errors".format(date, error))


if __name__ == '__main__':
    p_articles_result(p_articles)
    p_authors_result(p_authors)
    q_error_result(q_error)

f.close()   # ** CLOSE FILE *
