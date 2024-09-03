**Example 1: 扩展集群节点示例**

扩展集群节点

Input: 

```
tccli tke CreateClusterInstances --cli-unfold-argument  \
    --RunInstancePara {"Placement":{"Zone":"ap-guangzhou-4"},"InstanceType":"S3.SMALL1"} \
    --ClusterId cls-xxxxxxxx
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
    --ClusterId abc \
    --InstanceAdvancedSettings.MountTarget abc \
    --InstanceAdvancedSettings.DockerGraphPath abc \
    --InstanceAdvancedSettings.UserScript abc \
    --InstanceAdvancedSettings.Unschedulable 0 \
    --InstanceAdvancedSettings.Labels.0.Name abc \
    --InstanceAdvancedSettings.Labels.0.Value abc \
    --InstanceAdvancedSettings.DataDisks.0.DiskType abc \
    --InstanceAdvancedSettings.DataDisks.0.FileSystem abc \
    --InstanceAdvancedSettings.DataDisks.0.DiskSize 0 \
    --InstanceAdvancedSettings.DataDisks.0.AutoFormatAndMount True \
    --InstanceAdvancedSettings.DataDisks.0.MountTarget abc \
    --InstanceAdvancedSettings.DataDisks.0.DiskPartition abc \
    --InstanceAdvancedSettings.ExtraArgs.Kubelet abc \
    --InstanceAdvancedSettings.DesiredPodNumber 0 \
    --InstanceAdvancedSettings.GPUArgs.MIGEnable True \
    --InstanceAdvancedSettings.GPUArgs.Driver.Version abc \
    --InstanceAdvancedSettings.GPUArgs.Driver.Name abc \
    --InstanceAdvancedSettings.GPUArgs.CUDA.Version abc \
    --InstanceAdvancedSettings.GPUArgs.CUDA.Name abc \
    --InstanceAdvancedSettings.GPUArgs.CUDNN.Version abc \
    --InstanceAdvancedSettings.GPUArgs.CUDNN.Name abc \
    --InstanceAdvancedSettings.GPUArgs.CUDNN.DocName abc \
    --InstanceAdvancedSettings.GPUArgs.CUDNN.DevName abc \
    --InstanceAdvancedSettings.GPUArgs.CustomDriver.Address abc \
    --InstanceAdvancedSettings.PreStartUserScript abc \
    --InstanceAdvancedSettings.Taints.0.Key abc \
    --InstanceAdvancedSettings.Taints.0.Value abc \
    --InstanceAdvancedSettings.Taints.0.Effect abc \
    --RunInstancePara abc \
    --SkipValidateOptions abc
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

