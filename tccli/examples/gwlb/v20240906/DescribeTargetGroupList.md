**Example 1: 获取目标组列表**

获取目标组列表

Input: 

```
tccli gwlb DescribeTargetGroupList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "TargetGroupSet": [
            {
                "TargetGroupId": "abc",
                "VpcId": "abc",
                "TargetGroupName": "abc",
                "Port": 1,
                "CreatedTime": "2020-09-22T00:00:00+00:00",
                "UpdatedTime": "2020-09-22T00:00:00+00:00",
                "AssociatedRule": [
                    {
                        "LoadBalancerId": "abc",
                        "LoadBalancerName": "abc"
                    }
                ],
                "Protocol": "abc",
                "ScheduleAlgorithm": "abc",
                "HealthCheck": {
                    "HealthSwitch": true,
                    "Protocol": "abc",
                    "Port": 0,
                    "Timeout": 0,
                    "IntervalTime": 0,
                    "HealthNum": 0,
                    "UnHealthNum": 0
                },
                "AllDeadToAlive": true,
                "AssociatedRuleCount": 0
            }
        ],
        "RequestId": "abc"
    }
}
```

