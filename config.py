# edit the URI below to add your RDS password and your AWS URL
# The other elements are the same as used in the tutorial
# format: (user):(password)@(db_identifier).amazonaws.com:3306/(db_name)

# Uncomment the line below if you wnat to work with a remote DB
#SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://<db_username>:<db_password>@<db_endpoint>:3306/<db_name>'

# Uncomment the line below if you want to work with a local DB
#SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'

SQLALCHEMY_POOL_RECYCLE = 3600

WTF_CSRF_ENABLED = True
SECRET_KEY = 'dev_secret_key' #NOT secret, as it's published to version control 
