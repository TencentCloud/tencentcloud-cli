**Example 1: 查询事件**



Input: 

```
tccli ags DescribeEventCenterEvents --cli-unfold-argument  \
    --Filters.0.Name ToolId \
    --Filters.0.Values sdt-7dl0dcpn \
    --StartTime 2026-10-23T13:28:00Z \
    --Offset 0 \
    --Limit 100 \
    --Order Asc \
    --Mode Raw
```

Output: 
```
{
    "Response": {
        "EndTime": "2026-10-23T13:32:39.90197686Z",
        "Events": [
            {
                "EventId": "17083c5e-4af9-4a63-b012-6ac843847bd2",
                "EventLevel": "Normal",
                "EventType": "SandboxStarting",
                "Extensions": "{\"ToolId\":\"sdt-7dl0dcpn\",\"ToolType\":\"code-interpreter\",\"ToolName\":\"event-center-test-1023\"}",
                "Message": "SandboxStarting",
                "ObjectId": "sdt-7dl0dcpn",
                "ObjectType": "SandboxTool",
                "OccurredAt": "2026-10-23T13:29:02.427Z",
                "Source": "Sandbox"
            }
        ],
        "Mode": "Raw",
        "StartTime": "2026-10-23T13:28:00Z",
        "TotalCount": 4,
        "RequestId": "d1fac4dc-5a56-47db-84e2-68ea97f6b4aa"
    }
}
```

