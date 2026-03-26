#!/Users/haydenrobinette/miniforge3/envs/ds2002/bin/python3

import boto3
import logging
import sys
import os

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logging.basicConfig(level=logging.INFO, handlers=[console_handler])



def parse_args():
    """Look through arguments for provided inputFolder and the bucket prefix, log an error otherwise."""
    try:
        inputFolder = sys.argv[1]
        bucketPrefix = sys.argv[2]
    except IndexError:
        logging.error(f"Usage: python {sys.argv[0]} <input_folder> <bucketPrefix>")
        sys.exit(1)

    return inputFolder, bucketPrefix




def upload(input_folder, destination):
    """Upload all files from input_folder to the specified S3 bucket destination."""
    parts = destination.split('/', 1)
    bucket = parts[0]
    prefix = parts[1] if len(parts) > 1 else ''

    try:
        s3 = boto3.client('s3', region_name="us-east-1")

        for file in os.scandir(input_folder):
            if file.is_file():
                s3Key = prefix + file.name
                logging.info(f"Uploading {file.name} -> s3://{bucket}/{s3Key}")

                with open(file.path, 'rb') as f:   # ✅ fixed — reads actual file contents
                    s3.put_object(
                        Body=f,
                        Bucket=bucket,
                        Key=s3Key
                    )
                logging.info(f"Successfully uploaded {file.name}")

        return True

    except Exception as e:
        logging.error(f"Upload failed: {e}")
        return False
    

def main():
    """Main entry point. Parses arguments, runs upload, and logs outcome."""
    input_folder, destination = parse_args()

    logging.info(f"Starting the uploading of file {input_folder} to s3://{destination}")

    success = upload(input_folder, destination)

    if success:
        logging.info("All files uploaded successfully.")
    else:
        logging.error("Upload completed with errors. Check logs above.")
        sys.exit(1)


if __name__ == "__main__":
    main()

