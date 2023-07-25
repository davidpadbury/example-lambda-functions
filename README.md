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

[Install](https://us-east-1.console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?templateURL=https://lambda-function-examples.s3.amazonaws.com/testing/sleepy-lambda.yml&stackName=SleepyLambda)

*Example Payloads*:

```json
{
    "sleepSeconds": "30"
}
```

### Faily Lambda

A lambda functions that does nothing but blow up when called. Useful for testing error handling.

[Install](https://us-east-1.console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?templateURL=https://lambda-function-examples.s3.amazonaws.com/testing/faily-lambda.yml&stackName=FailyLambda)

### Echo Message Lambda

A lambda function that just echos back the message you send it. Useful for checking your requests.

[Install](https://us-east-1.console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?templateURL=https://lambda-function-examples.s3.amazonaws.com/testing/echo-message-lambda.yml&stackName=EchoMessageLambda)

*Example Payloads*:

```json
{
    "message": "Knock Knock"
}
```

### Response Generator Lambda

Generates a bunch of text or a bunch of binary rubbish. Useful for verifying response handling with extreme responses.

[Install](https://us-east-1.console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?templateURL=https://lambda-function-examples.s3.amazonaws.com/testing/response-generator-lambda.yml&stackName=ResponseGeneratorLambda)

*Example Payloads*:

Generate response of random bytes:
```json
{
    "type": "binary",
    "size": "1024"
}
```

Generate response of random printable characters:
```json
{
    "type": "text",
    "size": "1024"
}
```

By default the response will be embedded in a response object in the structure `{ statusCode, message }`.
To just return the generated response without the response object do:
```json
{
    "type": "text",
    "size": "1024",
    "embedResponse": false
}
```