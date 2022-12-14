**Example 1: 集群扩容**



Input: 

```
tccli emr ScaleOutCluster --cli-unfold-argument  \
    --PodSpecInfo.PodParameter.InstanceId xx \
    --PodSpecInfo.PodParameter.Parameter xx \
    --PodSpecInfo.PodParameter.Config xx \
    --PodSpecInfo.PodSpec.VpcId xx \
    --PodSpecInfo.PodSpec.ResourceProviderIdentifier xx \
    --PodSpecInfo.PodSpec.EnableDynamicSpecFlag True \
    --PodSpecInfo.PodSpec.ResourceProviderType xx \
    --PodSpecInfo.PodSpec.NodeFlag xx \
    --PodSpecInfo.PodSpec.DynamicPodSpec.LimitMemory 0.0 \
    --PodSpecInfo.PodSpec.DynamicPodSpec.RequestMemory 0.0 \
    --PodSpecInfo.PodSpec.DynamicPodSpec.LimitCpu 0.0 \
    --PodSpecInfo.PodSpec.DynamicPodSpec.RequestCpu 0.0 \
    --PodSpecInfo.PodSpec.PodName xx \
    --PodSpecInfo.PodSpec.Memory 1 \
    --PodSpecInfo.PodSpec.SubnetId xx \
    --PodSpecInfo.PodSpec.CpuType xx \
    --PodSpecInfo.PodSpec.PodVolumes.0.VolumeType xx \
    --PodSpecInfo.PodSpec.PodVolumes.0.HostVolume.VolumePath xx \
    --PodSpecInfo.PodSpec.PodVolumes.0.PVCVolume.DiskSize 1 \
    --PodSpecInfo.PodSpec.PodVolumes.0.PVCVolume.DiskNum 0 \
    --PodSpecInfo.PodSpec.PodVolumes.0.PVCVolume.DiskType xx \
    --PodSpecInfo.PodSpec.Cpu 1 \
    --ResourceSpec.DataDisk.0.Count 0 \
    --ResourceSpec.DataDisk.0.DiskSize 0 \
    --ResourceSpec.DataDisk.0.DiskType xx \
    --ResourceSpec.SystemDisk.0.Count 0 \
    --ResourceSpec.SystemDisk.0.DiskSize 0 \
    --ResourceSpec.SystemDisk.0.DiskType xx \
    --ResourceSpec.LocalDataDisk.0.Count 0 \
    --ResourceSpec.LocalDataDisk.0.DiskSize 0 \
    --ResourceSpec.LocalDataDisk.0.DiskType xx \
    --ResourceSpec.InstanceType xx \
    --ResourceSpec.Tags.0.TagKey xx \
    --ResourceSpec.Tags.0.TagValue xx \
    --SoftDeployInfo 0 \
    --Zone xx \
    --ScriptBootstrapActionConfig.0.CosFileName xx \
    --ScriptBootstrapActionConfig.0.Args xx \
    --ScriptBootstrapActionConfig.0.CosFileURI xx \
    --ScriptBootstrapActionConfig.0.ExecutionMoment xx \
    --Tags.0.TagKey xx \
    --Tags.0.TagValue xx \
    --InstanceId xx \
    --ClickHouseClusterName xx \
    --YarnNodeLabel xx \
    --ClickHouseClusterType xx \
    --ServiceNodeInfo 0 \
    --InstanceChargeType xx \
    --HardwareSourceType xx \
    --ScaleOutNodeConfig.NodeCount 1 \
    --ScaleOutNodeConfig.NodeFlag xx \
    --ClientToken xx \
    --SubnetId xx \
    --InstanceChargePrepaid.RenewFlag True \
    --InstanceChargePrepaid.Period 0 \
    --EnableStartServiceFlag True \
    --DisasterRecoverGroupIds xx
```

Output: 
```
{
    "Response": {
        "InstanceId": "xx",
        "FlowId": 0,
        "RequestId": "xx",
        "ClientToken": "xx"
    }
}
```

