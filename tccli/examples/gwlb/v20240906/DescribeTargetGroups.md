**Example 1: 根据ID查询目标组信息**

根据ID查询目标组信息

Input: 

```
tccli gwlb DescribeTargetGroups --cli-unfold-argument  \
    --TargetGroupIds lbtg-5xunivs0
```

Output: 
```
{
    "Response": {
        "RequestId": "7ae76f16-a859-449a-a43e-674c229999cc",
        "TargetGroupSet": [
            {
                "AllDeadToAlive": false,
                "AssociatedRule": [
                    {
                        "LoadBalancerId": "gwlb-poqv7z4y",
                        "LoadBalancerName": "test-gwlb-2"
                    }
                ],
                "CreatedTime": "2024-09-04T14:30:45+08:00",
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
                "Protocol": "geneve",
                "ScheduleAlgorithm": "ip_hash_3",
                "TargetGroupId": "lbtg-5xunivs0",
                "TargetGroupName": "gwlb-tar-5",
                "UpdatedTime": "2024-09-04T14:30:44+08:00",
                "VpcId": "vpc-drpj1tv1"
            }
        ],
        "TotalCount": 1
    }
}
```

**Example 2: 根据条件查询目标组信息**

根据条件查询目标组信息

Input: 

```
tccli gwlb DescribeTargetGroups --cli-unfold-argument  \
    --Filters.0.Values vpc-drpj1tv1 \
    --Filters.0.Name TargetGroupVpcId
```

Output: 
```
{
    "Response": {
        "RequestId": "7ae76f16-a859-449a-a43e-674c229999cc",
        "TargetGroupSet": [
            {
                "AllDeadToAlive": false,
                "AssociatedRule": [
                    {
                        "LoadBalancerId": "gwlb-poqv7z4y",
                        "LoadBalancerName": "test-gwlb-2"
                    }
                ],
                "CreatedTime": "2024-09-04T14:30:45+08:00",
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
                "Protocol": "geneve",
                "ScheduleAlgorithm": "ip_hash_3",
                "TargetGroupId": "lbtg-5xunivs0",
                "TargetGroupName": "gwlb-tar-5",
                "UpdatedTime": "2024-09-04T14:30:44+08:00",
                "VpcId": "vpc-drpj1tv1"
            }
        ],
        "TotalCount": 1
    }
}
```

