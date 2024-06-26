#source from https://www.youtube.com/watch?v=Y18HF5ALXew&t=1037s
import boto3
import json
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
s3 = boto3.resource('s3')
s3_client = boto3.client('s3')

def lambda_handler(event, context):
   
   bucket = event['Records'][0]['s3']['bucket']['name']
   json_file_name = event['Records'][0]['s3']['object']['key']
   print(str(event))
   json_object = s3_client.get_object(Bucket=bucket,Key=json_file_name)
   jsonFileReader = json_object['Body'].read()
   jsonDict = json.loads(jsonFileReader)
   print(str(jsonDict))
   table = dynamodb.Table('restable')
   for item in jsonDict:
      table.put_item(
         Item = {
            'res_id' : str(item['res_id']),
            'res_name' : item['res_name'],
            'lat' : Decimal(str(item['lat'])),
            'lng' : Decimal(str(item['lng'])),
            'address1' : item['address1'],
            'rprsntv_me' : item['rprsntv_me']
         }
      )
   return {
      'statusCode': 200,
      'body': 'wow'
      # result_list = []
   # bucket_list = []
   # for bucket in s3.buckets.all():
   #    bucket_list.append(bucket)
   #    result_list.append(bucket.name)
   }