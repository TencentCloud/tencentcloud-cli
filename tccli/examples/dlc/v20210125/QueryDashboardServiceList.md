**Example 1: 引擎为 xgboost，按 P95LatencyMs 指标倒序排序的示例**



Input: 

```
tccli dlc QueryDashboardServiceList --cli-unfold-argument  \
    --Page 1 \
    --PageSize 20 \
    --Filters.0.Name Engine \
    --Filters.0.Operator EQ \
    --Filters.0.Values xgboost \
    --SortFields.0.Field P95LatencyMs \
    --SortFields.0.Order DESC
```

Output: 
```
{
    "Response": {
        "Items": [
            {
                "Engine": "xgboost",
                "Metrics": {
                    "CpuUtilization": 0,
                    "ErrorRate": 0,
                    "GpuMemoryTotalMB": 0,
                    "GpuMemoryUsedMB": 0,
                    "GpuUtilization": 0,
                    "MemoryTotalBytes": 0,
                    "MemoryUsedBytes": 0,
                    "NetworkReceiveMBPerSecond": 0,
                    "NetworkSendMBPerSecond": 0,
                    "P95LatencyMs": 0,
                    "P99LatencyMs": 0,
                    "QueueDepth": 0,
                    "RequestsPerSecond": 0,
                    "TimePerOutputTokenP99Ms": 0,
                    "TimeToFirstTokenP99Ms": 0,
                    "TokenThroughput": 0
                },
                "ModelIdentifier": "xgbxgb",
                "ModelName": "xgboost",
                "Replicas": {
                    "Available": 0,
                    "Desired": 1
                },
                "ServiceId": "svc-20260606214706-paqu",
                "ServiceName": "xgboost-xgbxgb",
                "Status": "Failed"
            }
        ],
        "Page": 1,
        "PageSize": 20,
        "Total": 8,
        "TotalPages": 1,
        "RequestId": "5d885425-46a9-488d-b5ea-0ba9958d6ec0"
    }
}
```

