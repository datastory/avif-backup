# coding: utf-8
from credentials import login
import requests
from time import gmtime, strftime
import boto3

def lambda_handler(event, context):
    s = requests.Session()
    s.get('http://www.birds.cz/avif/index.php?login=1&login_return_back=0')
    r = s.get('http://www.birds.cz/avif/export.php?what=my_observations', auth=(login['user'], login['pwd']))

    s3 = boto3.resource('s3')
    bucket = s3.Object(login['bucket'], 'avif/bckp_' + strftime("%Y-%m-%d_%H-%M-%S", gmtime()) + '.csv')
    bucket.put(Body=r.content)