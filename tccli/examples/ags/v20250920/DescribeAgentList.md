**Example 1: 查询 Agent 列表**



Input: 

```
tccli ags DescribeAgentList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 20 \
    --Filters.0.Name agent-name \
    --Filters.0.Values example-agent
```

Output: 
```
{
    "Response": {
        "AgentSet": [
            {
                "AgentId": "ag-example",
                "AgentName": "example-agent",
                "AgentType": "CLOUD",
                "DefaultVersion": "v1",
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

