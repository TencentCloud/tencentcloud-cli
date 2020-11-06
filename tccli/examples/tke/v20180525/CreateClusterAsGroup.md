**Example 1: 创建集群的伸缩组**

创建集群的伸缩组

Input: 

```
tccli tke CreateClusterAsGroup --cli-unfold-argument  \
    --ClusterId cls-xxxxxx \
    --AutoScalingGroupPara "{"AutoScalingGroupName":"001","MaxSize":5,"MinSize":0,"VpcId":"vpc-xxxxxxx","SubnetIds":["subnet-xxxxxxx"],"RetryPolicy":"IMMEDIATE_RETRY"}" \
    --LaunchConfigurePara "{"LaunchConfigurationName":"","InstanceType":"S4.SMALL1","SystemDisk":{"DiskType":"CLOUD_PREMIUM","DiskSize":50},"InternetAccessible":{"InternetChargeType":"TRAFFIC_POSTPAID_BY_HOUR","InternetMaxBandwidthOut":1,"PublicIpAssigned":true},"LoginSettings":{"Password":"YourPassword"},"SecurityGroupIds":["sg-xxxxxxx"],"EnhancedService":{"SecurityService":{"Enabled":true},"MonitorService":{"Enabled":true}},"InstanceChargeType":"POSTPAID_BY_HOUR"}"
```

Output: 
```
{
    "Response": {
        "AutoScalingGroupId": "asg-xxxxxxx",
        "LaunchConfigurationId": "asc-xxxxxxxx",
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

