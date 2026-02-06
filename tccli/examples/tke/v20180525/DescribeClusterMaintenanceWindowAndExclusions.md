**Example 1: 获取集群维护窗口和排除项**

获取集群维护窗口和排除项

Input: 

```
tccli tke DescribeClusterMaintenanceWindowAndExclusions --cli-unfold-argument  \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "RequestId": "f1048559-c7e4-4a7b-9d12-bc0256be3e26",
        "TotalCount": 1,
        "MaintenanceWindowAndExclusions": [
            {
                "ClusterID": "cls-12345678",
                "ClusterName": "test1",
                "Region": "ap-guangzhou",
                "MaintenanceTime": "20:00:00",
                "Duration": 3,
                "DayOfWeek": [
                    "MO",
                    "WE"
                ],
                "Exclusions": []
            }
        ]
    }
}
```

