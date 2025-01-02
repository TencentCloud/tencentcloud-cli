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
    --ClusterId cls-e55paxnt \
    --InstanceAdvancedSettings.MountTarget test \
    --InstanceAdvancedSettings.DockerGraphPath test \
    --InstanceAdvancedSettings.UserScript test \
    --InstanceAdvancedSettings.Unschedulable 0 \
    --InstanceAdvancedSettings.Labels.0.Name test \
    --InstanceAdvancedSettings.Labels.0.Value test \
    --InstanceAdvancedSettings.DataDisks.0.DiskType test \
    --InstanceAdvancedSettings.DataDisks.0.FileSystem test \
    --InstanceAdvancedSettings.DataDisks.0.DiskSize 0 \
    --InstanceAdvancedSettings.DataDisks.0.AutoFormatAndMount True \
    --InstanceAdvancedSettings.DataDisks.0.MountTarget test \
    --InstanceAdvancedSettings.DataDisks.0.DiskPartition test \
    --InstanceAdvancedSettings.ExtraArgs.Kubelet test \
    --InstanceAdvancedSettings.DesiredPodNumber 0 \
    --InstanceAdvancedSettings.GPUArgs.MIGEnable True \
    --InstanceAdvancedSettings.GPUArgs.Driver.Version test \
    --InstanceAdvancedSettings.GPUArgs.Driver.Name test \
    --InstanceAdvancedSettings.GPUArgs.CUDA.Version test \
    --InstanceAdvancedSettings.GPUArgs.CUDA.Name test \
    --InstanceAdvancedSettings.GPUArgs.CUDNN.Version test \
    --InstanceAdvancedSettings.GPUArgs.CUDNN.Name test \
    --InstanceAdvancedSettings.GPUArgs.CUDNN.DocName test \
    --InstanceAdvancedSettings.GPUArgs.CUDNN.DevName test \
    --InstanceAdvancedSettings.GPUArgs.CustomDriver.Address test \
    --InstanceAdvancedSettings.PreStartUserScript test \
    --InstanceAdvancedSettings.Taints.0.Key test \
    --InstanceAdvancedSettings.Taints.0.Value test \
    --InstanceAdvancedSettings.Taints.0.Effect test \
    --RunInstancePara test \
    --SkipValidateOptions test
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

