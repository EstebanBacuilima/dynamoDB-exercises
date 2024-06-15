from boto3 import resource
from os import getenv

dynamodb = resource("dynamodb",
                    aws_access_key_id=getenv("AWS_ACCESS_KEY_ID"),
                    aws_secret_access_key=getenv("AWS_SECRET_ACCESS_KEY"),
                    region_name=getenv("REGION_NAME"))

# Add Tables
tables = [
    {
        "TableName": "users",
        "KeySchema": [
            {
                'AttributeName': 'id',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'created_at', # CLASSIFICATION KEY by DATE
                'KeyType': 'RANGE'
            },

        ],
        "AttributeDefinitions": [
            {
                'AttributeName': 'id',
                'AttributeType': 'S' # S:STRING | N:NUMBER | B:BINARY
            },
            {
                'AttributeName': 'created_at',
                'AttributeType': 'S'
            }
        ],
    },
]

# Create tables in dynamodb
def create_tables():
    print("INIT")
    try:
        for table in tables:
            dynamodb.create_table(
                TableName=table["TableName"],
                KeySchema=table["KeySchema"],
                AttributeDefinitions=table["AttributeDefinitions"],
                BillingMode="PAY_PER_REQUEST"
            )
    except Exception as e:
        print(e)