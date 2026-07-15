**Example 1: 查询 Environment**



Input: 

```
tccli ags DescribeEnvironment --cli-unfold-argument  \
    --EnvironmentId env-example
```

Output: 
```
{
    "Response": {
        "Environment": {
            "EnvironmentId": "env-example",
            "EnvironmentTemplateId": "envt-example",
            "AgentId": "ag-example",
            "UserId": "user-example",
            "SessionId": "session-example",
            "Status": "ACTIVE",
            "CreatedTime": "2026-07-03T10:56:18Z",
            "UpdatedTime": "2026-07-03T10:56:18Z"
        },
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

