**Example 1: 扩展集群节点示例**

扩展集群节点

Input: 

```
tccli tke CreateClusterInstances --cli-unfold-argument  \
    --RunInstancePara {"Placement":{"Zone":"ap-guangzhou-4"},"InstanceType":"S3.SMALL1"} \
    --ClusterId cls-e55paxnt
```

Output: 
```
{
    "Response": {
        "InstanceIdSet": [
            "ins-e55paxnt"
        ],
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

**Example 2: 添加集群节点(多块数据盘）**

添加带有多个数据盘的节点到集群
注意1: InstanceAdvancedSettings设置DataDisks,  多盘数据盘挂载信息，后端会根据盘的类型、大小匹配数据盘ID，将对应的路径挂载
注意2: RunInstancePara设置DataDisks, 此参数透传给CVM，购买多块数据盘
注意3: InstanceAdvancedSettings的MountTarget早期是支持单盘的，多盘场景废弃，无需填写

Input: 

```
tccli tke CreateClusterInstances --cli-unfold-argument  \
    --ClusterId cls-nfjdk3n0 \
    --InstanceAdvancedSettings.DesiredPodNumber 120 \
    --InstanceAdvancedSettings.Taints None \
    --InstanceAdvancedSettings.DataDisks.0.AutoFormatAndMount True \
    --InstanceAdvancedSettings.DataDisks.0.DiskSize 50 \
    --InstanceAdvancedSettings.DataDisks.0.DiskType CLOUD_BSSD \
    --InstanceAdvancedSettings.DataDisks.0.FileSystem ext4 \
    --InstanceAdvancedSettings.DataDisks.0.MountTarget /run \
    --InstanceAdvancedSettings.DataDisks.0.DiskPartition /dev/vda \
    --InstanceAdvancedSettings.DataDisks.1.AutoFormatAndMount True \
    --InstanceAdvancedSettings.DataDisks.1.DiskSize 50 \
    --InstanceAdvancedSettings.DataDisks.1.DiskType CLOUD_BSSD \
    --InstanceAdvancedSettings.DataDisks.1.FileSystem ext4 \
    --InstanceAdvancedSettings.DataDisks.1.MountTarget /var/lib/data2 \
    --InstanceAdvancedSettings.DataDisks.1.DiskPartition /dev/vda \
    --InstanceAdvancedSettings.DockerGraphPath  \
    --InstanceAdvancedSettings.GPUArgs.CUDA.Name  \
    --InstanceAdvancedSettings.GPUArgs.CUDA.Version  \
    --InstanceAdvancedSettings.GPUArgs.CUDNN.DevName  \
    --InstanceAdvancedSettings.GPUArgs.CUDNN.DocName  \
    --InstanceAdvancedSettings.GPUArgs.CUDNN.Name  \
    --InstanceAdvancedSettings.GPUArgs.CUDNN.Version  \
    --InstanceAdvancedSettings.GPUArgs.Driver.Name  \
    --InstanceAdvancedSettings.GPUArgs.Driver.Version  \
    --InstanceAdvancedSettings.GPUArgs.MIGEnable False \
    --InstanceAdvancedSettings.PreStartUserScript  \
    --InstanceAdvancedSettings.Unschedulable 0 \
    --InstanceAdvancedSettings.UserScript  \
    --RunInstancePara {"InstanceChargeType":"POSTPAID_BY_HOUR","Placement":{"Zone":"ap-beijing-1","ProjectId":0},"InstanceType":"S5.LARGE8","SystemDisk":{"DiskType":"CLOUD_BSSD","DiskSize":50},"DataDisks":[{"DiskType":"CLOUD_BSSD","DiskSize":50},{"DiskType":"CLOUD_BSSD","DiskSize":50}],"VirtualPrivateCloud":{"VpcId":"vpc-fcccepnm","SubnetId":"subnet-f6c7fr8d","AsVpcGateway":false,"Ipv6AddressCount":0},"InternetAccessible":{"InternetChargeType":"TRAFFIC_POSTPAID_BY_HOUR","InternetMaxBandwidthOut":0,"PublicIpAssigned":false},"InstanceCount":1,"ImageId":"img-fqais24x","HostName":"tke","InstanceName":"tke","LoginSettings":{"KeyIds":["skey-f6c7fr8d"]},"SecurityGroupIds":["sg-f6c7fr8d"],"EnhancedService":{"SecurityService":{"Enabled":true},"MonitorService":{"Enabled":true}}}
```

Output: 
```
{
    "Response": {
        "InstanceIdSet": [
            "ins-e55paxnt"
        ],
        "RequestId": "eac6b301-a322-493a-8e36-83b295459397"
    }
}
```

