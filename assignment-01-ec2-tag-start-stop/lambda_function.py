import os
import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client("ec2")

TAG_KEY = os.getenv("TAG_KEY", "Action")
STOP_VALUE = os.getenv("STOP_VALUE", "Auto-Stop")
START_VALUE = os.getenv("START_VALUE", "Auto-Start")


def _get_instances_by_tag(tag_key: str, tag_value: str):
    paginator = ec2.get_paginator("describe_instances")
    filters = [{"Name": f"tag:{tag_key}", "Values": [tag_value]}]

    instance_ids = []
    for page in paginator.paginate(Filters=filters):
        for reservation in page.get("Reservations", []):
            for inst in reservation.get("Instances", []):
                instance_ids.append(inst["InstanceId"])
    return instance_ids


def lambda_handler(event, context):
    stopped = []
    started = []
    errors = []

    stop_ids = _get_instances_by_tag(TAG_KEY, STOP_VALUE)
    start_ids = _get_instances_by_tag(TAG_KEY, START_VALUE)

    print(f"Found Auto-Stop instances: {stop_ids}")
    print(f"Found Auto-Start instances: {start_ids}")

    if stop_ids:
        try:
            ec2.stop_instances(InstanceIds=stop_ids)
            stopped = stop_ids
            print(f"Stop requested for: {stopped}")
        except ClientError as e:
            errors.append({"action": "stop", "error": str(e)})
            print(f"ERROR stopping instances: {e}")

    if start_ids:
        try:
            ec2.start_instances(InstanceIds=start_ids)
            started = start_ids
            print(f"Start requested for: {started}")
        except ClientError as e:
            errors.append({"action": "start", "error": str(e)})
            print(f"ERROR starting instances: {e}")

    return {
        "statusCode": 200 if not errors else 207,
        "body": {
            "stopped": stopped,
            "started": started,
            "errors": errors
        }
    }
