**Example 1: 创建集群维护窗口和排除项**

创建集群维护窗口和排除项

Input: 

```
tccli tke CreateClusterMaintenanceWindowAndExclusions --cli-unfold-argument  \
    --ClusterID cls-3n90hta2 \
    --MaintenanceTime 20:00:00 \
    --Duration 4 \
    --DayOfWeek MO TU WE TH FR
```

Output: 
```
{
    "Response": {
        "RequestId": "f1048559-c7e4-4a7b-9d12-bc0256be3e26"
    }
}
```

