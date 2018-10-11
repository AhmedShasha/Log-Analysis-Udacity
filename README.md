# LogAnalysis Project
## Udacity-First-Project
### Tools 
```
1-Python 
2-VirtualMachine
3-Vagrant 
4-PostgreSQL
```
### Install

* Insrall .[Vagrant](https://www.vagrantup.com/) and .[VirtualBox](https://www.virtualbox.org/)
* Download or clone from github .[fullstack-nandegree-vm repository](https://github.com/udacity/fullstack-nanodegree-vm)
* Download and Install .[PostgreSQL](https://www.postgresql.org/download/)

### Run 
```
1-Change directory to vagrant
2-Vagrant up command to run then vagrant ssh
3-Go to Project file and run by command " python logAnalysis.py "
```

### Views 
```
1-Create view pep_articles "" create view pep_articles as
                      select articles.title, count(articles.title)
                      as number from articles
                      join log on log.path like concat('%', articles.slug, '%')
                      group by articles.title
                      order by number DESC limit 8;
                      select * from pep_articles; ""
                      
2-Create view pep_authors "" create view pep_authors as
                     select authors.name, count(*)
                     as number from articles
                     join authors on articles.author = authors.id
                     join log on log.path like concat('%', articles.slug, '%')
                     group by authors.name
                     order by number DESC;
                     select * from pep_authors; ""
                     
3-Create view que_error  "" create view que_error as
                  select main.date,(100.0*main.error/main.num)
                  from (select date_trunc('day', time) as date,
                  count(id) as num,
                  sum(case when status='404 NOT FOUND' then 1 else 0 end)
                  as error from log group by date) as main
                  where (100.0*main.error/main.num) >1;
                  select * from que_error; ""
```
