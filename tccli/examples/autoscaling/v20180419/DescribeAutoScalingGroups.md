**Example 1: 查询伸缩组**

指定伸缩组ID查询伸缩组

Input: 

```
tccli as DescribeAutoScalingGroups --cli-unfold-argument  \
    --AutoScalingGroupIds asg-pts6qcgp
```

Output: 
```
{
    "Response": {
        "AutoScalingGroupSet": [
            {
                "InActivityStatus": "NOT_IN_ACTIVITY",
                "LoadBalancerIdSet": [],
                "RetryPolicy": "IMMEDIATE_RETRY",
                "InServiceInstanceCount": 0,
                "CreatedTime": "2022-04-21T03:21:14Z",
                "SpotMixedAllocationPolicy": {
                    "CompensateWithBaseInstance": null,
                    "SpotAllocationStrategy": null,
                    "OnDemandPercentageAboveBaseCapacity": null,
                    "BaseCapacity": null
                },
                "VpcId": "vpc-lceuvai4",
                "InstanceAllocationPolicy": "LAUNCH_CONFIGURATION",
                "Tags": [],
                "LaunchConfigurationId": "asc-mo1woym9",
                "MaxSize": 1,
                "MultiZoneSubnetPolicy": "PRIORITY",
                "SubnetIdSet": [
                    "subnet-6qqolfi7"
                ],
                "HealthCheckType": "CLB",
                "LoadBalancerHealthCheckGracePeriod": 0,
                "ForwardLoadBalancerSet": [
                    {
                        "TargetAttributes": [
                            {
                                "Port": 8080,
                                "Weight": 10
                            }
                        ],
                        "Region": "ap-shanghai",
                        "LocationId": "loc-5dovrfov",
                        "ListenerId": "lbl-i4p05pmv",
                        "LoadBalancerId": "lb-pbx8nq2p"
                    }
                ],
                "ProjectId": 0,
                "AutoScalingGroupName": "testasg",
                "MinSize": 0,
                "ServiceSettings": {
                    "ReplaceMonitorUnhealthy": false,
                    "ReplaceLoadBalancerUnhealthy": false,
                    "ScalingMode": "CLASSIC_SCALING"
                },
                "LaunchConfigurationName": "test",
                "CapacityRebalance": false,
                "TerminationPolicySet": [
                    "OLDEST_INSTANCE"
                ],
                "AutoScalingGroupStatus": "NORMAL",
                "InstanceCount": 0,
                "DesiredCapacity": 0,
                "AutoScalingGroupId": "asg-pts6qcgp",
                "Ipv6AddressCount": 0,
                "DefaultCooldown": 300,
                "EnabledStatus": "ENABLED",
                "ZoneSet": []
            }
        ],
        "TotalCount": 1,
        "RequestId": "53a76c96-a88c-4972-8488-66d6c15a080f"
    }
}
```

**Example 2: 查询绑定了标签的伸缩组**

查询绑定了标签键值对（city:shenzhen）的伸缩组。

Input: 

```
tccli as DescribeAutoScalingGroups --cli-unfold-argument  \
    --Limit 1 \
    --Filters.0.Values shenzhen \
    --Filters.0.Name tag:city \
    --Offset 0
```

Output: 
```
{
    "Response": {
        "AutoScalingGroupSet": [
            {
                "InActivityStatus": "NOT_IN_ACTIVITY",
                "LoadBalancerIdSet": [],
                "RetryPolicy": "IMMEDIATE_RETRY",
                "InServiceInstanceCount": 0,
                "CreatedTime": "2019-10-29T02:21:26Z",
                "SpotMixedAllocationPolicy": {
                    "CompensateWithBaseInstance": null,
                    "SpotAllocationStrategy": null,
                    "OnDemandPercentageAboveBaseCapacity": null,
                    "BaseCapacity": null
                },
                "VpcId": "vpc-qmjyqjnk",
                "InstanceAllocationPolicy": "LAUNCH_CONFIGURATION",
                "Tags": [
                    {
                        "Key": "city",
                        "Value": "shenzhen"
                    }
                ],
                "LaunchConfigurationId": "asc-3d9e2zfx",
                "MaxSize": 10,
                "MultiZoneSubnetPolicy": "PRIORITY",
                "SubnetIdSet": [
                    "subnet-3cpb9yfp",
                    "subnet-c98udmmr",
                    "subnet-1xsr551x",
                    "subnet-o3ibshdr",
                    "subnet-6c7q2jhz"
                ],
                "HealthCheckType": "CVM",
                "LoadBalancerHealthCheckGracePeriod": 0,
                "ForwardLoadBalancerSet": [
                    {
                        "TargetAttributes": [
                            {
                                "Port": 8080,
                                "Weight": 10
                            }
                        ],
                        "Region": "ap-shanghai",
                        "LocationId": "",
                        "ListenerId": "lbl-aiwdu9bd",
                        "LoadBalancerId": "lb-k264wzwj"
                    },
                    {
                        "TargetAttributes": [
                            {
                                "Port": 80,
                                "Weight": 10
                            }
                        ],
                        "Region": "ap-shanghai",
                        "LocationId": "loc-qmxmx085",
                        "ListenerId": "lbl-ldjbrn65",
                        "LoadBalancerId": "lb-k264wzwj"
                    }
                ],
                "ProjectId": 0,
                "AutoScalingGroupName": "sz-asg",
                "MinSize": 0,
                "ServiceSettings": {
                    "ReplaceMonitorUnhealthy": false,
                    "ReplaceLoadBalancerUnhealthy": false,
                    "ScalingMode": "CLASSIC_SCALING"
                },
                "LaunchConfigurationName": "sz-asc",
                "CapacityRebalance": false,
                "TerminationPolicySet": [
                    "OLDEST_INSTANCE"
                ],
                "AutoScalingGroupStatus": "NORMAL",
                "InstanceCount": 0,
                "DesiredCapacity": 0,
                "AutoScalingGroupId": "asg-h71x7a3f",
                "Ipv6AddressCount": 0,
                "DefaultCooldown": 300,
                "EnabledStatus": "ENABLED",
                "ZoneSet": []
            }
        ],
        "TotalCount": 1,
        "RequestId": "53a76c96-a88c-4972-8488-66d6c15a080f"
    }
}
```

