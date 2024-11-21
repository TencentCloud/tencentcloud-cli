**Example 1: 查询实例**

根据指定实例 ID 或过滤条件查询实例的相关信息。

Input: 

```
tccli as DescribeAutoScalingInstances --cli-unfold-argument  \
    --InstanceIds ins-1fswxz1m
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "AutoScalingInstanceSet": [
            {
                "ProtectedFromScaleIn": false,
                "Zone": "ap-guangzhou-3",
                "LaunchConfigurationId": "asc-5fzsm72a",
                "InstanceId": "ins-1fswxz1m",
                "VersionNumber": 1,
                "DisasterRecoverGroupIds": [],
                "AddTime": "2018-08-21T12:05:12Z",
                "CreationType": "AUTO_CREATION",
                "AutoScalingGroupName": "asgname",
                "AutoScalingGroupId": "asg-4o61gsxi",
                "HealthStatus": "HEALTHY",
                "LifeCycleState": "IN_SERVICE",
                "LaunchConfigurationName": "系列2本地盘",
                "InstanceType": "S2.SMALL2",
                "WarmupStatus": "IN_WARMUP"
            }
        ],
        "RequestId": "2ae3e836-d47a-431c-b54b-4e1c2f419e5b"
    }
}
```

