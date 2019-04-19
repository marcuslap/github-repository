import boto3
import sys

session = boto3.Session(profile_name='pythonAutomation')
s3 = session.resource('s3')

_name_ = "_main_"

if _name_ == '_main_':
    print(sys.argv)
    for bucket in s3.buckets.all():
        print(bucket)
