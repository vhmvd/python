import boto3


# For connection with the client using keys

s3client = boto3.client(
's3',
aws_access_key_id="AKIAI6275XY4QXOTQPFA",
aws_secret_access_key="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",
)



def upload(filePathLocal, bucketName, fileNameS3):
  try:
    s3client.upload_file(filePathLocal, bucketName, fileNameS3)
    print("Upload Successful")
  except FileNotFoundError:
    print("The file was not found")

upload("hello.txt", "kens-temp-bucket", "hello.txt")