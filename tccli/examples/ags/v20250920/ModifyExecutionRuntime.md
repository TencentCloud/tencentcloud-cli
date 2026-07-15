**Example 1: 修改 ExecutionRuntime**



Input: 

```
tccli ags ModifyExecutionRuntime --cli-unfold-argument  \
    --ExecutionRuntimeId runtime-example \
    --Capacity 3 \
    --SchedulingStatus DISABLED
```

Output: 
```
{
    "Response": {
        "ExecutionRuntime": {
            "ExecutionRuntimeId": "runtime-example",
            "AgentId": "ag-example",
            "SchedulingStatus": "DISABLED",
            "ActiveLeaseCount": 2,
            "Capacity": 3,
            "Endpoint": {
                "Scheme": "HTTPS",
                "Host": "{{ .SourcePort }}-{{ .Metadata.RuntimeInstanceID }}.example.com",
                "Port": "443",
                "Metadata": [
                    {}
                ]
            },
            "CreatedTime": "2026-07-03T10:56:18Z",
            "UpdatedTime": "2026-07-03T10:56:18Z"
        },
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

