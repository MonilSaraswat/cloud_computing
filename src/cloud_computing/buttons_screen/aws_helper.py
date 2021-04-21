import boto
from boto.file import Key
from django.conf import settings


def upload_file_to_s3(file_data, file_name, directory):
    """
    This method uploads files to S3
    :param file_data:
    :param file_name:
    :param directory:
    :return:
    """
    s3_upload_path = directory + str(file_name)
    conn = boto.connect_s3(settings.AWS_ACCESS_KEY_ID, settings.AWS_SECRET_ACCESS_KEY)
    b = conn.get_bucket(settings.AWS_STORAGE_BUCKET_NAME)
    k = b.new_key(s3_upload_path)
    k.set_contents_from_file(file_data)
    k.close()
    conn.close()
    return s3_upload_path


def get_file_from_aws(file_data):
    """
    This method is used to fetch files from S3
    """
    file_path = file_data.get('file_path')
    conn = boto.connect_s3(settings.AWS_ACCESS_KEY_ID, settings.AWS_SECRET_ACCESS_KEY)
    bucket = conn.get_bucket(settings.AWS_STORAGE_BUCKET_NAME)
    k = Key(bucket)
    k.key = file_path
    k.open()
    data = k.read()
    k.close()
    return data
