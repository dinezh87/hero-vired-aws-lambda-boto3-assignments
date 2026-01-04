import os
import json
from datetime import datetime, timezone

import boto3

sns = boto3.client("sns")
ec2 = boto3.client("ec2")

SNS_TOPIC_ARN = os.environ["SNS_TOPIC_ARN"]


def lambda_handler(event, context):
    # Expected EventBridge event for EC2 state changes
    detail = event.get("detail", {})
    instance_id = detail.get("instance-id")
    state = detail.get("state")

    time_str = event.get("time") or datetime.now(timezone.utc).isoformat()

    # Optional enrichment: get instance Name tag
    instance_name = None
    if instance_id:
        resp = ec2.describe_instances(InstanceIds=[instance_id])
        tags = resp["Reservations"][0]["Instances"][0].get("Tags", [])
        for t in tags:
            if t.get("Key") == "Name":
                instance_name = t.get("Value")

    subject = f"EC2 State Change: {instance_id} -> {state}"
    message = {
        "time": time_str,
        "instance_id": instance_id,
        "instance_name": instance_name,
        "new_state": state,
        "raw_event": event
    }

    sns.publish(
        TopicArn=SNS_TOPIC_ARN,
        Subject=subject[:100],  # SNS subject limit safety
        Message=json.dumps(message, indent=2, default=str),
    )

    print(f"Notification sent for {instance_id} state={state}")
    return {"statusCode": 200, "body": {"notified": True, "instance_id": instance_id, "state": state}}
