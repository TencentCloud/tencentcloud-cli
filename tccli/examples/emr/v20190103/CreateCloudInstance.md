**Example 1: 创建tke集群**



Input: 

```
tccli emr CreateCloudInstance --cli-unfold-argument  \
    --InstanceName DataEngine-8w2mzvtn \
    --ClusterClass EMR-TKE \
    --Software virtualspark-3.2.2 \
    --PlatFormType eks \
    --CosBucket dlc-test-gz-1305424723 \
    --EksClusterId cls-m88ufafu \
    --ProductId 56 \
    --ClientToken 2026-08-24 10:32:37 \
    --VPCSettings.VpcId vpc-qqrxzbel \
    --VPCSettings.SubnetId subnet-glx7lnes \
    --CloudResources.0.ComponentName driver \
    --CloudResources.0.PodNumber 1 \
    --CloudResources.0.LimitCpu 8 \
    --CloudResources.0.LimitMemory 32 \
    --CloudResources.0.Service VIRTUALSPARK \
    --CloudResources.0.VolumeDir.VolumeType NEW_PVC \
    --CloudResources.0.Disks.0.DiskType CLOUD_PREMIUM \
    --CloudResources.0.Disks.0.DiskCapacity 50 \
    --CloudResources.0.Disks.0.DiskNumber 1 \
    --CloudResources.1.ComponentName executor \
    --CloudResources.1.PodNumber 15 \
    --CloudResources.1.LimitCpu 8 \
    --CloudResources.1.LimitMemory 32 \
    --CloudResources.1.Service VIRTUALSPARK \
    --CloudResources.1.VolumeDir.VolumeType NEW_PVC \
    --CloudResources.1.Disks.0.DiskType CLOUD_PREMIUM \
    --CloudResources.1.Disks.0.DiskCapacity 50 \
    --CloudResources.1.Disks.0.DiskNumber 1 \
    --SgId sg-ivnxb2xc \
    --LoginSettings.Password 0sw8yq8A@ \
    --ZoneId 900004
```

Output: 
```
{
    "Response": {
        "InstanceId": "emr-mt1cgnyo",
        "RequestId": "d17645a5-957e-4f5e-9b6a-a068d07035c1"
    }
}
```

