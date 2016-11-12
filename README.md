# Stripe Plan Subscription using Django

## How to run the project

### Requirements
- Docker
- docker-compose

### Instructions
1. Create a `.env` file based on .env.example and then modify MYSQL parameters
2. Run `docker-compose up`
3. That's it.

### Run tests

First let's install selenium:  
`pip install --upgrade selenium`

Use the following command to run tests  
`python manage.py test --keepdb `

And please be patient ;)
