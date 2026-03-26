#!/Users/haydenrobinette/miniforge3/envs/ds2002/bin/python3
import boto3

# create client
s3 = boto3.client('s3', region_name="us-east-1")
bucket = 'ds2002-xyb9vz'


# make request
response = s3.list_buckets()
# now iterate through the response:
for r in response['Buckets']:
    print(r['Name'])


#private file upload
imageName = "wallePhoto.jpg"
image = open(imageName, 'rb')

response = s3.put_object(
    Body = image,
    Bucket = bucket,
    Key = imageName
)
print(response)

#public upload
imageName = "publicWallePhoto.jpg"
image = open(imageName, 'rb')

response = s3.put_object(
    Body = image,
    Bucket = bucket,
    Key = imageName,
    ACL='public-read',
)
print(response)