
from boto3 import session

# load env vars from .env
from dotenv import load_dotenv
load_dotenv()

# Initiate session
session = session.Session()
client = session.client('s3',
                        region_name='eu-central-1')

# List all objects in a bucket
response = client.list_objects(Bucket='studierendenprojekt-tha-waldinventur')
for content in response['Contents']:
    print(content['Key'])

# Upload a file to your Space
client.download_file('studierendenprojekt-tha-waldinventur','small_image.jpg', 'small_image.jpg')