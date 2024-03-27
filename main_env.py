import os

dp_url = os.getenv('DP_URL', default='url')
dp_user = os.getenv('DP_USER', default='user')
dp_password = os.getenv('DP_PASSWORD', default='password')

db_params_dp = {
    "user": os.getenv('POSTGRES_USER', default='user'),
    "password": os.getenv('POSTGRES_PASSWORD', default='password'),
    "host":  os.getenv('POSTGRES_HOST', default='host'),
    "port": os.getenv('POSTGRES_PORT', default=0000),
    "database": os.getenv('POSTGRES_DB', default='db'),

}
