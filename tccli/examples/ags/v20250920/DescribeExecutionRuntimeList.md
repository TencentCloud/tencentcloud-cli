**Example 1: 查询 ExecutionRuntime 列表**



Input: 

```
tccli ags DescribeExecutionRuntimeList --cli-unfold-argument  \
    --Offset 0 \
    --Limit 20 \
    --Filters.0.Name agent-id \
    --Filters.0.Values ag-example \
    --Filters.1.Name scheduling-status \
    --Filters.1.Values ENABLED
```

Output: 
```
{
    "Response": {
        "ExecutionRuntimeSet": [
            {
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
            }
        ],
        "TotalCount": 1,
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

