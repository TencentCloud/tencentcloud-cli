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
    "DiskOperationLogSet": [
        {
            "OperationState": "SUCCESS",
            "StartTime": "2018-09-19 20:40:20",
            "Operator": "100004375281",
            "Operation": "CBS_OPERATION_MODIFY",
            "EndTime": "2018-09-19 20:40:20",
            "DiskId": "disk-ou4acu4i"
        },
        {
            "OperationState": "SUCCESS",
            "StartTime": "2018-09-19 20:40:16",
            "Operator": "100004375281",
            "Operation": "CBS_OPERATION_MODIFY",
            "EndTime": "2018-09-19 20:40:16",
            "DiskId": "disk-ou4acu4i"
        },
        {
            "OperationState": "SUCCESS",
            "StartTime": "2018-09-19 20:40:13",
            "Operator": "100004375281",
            "Operation": "CBS_OPERATION_EXPAND",
            "EndTime": "2018-09-19 20:40:13",
            "DiskId": "disk-ou4acu4i"
        },
        {
            "OperationState": "SUCCESS",
            "StartTime": "2018-09-19 20:39:59",
            "Operator": "100004375281",
            "Operation": "CBS_OPERATION_CREATE",
            "EndTime": "2018-09-19 20:39:59",
            "DiskId": "disk-ou4acu4i"
        }
    ]
}
```

