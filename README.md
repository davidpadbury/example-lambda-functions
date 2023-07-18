# Example Lambda Functions

## Ops

### Recent CloudWatch Logs Errors

Returns a list of the most common errors that were recently seen in a CloudWatch Logs Group.

[Install](https://us-east-1.console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?templateURL=https://lambda-function-examples.s3.amazonaws.com/ops/cloudwatch-recent-errors.yml&stackName=CloudWatchRecentErrors)

*Example Payload*:

```json
{
    "logGroup": "$LogGroup"
}
```

### Recent CloudFormation Stack Changes

Recents a list of recent changes to CloudFormation stacks.

[Install](https://us-east-1.console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?templateURL=https://lambda-function-examples.s3.amazonaws.com/ops/cloudformation-recent-changes.yml&stackName=CloudFormationRecentChanges)

## Integrations

### Jira Create Issue

Create a JIRA issue with a provided summary and description.

[Install](https://us-east-1.console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?templateURL=https://lambda-function-examples.s3.amazonaws.com/integrations/jira-create-issue.yml&stackName=JiraCreateIssue)

*Example Payload*:

```json
{
    "summary": "$Summary",
    "description": "$Description"
}
```

## Testing

Useful for verifying things that invoke lambda functions and do things with their output.

### Sleepy Lambda

Creates a lambda that takes a number of seconds and sleeps for that long. Useful for verifying timeout behavior in callers.

[Install](https://us-east-1.console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?templateURL=https://lambda-function-examples.s3.amazonaws.com/integrations/sleepy-lambda.yml&stackName=SleepyLambda)

*Example Payloads*:

```json
{
    "sleepSeconds": "30"
}
```