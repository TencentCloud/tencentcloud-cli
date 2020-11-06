**Example 1: Extending Cluster Nodes**



Input: 

```
tccli tke CreateClusterInstances --cli-unfold-argument  \
    --ClusterId cls-xxxxxxxx \
    --RunInstancePara {"Placement":{"Zone":"ap-guangzhou-4"},"InstanceType":"S3.SMALL1"}
```

Output: 
```
{
    "Response": {
        "InstanceIdSet": [
            "ins-xxxxxxxx"
        ],
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

**Example 2: Adding cluster nodes (multiple data disks)**

Adding a node with multiple data disks to a cluster
Note 1: set DataDisks in InstanceAdvancedSettings to set the mounting information for multiple data disks. The backend will match data disks with data disk IDs based on their types and sizes and mount them to the corresponding paths.
Note 2: set DataDisks in RunInstancePara. This parameter will be passed through to the CVM to indicate the purchase of multiple data disks.
Note 3: `MountTarget` in InstanceAdvancedSettings initially supported single-disk configuration but is discarded in multi-disk scenarios, so it does not need to be entered here.

Input: 

```
tccli tke CreateClusterInstances --cli-unfold-argument  \
    --Action CreateClusterInstances \
    --ApiModule tke \
    --AppId 123 \
    --ClientIp 127.0.0.1 \
    --ClusterId cls-qxxxxxx \
    --InstanceAdvancedSettings.DataDisks.0.AutoFormatAndMount True \
    --InstanceAdvancedSettings.DataDisks.0.DiskSize 50 \
    --InstanceAdvancedSettings.DataDisks.0.DiskType CLOUD_PREMIUM \
    --InstanceAdvancedSettings.DataDisks.0.FileSystem ext4 \
    --InstanceAdvancedSettings.DataDisks.0.MountTarget /data2 \
    --InstanceAdvancedSettings.DataDisks.1.AutoFormatAndMount True \
    --InstanceAdvancedSettings.DataDisks.1.DiskSize 120 \
    --InstanceAdvancedSettings.DataDisks.1.DiskType CLOUD_PREMIUM \
    --InstanceAdvancedSettings.DataDisks.1.FileSystem ext4 \
    --InstanceAdvancedSettings.DataDisks.1.MountTarget /data4 \
    --InstanceAdvancedSettings.DataDisks.2.AutoFormatAndMount True \
    --InstanceAdvancedSettings.DataDisks.2.DiskSize 100 \
    --InstanceAdvancedSettings.DataDisks.2.DiskType CLOUD_PREMIUM \
    --InstanceAdvancedSettings.DataDisks.2.FileSystem ext4 \
    --InstanceAdvancedSettings.DataDisks.2.MountTarget /data3 \
    --InstanceAdvancedSettings.DataDisks.3.AutoFormatAndMount True \
    --InstanceAdvancedSettings.DataDisks.3.DiskSize 50 \
    --InstanceAdvancedSettings.DataDisks.3.DiskType CLOUD_PREMIUM \
    --InstanceAdvancedSettings.DataDisks.3.FileSystem ext4 \
    --InstanceAdvancedSettings.DataDisks.3.MountTarget /data5 \
    --InstanceAdvancedSettings.DockerGraphPath /var/lib/docker \
    --InstanceAdvancedSettings.MountTarget /var/lib/docker \
    --InstanceAdvancedSettings.Unschedulable 0 \
    --InstanceAdvancedSettings.UserScript  \
    --Language zh-CN \
    --Region ap-chongqing \
    --RequestId 76a8bf8c-c039-4f52-ab31-5be5cafc53e3 \
    --RequestSource MC \
    --RunInstancePara {"InstanceChargeType":"POSTPAID_BY_HOUR","Placement":{"Zone":"ap-chongqing-1","ProjectId":0},"InstanceType":"S3.SMALL1","SystemDisk":{"DiskType":"CLOUD_PREMIUM","DiskSize":50},"DataDisks":[{"DiskType":"CLOUD_PREMIUM","DiskSize":50},{"DiskType":"CLOUD_PREMIUM","DiskSize":120},{"DiskType":"CLOUD_PREMIUM","DiskSize":100},{"DiskType":"CLOUD_PREMIUM","DiskSize":50}],"VirtualPrivateCloud":{"VpcId":"vpc-d5ivotej","SubnetId":"subnet-qh3ax3mo","AsVpcGateway":false},"InternetAccessible":{"InternetChargeType":"TRAFFIC_POSTPAID_BY_HOUR","InternetMaxBandwidthOut":1,"PublicIpAssigned":true},"InstanceCount":1,"ImageId":"img-xxxxxx","InstanceName":"tke_cls-xxx_worker","LoginSettings":{"KeyIds":["skey-cxxxx"]},"SecurityGroupIds":["sg-nxxxxxx"],"EnhancedService":{"SecurityService":{"Enabled":true},"MonitorService":{"Enabled":true}}} \
    --SubAccountUin 123 \
    --Timestamp 1574854507 \
    --Token  \
    --Uin 12345678 \
    --Version 2018-05-25
```

Output: 
```
{
    "Response": {
        "InstanceIdSet": [
            "ins-xxxxxxxx"
        ],
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

