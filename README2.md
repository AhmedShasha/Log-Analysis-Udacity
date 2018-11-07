# LogAnalysis Project

### Tools 
```
1-Python 
2-VirtualMachine
3-Vagrant 
4-PostgreSQL
5-Database newsdata.sql
```
### Install

1- Download and Install .[Vagrant](https://www.vagrantup.com/) and .[VirtualBox](https://www.virtualbox.org/)
2- Download or clone from github .[fullstack-nandegree-vm repository](https://github.com/udacity/fullstack-nanodegree-vm)
3- Download and Install .[PostgreSQL](https://www.postgresql.org/download/)
4- Download database from here .[newsdata](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

### Run 
```
1-Go to vagrant
2-Vagrant up then vagrant ssh
3-Go to Project file and run it 
```

### Views 
```
1-pp_article = """create view pep_articles as
                      select articles.t, count(articles.t)
                      as num from articles
                      join log on log.path like concat('%', articles.slug, '%')
                      group by articles.t
                      order by num DESC limit 8;
                      select * from pep_articles;
          """
                      
2-pp_author = """ create view pep_authors as
                     select authors.n, count(*)
                     as num from articles
                     join authors on articles.author = authors.id
                     join log on log.path like concat('%', articles.slug, '%')
                     group by authors.n
                     order by num DESC;
                     select * from pep_authors;
          """ 
                     
3-qq_errors = """create view que_error as
                  select main.date,(100.0*main.error/main.num)
                  from (select date_trunc('day', time) as date,
                  count(id) as num,
                  sum(case when status='404 NOT FOUND' then 1 else 0 end)
                  as error from log group by date) as main
                  where (100.0*main.error/main.num) >1;
                  select * from que_error;
          """

```
