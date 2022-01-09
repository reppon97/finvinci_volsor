## Basic Web Service for currency conversion

Service saves conversion rates from [this API](https://github.com/fawazahmed0/currency-api) for USD, EUR, PLN, CZK once on start up and once a day at 16:00 (4 PM) UTC (Stock exchange market closing time).

### Stack: 

- API: 
    * Django (Django Rest Framework)
    * Celery (Celery beat for periodic tasks)
    * Redis (needed for Celery)
    * PostgreSQL
- UI: Bootstrap 5.x (Nothing special, just needed their forms)

API's powered by docker-compose to make it practical and easy-to-use. 

### Usage:

`docker-compose up --build`

or simply:

`make docker-up`

to shut it down:

`make docker-down`

### Tests:

`make test`
