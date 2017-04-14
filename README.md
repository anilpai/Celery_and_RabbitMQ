# Celery <3 RabbitMQ

Simple working demo of Celery working with RabbitMQ.

# Installing RabbitMQ.

`$ brew install rabbitmq`

`$ PATH=$PATH:/usr/local/sbin`

`$ rabbitmq-server`

# Create new user and setup host & tag.

### add user 'jon' with password 'snow'
`$ rabbitmqctl add_user jon snow`
### add virtual host 'jon_vhost'
`$ rabbitmqctl add_vhost jon_vhost`
### add user tag 'jon_tag' for user 'jon'
`$ rabbitmqctl set_user_tags jon jon_tag`
### set permission for user 'jon' on virtual host 'jon_vhost'
`$ rabbitmqctl set_permissions -p jon_vhost jon ".*" ".*" ".*"`

# Running the project.

## Open 3 terminals to run these 3 commands.

#1 Starting Celery Worker.
`$ celery -A test_celery worker --loglevel=info`

#2 Running Tasks.
`$ python -m test_celery.run_tasks`

#3 Monitoring Celery in Real Time using Flower.
`$ celery -A test_celery flower`

Flower : Open the browser & visit `http://localhost:5555`
