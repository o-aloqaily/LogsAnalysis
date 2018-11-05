#!/usr/bin/env python
import psycopg2


def getTopThreeArticles(conn):
    cur = conn.cursor()
    cur.execute(
        """
        select a.title, count(*) as views
        from articles as a join log as l on l.path LIKE CONCAT('%', a.slug)
        group by a.title
        order by count(*) desc
        limit 3;
        """
    )
    results = cur.fetchall()
    for article in results:
        title = article[0]
        views = article[1]
        print("\"%s\" - %s views." % (title, views))


def getTopAuthors(conn):
    cur = conn.cursor()
    cur.execute(
        """
        select au.name, count(*) as Views
        from authors as au
        join articles as ar on au.id = ar.author
        join log as lo on lo.path LIKE CONCAT('%', ar.slug)
        group by au.name
        order by Views desc
        """
    )
    results = cur.fetchall()
    for author in results:
        name = author[0]
        views = author[1]
        print("%s - %s views" % (name, views))


def getDaysWithMostErrors(conn):
    cur = conn.cursor()
    cur.execute(
        """
        select * from (
            select
                totalReq.day,
                (100*totalErr.num::float/totalReq.num::float)
                as error_percentage
            from
                (
                    select DATE(time) as day, count(*) as num
                    from log
                    group by day
                ) as totalReq,
                (
                    select DATE(time) as day, count(*) as num
                    from log
                    where status = '404 NOT FOUND'
                    group by day
                ) as totalErr
            where totalReq.day = totalErr.day
        ) as sub
        where error_percentage > 1
        """
    )
    results = cur.fetchall()
    for result in results:
        date = result[0]
        perc = result[1]
        print("%s - %s errors" % (formatDate(date), perc))


def formatDate(date):
    return date.strftime('%b %d, %Y')


if __name__ == "__main__":
    conn = psycopg2.connect('dbname=news')
    print('------------------- Top Three Articles -------------------')
    getTopThreeArticles(conn)
    print('------------------- Top Authors -------------------')
    getTopAuthors(conn)
    print('-------------- Days with more than 1 percent errors --------------')
    getDaysWithMostErrors(conn)
    conn.close()
