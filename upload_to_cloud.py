import boto3

def upload_to_s3(file_path, bucket_name, s3_key, aws_access_key, aws_secret_key):
    s3 = boto3.client(
        "s3",
        aws_access_key_id=aws_access_key,
        aws_secret_access_key=aws_secret_key
    )
    s3.upload_file(file_path, bucket_name, s3_key)
    print("File uploaded to S3 successfully!")
