from gcloud import storage
storage_client=storage.Client()
bucket=storage_client.get_bucket("learning-bucket-23")
blob=bucket.blob("tffolder/newtxt.txt")
blob.upload_from_filename("./test.txt")