**Example 1: 创建第三方节点池**

创建注册节点池

Input: 

```
tccli tke CreateExternalNodePool --cli-unfold-argument  \
    --ClusterId cls-lm91rql0 \
    --InstanceAdvancedSettings.PreStartUserScript xx \
    --InstanceAdvancedSettings.DockerGraphPath xx \
    --InstanceAdvancedSettings.Labels.0.Name xx \
    --InstanceAdvancedSettings.Labels.0.Value xx \
    --InstanceAdvancedSettings.ExtraArgs.Kubelet xx \
    --InstanceAdvancedSettings.Taints.0.Value xx \
    --InstanceAdvancedSettings.Taints.0.Key xx \
    --InstanceAdvancedSettings.Taints.0.Effect xx \
    --InstanceAdvancedSettings.Unschedulable 0 \
    --InstanceAdvancedSettings.UserScript xx \
    --InstanceAdvancedSettings.DesiredPodNumber 61 \
    --InstanceAdvancedSettings.GPUArgs.MIGEnable True \
    --InstanceAdvancedSettings.GPUArgs.CustomDriver.Address xx \
    --InstanceAdvancedSettings.GPUArgs.Driver.Version xx \
    --InstanceAdvancedSettings.GPUArgs.Driver.Name xx \
    --InstanceAdvancedSettings.GPUArgs.CUDA.Version xx \
    --InstanceAdvancedSettings.GPUArgs.CUDA.Name xx \
    --InstanceAdvancedSettings.GPUArgs.CUDNN.DocName xx \
    --InstanceAdvancedSettings.GPUArgs.CUDNN.Version xx \
    --InstanceAdvancedSettings.GPUArgs.CUDNN.Name xx \
    --InstanceAdvancedSettings.GPUArgs.CUDNN.DevName xx \
    --InstanceAdvancedSettings.MountTarget xx \
    --InstanceAdvancedSettings.DataDisks.0.DiskPartition xx \
    --InstanceAdvancedSettings.DataDisks.0.DiskType xx \
    --InstanceAdvancedSettings.DataDisks.0.DiskSize 0 \
    --InstanceAdvancedSettings.DataDisks.0.FileSystem xx \
    --InstanceAdvancedSettings.DataDisks.0.AutoFormatAndMount True \
    --InstanceAdvancedSettings.DataDisks.0.MountTarget xx \
    --Name IDC节点池 \
    --ContainerRuntime docker \
    --RuntimeVersion 19.3 \
    --Labels.0.Name lkong1 \
    --Labels.0.Value lkong1 \
    --Labels.1.Name tke.cloud.tencent.com/location \
    --Labels.1.Value gz
```

Output: 
```
{
    "Response": {
        "NodePoolId": "np-kennkdng",
        "RequestId": "4c6c63c7-b23e-4896-bf3b-6bc44dxxxxxx"
    }
}
```

