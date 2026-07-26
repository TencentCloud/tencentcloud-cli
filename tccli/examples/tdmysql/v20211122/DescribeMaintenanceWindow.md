**Example 1: 查询运维时间窗口**



Input: 

```
tccli tdmysql DescribeMaintenanceWindow --cli-unfold-argument  \
    --InstanceId tdsql3-99c63ac1
```

Output: 
```
{
    "Response": {
        "InstanceId": "tdsql3-99c63ac1",
        "MaintenanceWindow": "01:00-02:00",
        "WeekDays": [
            "Monday"
        ],
        "RequestId": "e86bfa23-997d-4033-88d8-44d93da43f0b"
    }
}
```

