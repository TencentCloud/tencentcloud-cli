**Example 1: 获取全局维护窗口和排除项**

获取全局维护窗口和排除项

Input: 

```
tccli tke DescribeGlobalMaintenanceWindowAndExclusions --cli-unfold-argument  \
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
                "ID": 1,
                "TargetRegions": [
                    "*"
                ],
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

