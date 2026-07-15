**Example 1: 注册 ExecutionRuntime**



Input: 

```
tccli ags RegisterExecutionRuntime --cli-unfold-argument  \
    --AgentId ag-example \
    --Capacity 0 \
    --SchedulingStatus ENABLED \
    --Endpoint.Scheme HTTPS \
    --Endpoint.Host {{ .SourcePort }}-{{ .Metadata.RuntimeInstanceID }}.example.com \
    --Endpoint.Port 443
```

Output: 
```
{
    "Response": {
        "ExecutionRuntime": {
            "ExecutionRuntimeId": "runtime-example",
            "AgentId": "ag-example",
            "SchedulingStatus": "ENABLED",
            "ActiveLeaseCount": 2,
            "Capacity": 0,
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

