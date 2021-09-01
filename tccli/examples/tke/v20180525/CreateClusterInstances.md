**Example 1: 扩展集群节点示例**



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

**Example 2: 添加集群节点(多块数据盘）**

添加带有多个数据盘的节点到集群
注意1: InstanceAdvancedSettings设置DataDisks,  多盘数据盘挂载信息，后端会根据盘的类型、大小匹配数据盘ID，将对应的路径挂载
注意2: RunInstancePara设置DataDisks, 此参数透传给CVM，购买多块数据盘
注意3: InstanceAdvancedSettings的MountTarget早期是支持单盘的，多盘场景废弃，无需填写

Input: 

```
tccli tke CreateClusterInstances --cli-unfold-argument  \
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
    --SkipValidateOptions GlobalRouteCIDRCheck VpcCniCIDRCheck \
    --RunInstancePara xx \
    --ClusterId cls-xxxxx
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

