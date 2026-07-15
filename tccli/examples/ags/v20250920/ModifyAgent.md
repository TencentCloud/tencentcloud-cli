**Example 1: 修改 Agent**



Input: 

```
tccli ags ModifyAgent --cli-unfold-argument  \
    --AgentId ag-example \
    --AgentName example-agent-updated \
    --DefaultVersion v2
```

Output: 
```
{
    "Response": {
        "Agent": {
            "AgentId": "ag-example",
            "AgentName": "example-agent-updated",
            "AgentType": "CLOUD",
            "DefaultVersion": "v2",
            "Status": "ACTIVE",
            "CreatedTime": "2026-07-03T10:56:18Z",
            "UpdatedTime": "2026-07-03T10:56:18Z"
        },
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

