import os
from datetime import datetime, timezone, timedelta

import boto3

ec2 = boto3.client("ec2")

VOLUME_ID = os.environ["VOLUME_ID"]
RETENTION_DAYS = int(os.getenv("RETENTION_DAYS", "30"))
SNAPSHOT_TAG_KEY = os.getenv("SNAPSHOT_TAG_KEY", "CreatedBy")
SNAPSHOT_TAG_VALUE = os.getenv("SNAPSHOT_TAG_VALUE", "hv-assignment-04")


def lambda_handler(event, context):
    # 1) Create snapshot
    desc = f"Automated snapshot for {VOLUME_ID} ({SNAPSHOT_TAG_VALUE})"
    snap = ec2.create_snapshot(VolumeId=VOLUME_ID, Description=desc)
    snapshot_id = snap["SnapshotId"]

    ec2.create_tags(
        Resources=[snapshot_id],
        Tags=[
            {"Key": SNAPSHOT_TAG_KEY, "Value": SNAPSHOT_TAG_VALUE},
            {"Key": "VolumeId", "Value": VOLUME_ID},
        ],
    )

    print(f"Created snapshot: {snapshot_id} for volume {VOLUME_ID}")

    # 2) Cleanup old snapshots (only the ones created by this automation)
    cutoff = datetime.now(timezone.utc) - timedelta(days=RETENTION_DAYS)
    deleted = []

    paginator = ec2.get_paginator("describe_snapshots")
    for page in paginator.paginate(
        OwnerIds=["self"],
        Filters=[{"Name": f"tag:{SNAPSHOT_TAG_KEY}", "Values": [SNAPSHOT_TAG_VALUE]}],
    ):
        for s in page.get("Snapshots", []):
            sid = s["SnapshotId"]
            start_time = s["StartTime"]  # timezone-aware
            if start_time < cutoff:
                ec2.delete_snapshot(SnapshotId=sid)
                deleted.append({"snapshot_id": sid, "start_time": start_time.isoformat()})
                print(f"Deleted old snapshot: {sid} (StartTime={start_time})")

    return {
        "statusCode": 200,
        "body": {
            "volume_id": VOLUME_ID,
            "created_snapshot_id": snapshot_id,
            "retention_days": RETENTION_DAYS,
            "deleted": deleted,
        },
    }
