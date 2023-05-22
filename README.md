# Example Lambda Functions

## Ops

### Recent CloudWatch Logs Errors

Returns a list of the most common errors that were recently seen in a CloudWatch Logs Group.

[Install](https://us-east-1.console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?templateURL=https://raw.githubusercontent.com/davidpadbury/example-lambda-functions/main/templates/ops/cloudwatch-recent-errors.yml&stackName=CloudWatchRecentErrors)

*Example Payload*:

```json
{
    "logGroup": "$LogGroup"
}
```

### Recent CloudFormation Stack Changes

Recents a list of recent changes to CloudFormation stacks.

[Install](https://us-east-1.console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?templateURL=https://raw.githubusercontent.com/davidpadbury/example-lambda-functions/main/templates/ops/cloudformation-recent-changes.yml&stackName=CloudFormationRecentChanges)

## Integrations

### Jira Create Issue

Create a JIRA issue with a provided summary and description.

[Install](https://us-east-1.console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?templateURL=https://raw.githubusercontent.com/davidpadbury/example-lambda-functions/main/templates/integrations/jira-create-issue.yml&stackName=JiraCreateIssue)

*Example Payload*:

```json
{
    "summary": "$Summary",
    "description": "$Description"
}
```