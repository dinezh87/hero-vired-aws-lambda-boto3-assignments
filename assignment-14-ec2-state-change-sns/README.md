# Assignment 14 – Monitor EC2 Instance State Changes Using Lambda + EventBridge + SNS

## Objective
Send an SNS notification whenever an EC2 instance changes state (started/stopped).

## What I Learned
- Event-driven automation using EventBridge
- Using EC2 state change events as triggers
- Sending email alerts using SNS
- Parsing event payload in Lambda

---

## AWS Services Used
- AWS Lambda
- Amazon EC2
- Amazon SNS
- Amazon EventBridge
- IAM
- CloudWatch Logs

---

## Implementation Steps

### Step 1: Create SNS Topic & Email Subscription
- Created SNS topic (example: `hv-ec2-state-alerts`)
- Added email subscription and confirmed it via inbox

📸 **Screenshot Placeholder:**  
- SNS topic + subscription confirmed  
  - `screenshots/assignment-14/01-sns-topic-subscription.png`

---

### Step 2: Create IAM Role for Lambda
IAM → Roles → Create role → Trusted entity: **Lambda**

Permissions required:
- `sns:Publish`
- (Optional) `ec2:DescribeInstances` (to fetch instance name)

📸 **Screenshot Placeholder:**  
- IAM role page showing permissions  
  - `screenshots/assignment-14/02-iam-role-policy.png`

---

### Step 3: Create Lambda Function
Lambda → Create function:
- Runtime: Python 3.x
- Environment variable:
  - `SNS_TOPIC_ARN` = `<your-sns-topic-arn>`

📸 **Screenshot Placeholder:**  
- Lambda configuration showing env var + role  
  - `screenshots/assignment-14/03-lambda-env-vars.png`

📸 **Screenshot Placeholder:**  
- Lambda code screenshot  
  - `screenshots/assignment-14/04-lambda-code.png`

---

### Step 4: Create EventBridge Rule (EC2 State Change)
EventBridge → Create rule:
- Event pattern:
  - Source: `aws.ec2`
  - Detail-type: `EC2 Instance State-change Notification`
- Target: Lambda function

📸 **Screenshot Placeholder:**  
- EventBridge rule showing pattern + target  
  - `screenshots/assignment-14/05-eventbridge-rule.png`

---

### Step 5: Testing
- Started / Stopped an EC2 instance
- Verified:
  - Lambda triggered (CloudWatch logs)
  - SNS email received

📸 **Screenshot Placeholder:**  
- CloudWatch logs showing event received and SNS published  
  - `screenshots/assignment-14/06-cloudwatch-logs.png`

📸 **Screenshot Placeholder:**  
- Email alert received (SNS notification)  
  - `screenshots/assignment-14/07-email-alert.png`

---

## Code
See: `lambda_function.py`

---

## Result / Output
✅ SNS email received for EC2 start/stop events.  
✅ EventBridge successfully triggered Lambda on state changes.  
✅ Logs and screenshots captured.
