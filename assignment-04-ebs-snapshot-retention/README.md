# Assignment 4 – Automatic EBS Snapshot Creation and Cleanup (30-Day Retention)

## Objective
Automatically:
1) Create a snapshot for a specified EBS volume  
2) Delete snapshots older than **30 days** (retention cleanup)

## What I Learned
- Why EBS snapshots are used (backup, DR, cloning)
- How to create snapshots with Boto3
- How to filter snapshots and apply retention cleanup
- IAM permissions required for snapshot create/delete

---

## AWS Services Used
- AWS Lambda
- Amazon EC2 / EBS
- IAM
- CloudWatch Logs
- (Optional) EventBridge scheduling

---

## EBS Snapshot Concept (Simple Explanation)
- **EBS volume** is like a hard disk attached to your EC2.
- **Snapshot** is a backup of that disk.
- Used for:
  - restoring data after failure
  - cloning volumes/environments
  - compliance backups
- Retention cleanup avoids too many snapshots and reduces cost.

---

## Implementation Steps

### Step 1: Identify EBS Volume
- Selected an EBS volume to back up
- Noted the `VolumeId`

📸 **Screenshot Placeholder:**  
- EBS Volume details showing VolumeId  
  - `screenshots/assignment-04/01-ebs-volume-id.png`

---

### Step 2: Create IAM Role for Lambda
IAM → Roles → Create role → Trusted entity: **Lambda**

Permissions added (as per assignment instruction):
- `AmazonEC2FullAccess` *(simplified permission for project)*

📸 **Screenshot Placeholder:**  
- IAM role page showing attached policy  
  - `screenshots/assignment-04/02-iam-role-policy.png`

---

### Step 3: Create Lambda Function
Lambda → Create function:
- Runtime: Python 3.x
- Environment variables set:
  - `VOLUME_ID` = `<your-volume-id>`
  - `RETENTION_DAYS` = `30`

📸 **Screenshot Placeholder:**  
- Lambda configuration showing env vars  
  - `screenshots/assignment-04/03-lambda-env-vars.png`

📸 **Screenshot Placeholder:**  
- Lambda code screenshot  
  - `screenshots/assignment-04/04-lambda-code.png`

---

### Step 4: Manual Invocation (Testing)
- Ran the Lambda function manually
- Verified:
  - New snapshot created
  - Old snapshots (if any) older than retention period deleted
- Checked CloudWatch logs for snapshot IDs

📸 **Screenshot Placeholder:**  
- Lambda test execution result  
  - `screenshots/assignment-04/05-lambda-test-result.png`

📸 **Screenshot Placeholder:**  
- CloudWatch logs showing created/deleted snapshot IDs  
  - `screenshots/assignment-04/06-cloudwatch-logs.png`

📸 **Screenshot Placeholder:**  
- EC2 Snapshots page showing newly created snapshot  
  - `screenshots/assignment-04/07-snapshots-list.png`

---

### Step 5 (Bonus): EventBridge Schedule (If Implemented)
- Created an EventBridge schedule (weekly/daily) to run Lambda automatically

📸 **Screenshot Placeholder (optional):**  
- EventBridge rule showing schedule and target Lambda  
  - `screenshots/assignment-04/08-eventbridge-rule.png`

---

## Code
See: `lambda_function.py`

---

## Result / Output
✅ Snapshot automation successfully created backups and enforced retention cleanup.  
✅ Logs and screenshots captured.
