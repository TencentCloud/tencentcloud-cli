**Example 1: 创建节点池**



Input: 

```
tccli tke CreateClusterNodePool --cli-unfold-argument  \
    --AutoScalingGroupPara {"AutoScalingGroupName":"","MaxSize":20,"MinSize":0,"DesiredCapacity":2,"VpcId":"vpc-2ln96dly","SubnetIds":["subnet-40bgrdix"],"MultiZoneSubnetPolicy":"PRIORITY","RetryPolicy":"IMMEDIATE_RETRY","ServiceSettings":{"ScalingMode":"CLASSIC_SCALING"}} \
    --ClusterId cls-xxxxxxx \
    --ContainerRuntime docker \
    --DeletionProtection True \
    --EnableAutoscale True \
    --InstanceAdvancedSettings.DataDisks.0.AutoFormatAndMount True \
    --InstanceAdvancedSettings.DataDisks.0.DiskSize 500 \
    --InstanceAdvancedSettings.DataDisks.0.DiskPartition xxx \
    --InstanceAdvancedSettings.DataDisks.0.DiskType CLOUD_BSSD \
    --InstanceAdvancedSettings.DataDisks.0.FileSystem xfs \
    --InstanceAdvancedSettings.DataDisks.0.MountTarget /var/lib/docker \
    --InstanceAdvancedSettings.Taints.0.Value value \
    --InstanceAdvancedSettings.Taints.0.Key key \
    --InstanceAdvancedSettings.Taints.0.Effect NoExecute \
    --InstanceAdvancedSettings.DockerGraphPath /var/lib/docker \
    --InstanceAdvancedSettings.DesiredPodNumber 0 \
    --InstanceAdvancedSettings.PreStartUserScript xxxx \
    --InstanceAdvancedSettings.GPUArgs.CUDA.Name  \
    --InstanceAdvancedSettings.GPUArgs.CUDA.Version  \
    --InstanceAdvancedSettings.GPUArgs.CUDNN.DevName  \
    --InstanceAdvancedSettings.GPUArgs.CUDNN.DocName  \
    --InstanceAdvancedSettings.GPUArgs.CUDNN.Name  \
    --InstanceAdvancedSettings.GPUArgs.CUDNN.Version  \
    --InstanceAdvancedSettings.GPUArgs.Driver.Name  \
    --InstanceAdvancedSettings.GPUArgs.Driver.Version  \
    --InstanceAdvancedSettings.GPUArgs.MIGEnable False \
    --InstanceAdvancedSettings.Unschedulable 0 \
    --InstanceAdvancedSettings.UserScript Y3VybCAtcyxxxxxxxxxxxxxcmVzb2x2LmNvbmY= \
    --Taints.0.Value value \
    --Taints.0.Key key \
    --Taints.0.Effect NoExecute \
    --Labels.0.Name node-pool \
    --Labels.0.Value xxxx \
    --LaunchConfigurePara {"LaunchConfigurationName":"","InstanceType":"S6.8XLARGE64","SystemDisk":{"DiskType":"CLOUD_BSSD","DiskSize":50},"DataDisks":[{"DiskType":"CLOUD_BSSD","DiskSize":500}],"InternetAccessible":{"InternetChargeType":"TRAFFIC_POSTPAID_BY_HOUR","InternetMaxBandwidthOut":0,"PublicIpAssigned":false},"LoginSettings":{"KeyIds":["skey-xxxxx"]},"SecurityGroupIds":["sg-xxxxxx"],"EnhancedService":{"SecurityService":{"Enabled":true},"MonitorService":{"Enabled":true}},"HostNameSettings":{"HostName":"foundation-node","HostNameStyle":"UNIQUE"},"InstanceNameSettings":{"InstanceName":"node","InstanceNameStyle":"UNIQUE"},"InstanceChargeType":"PREPAID","InstanceChargePrepaid":{"Period":1,"RenewFlag":"NOTIFY_AND_AUTO_RENEW"}} \
    --Name node-pool \
    --NodePoolOs centos7.6.0_x64 \
    --OsCustomizeType GENERAL \
    --RuntimeVersion 19.3
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

