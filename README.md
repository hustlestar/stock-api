***STOCK API***

This project uses vantage api to get and parse data about different stocks.

This data is gathered at mysql database to perform future analytics.

As the next step rest api would be created with plotting and analytics.

Create ./back/secrets/credentials.properties
```
api.key=
etl.load.skip=false
db.user=
db.password=
db.host=database
db.port=3306
db.database=
plotly.user=
plotly.key=
```

Create ./database/secrets/ with following files
```
mysql-database
mysql-password
mysql-root-password
mysql-user
```

*To run application do following*     
```
docker-compose build
docker-compose up
```