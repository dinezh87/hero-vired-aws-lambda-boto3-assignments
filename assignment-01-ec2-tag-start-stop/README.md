# Assignment 1 – Automated EC2 Instance Management (Start/Stop by Tags)

## Objective
Automatically **stop** EC2 instances tagged with `Action=Auto-Stop` and **start** EC2 instances tagged with `Action=Auto-Start` using **AWS Lambda** and **Boto3**.

## What I Learned
- How Lambda runs Python code without servers
- How to use Boto3 to `describe_instances`, `stop_instances`, and `start_instances`
- Using EC2 tags as automation controls
- IAM permissions required for EC2 operations

---

## AWS Services Used
- AWS Lambda
- Amazon EC2
- IAM
- CloudWatch Logs

---

## Implementation Steps

### Step 1: Create 2 EC2 Instances
- Created two EC2 instances (t2.micro or free-tier eligible)
- Instance A tagged `Action=Auto-Stop`
- Instance B tagged `Action=Auto-Start`

📸 **Screenshot Placeholder:**  
- EC2 Instances list showing both instances and tags  
  - `screenshots/assignment-01/01-ec2-instances-tags.png`

---

### Step 2: Create IAM Role for Lambda
IAM → Roles → Create role → Trusted entity: **Lambda**

Permissions added (as per assignment instruction):
- `AmazonEC2FullAccess` *(for simplicity in this project)*

📸 **Screenshot Placeholder:**  
- IAM role page showing attached policy  
  - `screenshots/assignment-01/02-iam-role-policy.png`

---

### Step 3: Create Lambda Function
Lambda → Create function:
- Runtime: Python 3.x
- Execution role: IAM role from Step 2
- Added code in `lambda_function.py`

📸 **Screenshot Placeholder:**  
- Lambda function configuration page (name + runtime + role)  
  - `screenshots/assignment-01/03-lambda-config.png`

📸 **Screenshot Placeholder:**  
- Lambda code screenshot  
  - `screenshots/assignment-01/04-lambda-code.png`

---

### Step 4: Manual Invocation (Testing)
- Created a test event `{}` and ran the function
- Verified:
  - Auto-Stop instance moved to **stopped**
  - Auto-Start instance moved to **running**

📸 **Screenshot Placeholder:**  
- Lambda test execution result  
  - `screenshots/assignment-01/05-lambda-test-result.png`

📸 **Screenshot Placeholder:**  
- CloudWatch logs showing instance IDs started/stopped  
  - `screenshots/assignment-01/06-cloudwatch-logs.png`

📸 **Screenshot Placeholder:**  
- EC2 instance states after invocation  
  - `screenshots/assignment-01/07-ec2-state-changed.png`

---

## Code
See: `lambda_function.py`

---

## Result / Output
✅ Instances were started/stopped based on the tag values successfully.  
✅ Logs captured in CloudWatch and screenshots attached.
