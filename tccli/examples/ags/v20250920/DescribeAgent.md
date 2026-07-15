**Example 1: 查询 Agent 信息**



Input: 

```
tccli ags DescribeAgent --cli-unfold-argument  \
    --AgentId ag-example
```

Output: 
```
{
    "Response": {
        "Agent": {
            "AgentId": "ag-example",
            "AgentName": "example-agent",
            "AgentType": "CLOUD",
            "DefaultVersion": "v1",
            "Status": "ACTIVE",
            "CreatedTime": "2026-07-03T10:56:18Z",
            "UpdatedTime": "2026-07-03T10:56:18Z"
        },
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

