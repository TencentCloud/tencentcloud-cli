**Example 1: 创建节点池**



Input: 

```
tccli tke CreateClusterNodePool --cli-unfold-argument  \
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
    --InstanceAdvancedSettings.DesiredPodNumber 0 \
    --InstanceAdvancedSettings.MountTarget xx \
    --InstanceAdvancedSettings.DataDisks.0.DiskPartition xx \
    --InstanceAdvancedSettings.DataDisks.0.DiskType xx \
    --InstanceAdvancedSettings.DataDisks.0.DiskSize 0 \
    --InstanceAdvancedSettings.DataDisks.0.FileSystem xx \
    --InstanceAdvancedSettings.DataDisks.0.AutoFormatAndMount True \
    --InstanceAdvancedSettings.DataDisks.0.MountTarget xx \
    --LaunchConfigurePara xx \
    --OsCustomizeType xx \
    --Name xx \
    --RuntimeVersion xx \
    --Tags.0.Value xx \
    --Tags.0.Key xx \
    --Labels.0.Name xx \
    --Labels.0.Value xx \
    --ClusterId xx \
    --Taints.0.Value xx \
    --Taints.0.Key xx \
    --Taints.0.Effect xx \
    --EnableAutoscale True \
    --ContainerRuntime xx \
    --AutoScalingGroupPara xx \
    --NodePoolOs xx
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

