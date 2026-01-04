# Assignment 2 – Automated S3 Bucket Cleanup (Delete Objects Older than 30 Days)

## Objective
Automatically delete objects older than **30 days** from a specific S3 bucket using **AWS Lambda** and **Boto3**.

## What I Learned
- How to list S3 objects using pagination
- How to compare `LastModified` timestamps
- How to delete S3 objects programmatically
- IAM permissions needed for S3 cleanup automation

---

## AWS Services Used
- AWS Lambda
- Amazon S3
- IAM
- CloudWatch Logs

---

## Implementation Steps

### Step 1: Create S3 Bucket and Upload Objects
- Created a dedicated S3 bucket for cleanup testing
- Uploaded multiple objects for testing

📸 **Screenshot Placeholder:**  
- S3 bucket showing uploaded objects  
  - `screenshots/assignment-02/01-s3-objects-before.png`

---

### Step 2: Create IAM Role for Lambda
IAM → Roles → Create role → Trusted entity: **Lambda**

Permissions added (as per assignment instruction):
- `AmazonS3FullAccess`

📸 **Screenshot Placeholder:**  
- IAM role page showing attached policy  
  - `screenshots/assignment-02/02-iam-role-policy.png`

---

### Step 3: Create Lambda Function
Lambda → Create function:
- Runtime: Python 3.x
- Set environment variables:
  - `BUCKET_NAME` = `<your-bucket-name>`
  - `RETENTION_DAYS` = `30`

📸 **Screenshot Placeholder:**  
- Lambda configuration page showing env vars  
  - `screenshots/assignment-02/03-lambda-env-vars.png`

📸 **Screenshot Placeholder:**  
- Lambda code screenshot  
  - `screenshots/assignment-02/04-lambda-code.png`

---

### Step 4: Manual Invocation (Testing)
- Ran Lambda manually
- Verified that objects older than retention period were deleted
- Checked CloudWatch logs for deleted object keys

📸 **Screenshot Placeholder:**  
- Lambda test execution result  
  - `screenshots/assignment-02/05-lambda-test-result.png`

📸 **Screenshot Placeholder:**  
- CloudWatch logs showing deleted object names  
  - `screenshots/assignment-02/06-cloudwatch-logs.png`

📸 **Screenshot Placeholder:**  
- S3 bucket after cleanup  
  - `screenshots/assignment-02/07-s3-objects-after.png`

---

## Code
See: `lambda_function.py`

---

## Result / Output
✅ Lambda successfully deleted objects older than the configured retention period.  
✅ Logs and S3 screenshots captured.
