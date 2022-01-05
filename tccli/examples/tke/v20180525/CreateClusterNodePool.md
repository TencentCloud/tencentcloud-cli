**Example 1: 创建节点池**



Input: 

```
tccli tke CreateClusterNodePool --cli-unfold-argument  \
    --ClusterId cls-xxxxxx \
    --AutoScalingGroupPara {"AutoScalingGroupName":"","MaxSize":1,"MinSize":0,"DesiredCapacity":1,"VpcId":"vpc-xxx","SubnetIds":["subnet-xxx"],"RetryPolicy":"IMMEDIATE_RETRY","ServiceSettings":{"ScalingMode":"CLASSIC_SCALING"}} \
    --LaunchConfigurePara {"LaunchConfigurationName":"","InstanceType":"SA2.SMALL1","SystemDisk":{"DiskType":"CLOUD_PREMIUM","DiskSize":50},"InternetAccessible":{"InternetChargeType":"TRAFFIC_POSTPAID_BY_HOUR","InternetMaxBandwidthOut":0,"PublicIpAssigned":false},"LoginSettings":{"Password":"xxx"},"SecurityGroupIds":["sg-xxx"],"EnhancedService":{"SecurityService":{"Enabled":true},"MonitorService":{"Enabled":true}},"InstanceChargeType":"POSTPAID_BY_HOUR"} \
    --InstanceAdvancedSettings.MountTarget xxx \
    --EnableAutoscale true \
    --InstanceAdvancedSettings.DesiredPodNumber 0 \
    --InstanceAdvancedSettings.PreStartUserScript xx
```

Output: 
```
{
    "Response": {
        "NodePoolId": "np-xxx",
        "RequestId": "xxx-xxx-xxxx-xxx-xxxxx"
    }
}
```

