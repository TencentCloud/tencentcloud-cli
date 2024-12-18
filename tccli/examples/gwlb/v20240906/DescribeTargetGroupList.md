**Example 1: 获取目标组列表**

获取目标组列表

Input: 

```
tccli gwlb DescribeTargetGroupList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "RequestId": "5c5003ab-126b-4649-8c86-0a98f34cfe12",
        "TargetGroupSet": [
            {
                "AllDeadToAlive": true,
                "AssociatedRule": null,
                "AssociatedRuleCount": 1,
                "CreatedTime": "2024-10-15T00:00:00+00:00",
                "HealthCheck": {
                    "HealthNum": 3,
                    "HealthSwitch": true,
                    "IntervalTime": 5,
                    "Port": 0,
                    "Protocol": "icmp",
                    "Timeout": 2,
                    "UnHealthNum": 3
                },
                "Port": 6081,
                "Protocol": "tencent_geneve",
                "RegisteredInstancesCount": 1,
                "ScheduleAlgorithm": "ip_hash_3_elastic",
                "TargetGroupId": "lbtg-kbsv74pw",
                "TargetGroupName": "targetgroup1727599151",
                "UpdatedTime": "2024-10-15T00:00:00+00:00",
                "VpcId": "vpc-ojtgv3oh"
            },
            {
                "AllDeadToAlive": true,
                "AssociatedRule": null,
                "AssociatedRuleCount": 0,
                "CreatedTime": "2024-10-15T00:00:00+00:00",
                "HealthCheck": {
                    "HealthNum": 3,
                    "HealthSwitch": true,
                    "IntervalTime": 5,
                    "Port": 0,
                    "Protocol": "icmp",
                    "Timeout": 2,
                    "UnHealthNum": 3
                },
                "Port": 6081,
                "Protocol": "tencent_geneve",
                "RegisteredInstancesCount": 0,
                "ScheduleAlgorithm": "ip_hash_3_elastic",
                "TargetGroupId": "lbtg-141xpe2w",
                "TargetGroupName": "targetgroup1727175745",
                "UpdatedTime": "2024-10-15T00:00:00+00:00",
                "VpcId": "vpc-ojtgv3oh"
            },
            {
                "AllDeadToAlive": true,
                "AssociatedRule": null,
                "AssociatedRuleCount": 0,
                "CreatedTime": "2024-10-15T00:00:00+00:00",
                "HealthCheck": {
                    "HealthNum": 3,
                    "HealthSwitch": true,
                    "IntervalTime": 5,
                    "Port": 0,
                    "Protocol": "icmp",
                    "Timeout": 2,
                    "UnHealthNum": 3
                },
                "Port": 6081,
                "Protocol": "tencent_geneve",
                "RegisteredInstancesCount": 0,
                "ScheduleAlgorithm": "ip_hash_3_elastic",
                "TargetGroupId": "lbtg-myhtwkrw",
                "TargetGroupName": "targetgroup1726747698",
                "UpdatedTime": "2024-10-15T00:00:00+00:00",
                "VpcId": "vpc-ojtgv3oh"
            }
        ],
        "TotalCount": 3
    }
}
```

