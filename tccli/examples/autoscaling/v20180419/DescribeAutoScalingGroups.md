**Example 1: 查询伸缩组**

指定伸缩组ID查询伸缩组

Input: 

```
tccli as DescribeAutoScalingGroups --cli-unfold-argument  \
    --AutoScalingGroupIds asg-nkdwoui0
```

Output: 
```
{
    "Response": {
        "AutoScalingGroupSet": [
            {
                "LaunchConfigurationId": "asc-7vucy6ae",
                "ForwardLoadBalancerSet": [
                    {
                        "TargetAttributes": [
                            {
                                "Port": 8080,
                                "Weight": 10
                            }
                        ],
                        "LocationId": "loc-l3hmaev9",
                        "ListenerId": "lbl-ncw704sn",
                        "Region": "ap-guangzhou",
                        "LoadBalancerId": "lb-23aejgcv"
                    }
                ],
                "LoadBalancerIdSet": [],
                "InstanceCount": 1,
                "DesiredCapacity": 1,
                "AutoScalingGroupStatus": "NORMAL",
                "AutoScalingGroupId": "asg-nkdwoui0",
                "ProjectId": 0,
                "TerminationPolicySet": [
                    "OLDEST_INSTANCE"
                ],
                "AutoScalingGroupName": "vpc-7layer-lb",
                "InActivityStatus": "NOT_IN_ACTIVITY",
                "InServiceInstanceCount": 1,
                "DefaultCooldown": 301,
                "MinSize": 0,
                "MaxSize": 10,
                "VpcId": "vpc-hy436tmc",
                "LaunchConfigurationName": "启动配置1",
                "CreatedTime": "2018-09-27T02:01:28Z",
                "SubnetIdSet": [
                    "subnet-3tmerl37",
                    "subnet-b0vxjhot"
                ],
                "EnabledStatus": "ENABLED",
                "ZoneSet": []
            }
        ],
        "TotalCount": 1,
        "RequestId": "b8d3660c-bed1-40ad-9e7d-77390c9610be"
    }
}
```

**Example 2: 查询绑定了标签的伸缩组**

查询绑定了标签键值对（city:shenzhen）的伸缩组。

Input: 

```
tccli as DescribeAutoScalingGroups --cli-unfold-argument  \
    --Filters.0.Name tag:city \
    --Filters.0.Values shenzhen \
    --Offset 0 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "AutoScalingGroupSet": [
            {
                "LaunchConfigurationId": "asc-7vucy6ae",
                "ForwardLoadBalancerSet": [
                    {
                        "TargetAttributes": [
                            {
                                "Port": 8080,
                                "Weight": 10
                            }
                        ],
                        "LocationId": "loc-l3hmaev9",
                        "ListenerId": "lbl-ncw704sn",
                        "Region": "ap-guangzhou",
                        "LoadBalancerId": "lb-23aejgcv"
                    }
                ],
                "LoadBalancerIdSet": [],
                "InstanceCount": 1,
                "DesiredCapacity": 1,
                "AutoScalingGroupStatus": "NORMAL",
                "AutoScalingGroupId": "asg-nkdwoui0",
                "ProjectId": 0,
                "TerminationPolicySet": [
                    "OLDEST_INSTANCE"
                ],
                "AutoScalingGroupName": "vpc-7layer-lb",
                "InActivityStatus": "NOT_IN_ACTIVITY",
                "InServiceInstanceCount": 1,
                "DefaultCooldown": 301,
                "MinSize": 0,
                "MaxSize": 10,
                "VpcId": "vpc-hy436tmc",
                "LaunchConfigurationName": "启动配置1",
                "CreatedTime": "2018-09-27T02:01:28Z",
                "SubnetIdSet": [
                    "subnet-3tmerl37",
                    "subnet-b0vxjhot"
                ],
                "EnabledStatus": "ENABLED",
                "ZoneSet": [],
                "Tags": [
                    {
                        "Key": "city",
                        "Value": "shenzhen"
                    }
                ]
            }
        ],
        "TotalCount": 1,
        "RequestId": "b8d3660c-bed1-40ad-9e7d-77390c9610be"
    }
}
```

