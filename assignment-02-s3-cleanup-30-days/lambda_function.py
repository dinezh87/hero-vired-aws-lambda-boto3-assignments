import os
from datetime import datetime, timezone, timedelta

import boto3

s3 = boto3.client("s3")

BUCKET_NAME = os.environ["BUCKET_NAME"]
RETENTION_DAYS = int(os.getenv("RETENTION_DAYS", "30"))


def lambda_handler(event, context):
    cutoff = datetime.now(timezone.utc) - timedelta(days=RETENTION_DAYS)
    deleted = []
    scanned = 0

    paginator = s3.get_paginator("list_objects_v2")

    for page in paginator.paginate(Bucket=BUCKET_NAME):
        for obj in page.get("Contents", []):
            scanned += 1
            key = obj["Key"]
            last_modified = obj["LastModified"]

            if last_modified < cutoff:
                s3.delete_object(Bucket=BUCKET_NAME, Key=key)
                deleted.append({"key": key, "last_modified": last_modified.isoformat()})
                print(f"Deleted: {key} (LastModified={last_modified})")

    print(f"Scanned objects: {scanned}")
    print(f"Deleted objects: {len(deleted)}")

    return {
        "statusCode": 200,
        "body": {
            "bucket": BUCKET_NAME,
            "retention_days": RETENTION_DAYS,
            "scanned": scanned,
            "deleted": deleted
        }
    }
