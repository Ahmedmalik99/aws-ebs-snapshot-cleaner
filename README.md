# AWS EBS Snapshot Cleaner (Lambda)

This project is an AWS Lambda function designed to automatically delete unused Amazon EBS snapshots. It is triggered using Amazon EventBridge on a schedule (e.g., daily).

## 🛠️ Features

- Lists all available EBS snapshots
- Deletes snapshots that are no longer in use
- Logs operations to CloudWatch Logs
- Triggered automatically using EventBridge

## 📂 Files

- `lambda_function.py`: Main Lambda function code.
- `policy.json`: IAM policy needed to allow EC2 and CloudWatch access.
- `eventbridge-rule.json` *(optional)*: Sample EventBridge rule for scheduling.

## 🚀 How to Deploy

1. **Create Lambda Function**
   - Runtime: Python 3.12+
   - Upload `lambda_function.py`
   - Set handler to: `lambda_function.lambda_handler`

2. **Attach IAM Role**
   - Create and attach a role with `policy.json` permissions

3. **Create EventBridge Rule**
   - Use `eventbridge-rule.json` or do it via AWS Console
   - Target: Your Lambda function

4. **Check Logs**
   - Go to CloudWatch Logs: `/aws/lambda/your-lambda-function-name`

## ✅ IAM Permissions

The Lambda execution role must have:

- `ec2:DescribeSnapshots`
- `ec2:DeleteSnapshot`
- `logs:*` (for logging)

## 🧪 Testing

You can manually test the Lambda with a dummy event like:

```json
{
  "source": "manual-test"
}
