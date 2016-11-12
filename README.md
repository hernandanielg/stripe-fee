# stripe-fee

## How to run the project

### Requirements
- Docker
- docker-compose

1. Create a `.env` file based on .env.example and then modify MYSQL parameters
2. Run `docker-compose up`
3. That's it.

### Run tests

Use the following command to run tests  
`python manage.py test --keepdb`

When using Docker please do:  
`docker-compose exec web python manage.py test --keepdb`

And please be patient ;)
