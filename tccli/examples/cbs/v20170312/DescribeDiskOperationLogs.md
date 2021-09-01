**Example 1: 查询云盘操作日志**



Input: 

```
tccli cbs DescribeDiskOperationLogs --cli-unfold-argument  \
    --Filters.0.Name disk-id \
    --Filters.0.Values disk-ou4acu4i
```

Output: 
```
{
    "Response": {
        "RequestId": "xx",
        "DiskOperationLogSet": [
            {
                "OperationState": "xx",
                "StartTime": "xx",
                "Operator": "xx",
                "Operation": "xx",
                "EndTime": "xx",
                "DiskId": "xx"
            }
        ]
    }
}
```

