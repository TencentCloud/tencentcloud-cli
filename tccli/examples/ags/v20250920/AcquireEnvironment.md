**Example 1: 获取 Environment**



Input: 

```
tccli ags AcquireEnvironment --cli-unfold-argument  \
    --EnvironmentTemplateId envt-example \
    --AgentId ag-example \
    --UserId user-example \
    --SessionId session-example
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
            "UpdatedTime": "2026-07-03T10:56:18Z",
            "ProviderConfig": {
                "ProviderKind": "TENCENT_AGS",
                "TencentAGS": {
                    "InstanceId": "ins-example",
                    "AccessToken": "example-access-token"
                }
            }
        },
        "EnvironmentLease": {
            "EnvironmentLeaseId": "envl-example",
            "EnvironmentId": "env-example",
            "ExpiresTime": "2026-07-03T11:01:18Z"
        },
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

