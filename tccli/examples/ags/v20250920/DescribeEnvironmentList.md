**Example 1: 查询 Environment 列表**



Input: 

```
tccli ags DescribeEnvironmentList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 20 \
    --Filters.0.Name environment-id \
    --Filters.0.Values env-example
```

Output: 
```
{
    "Response": {
        "EnvironmentSet": [
            {
                "EnvironmentId": "env-example",
                "EnvironmentTemplateId": "envt-example",
                "AgentId": "ag-example",
                "UserId": "user-example",
                "SessionId": "session-example",
                "Status": "ACTIVE",
                "CreatedTime": "2026-07-03T10:56:18Z",
                "UpdatedTime": "2026-07-03T10:56:18Z"
            }
        ],
        "TotalCount": 1,
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

