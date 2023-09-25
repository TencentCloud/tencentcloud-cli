**Example 1: 集群扩容**



Input: 

```
tccli emr ScaleOutCluster --cli-unfold-argument  \
    --ClientToken  \
    --InstanceChargeType SPOTPAID \
    --InstanceChargePrepaid.Period 0 \
    --InstanceChargePrepaid.RenewFlag True \
    --ScriptBootstrapActionConfig.0.CosFileURI https://devops-private-1251949819.cos.na-ashburn.myqcloud.com/emr/shell/emr_init.sh \
    --ScriptBootstrapActionConfig.0.Args abc \
    --ScriptBootstrapActionConfig.0.CosFileName emr_init \
    --ScriptBootstrapActionConfig.0.ExecutionMoment resourceAfter \
    --InstanceId emr-ge0vrqkl \
    --SoftDeployInfo 1 2 \
    --ServiceNodeInfo 7 \
    --DisasterRecoverGroupIds abc \
    --Tags.0.TagKey Team \
    --Tags.0.TagValue data \
    --HardwareSourceType host \
    --PodSpecInfo.PodSpec.ResourceProviderIdentifier cls-a1cd23fa \
    --PodSpecInfo.PodSpec.ResourceProviderType tke \
    --PodSpecInfo.PodSpec.NodeFlag TASK \
    --PodSpecInfo.PodSpec.Cpu 1 \
    --PodSpecInfo.PodSpec.Memory 1 \
    --PodSpecInfo.PodSpec.CpuType intel \
    --PodSpecInfo.PodSpec.PodVolumes.0.VolumeType abc \
    --PodSpecInfo.PodSpec.PodVolumes.0.PVCVolume.DiskSize 1 \
    --PodSpecInfo.PodSpec.PodVolumes.0.PVCVolume.DiskType abc \
    --PodSpecInfo.PodSpec.PodVolumes.0.PVCVolume.DiskNum 0 \
    --PodSpecInfo.PodSpec.PodVolumes.0.HostVolume.VolumePath abc \
    --PodSpecInfo.PodSpec.EnableDynamicSpecFlag True \
    --PodSpecInfo.PodSpec.DynamicPodSpec.RequestCpu 0 \
    --PodSpecInfo.PodSpec.DynamicPodSpec.LimitCpu 0 \
    --PodSpecInfo.PodSpec.DynamicPodSpec.RequestMemory 0 \
    --PodSpecInfo.PodSpec.DynamicPodSpec.LimitMemory 0 \
    --PodSpecInfo.PodSpec.VpcId vpc-d1c351hq \
    --PodSpecInfo.PodSpec.SubnetId subnet-lnejfj4p \
    --PodSpecInfo.PodSpec.PodName podeee \
    --PodSpecInfo.PodParameter.InstanceId abc \
    --PodSpecInfo.PodParameter.Config abc \
    --PodSpecInfo.PodParameter.Parameter abc \
    --ClickHouseClusterName abc \
    --ClickHouseClusterType new \
    --YarnNodeLabel abc \
    --EnableStartServiceFlag True \
    --ResourceSpec.Tags.0.TagKey abc \
    --ResourceSpec.Tags.0.TagValue abc \
    --ResourceSpec.InstanceType SA2.4XLARGE64 \
    --ResourceSpec.SystemDisk.0.Count 1 \
    --ResourceSpec.SystemDisk.0.DiskType CLOUD_PREMIUM \
    --ResourceSpec.SystemDisk.0.DiskSize 70 \
    --ResourceSpec.DataDisk.0.Count 1 \
    --ResourceSpec.DataDisk.0.DiskType CLOUD_HSSD \
    --ResourceSpec.DataDisk.0.DiskSize 70 \
    --ResourceSpec.LocalDataDisk.0.Count 1 \
    --ResourceSpec.LocalDataDisk.0.DiskType CLOUD_HSSD \
    --ResourceSpec.LocalDataDisk.0.DiskSize 100 \
    --Zone ap-shanghai-5 \
    --SubnetId subnet-lnejfj4p \
    --ScaleOutNodeConfig.NodeFlag CORE \
    --ScaleOutNodeConfig.NodeCount 1
```

Output: 
```
{
    "Response": {
        "InstanceId": "emr-ge0vrqkl",
        "ClientToken": "",
        "FlowId": 0,
        "RequestId": "1e5c1189-bd1d-4cd7-ab49-72ed158c482c"
    }
}
```

