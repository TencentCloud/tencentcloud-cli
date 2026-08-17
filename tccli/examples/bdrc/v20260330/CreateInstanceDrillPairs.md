**Example 1: 创建演练**



Input: 

```
tccli bdrc CreateInstanceDrillPairs --cli-unfold-argument  \
    --ProtectGroupId pg-cepq4abv \
    --DrillPairGroupVpc vpc-3pwbhict \
    --DrillPairGroupName my drill test2 \
    --CreateTargetInstanceParameters.0.SourceInstanceId ins-f8upbkwy \
    --CreateTargetInstanceParameters.0.InstanceChargeType POSTPAID_BY_HOUR \
    --CreateTargetInstanceParameters.0.Placement.Zone ap-guangzhou-3 \
    --CreateTargetInstanceParameters.0.ImageId img-l8og963d \
    --CreateTargetInstanceParameters.0.SystemDisk.DiskType CLOUD_PREMIUM \
    --CreateTargetInstanceParameters.0.SystemDisk.DiskSize 50 \
    --CreateTargetInstanceParameters.0.InstanceType S2.MEDIUM2 \
    --CreateTargetInstanceParameters.0.VirtualPrivateCloud.VpcId vpc-3pwbhict \
    --CreateTargetInstanceParameters.0.VirtualPrivateCloud.SubnetId subnet-lreo8zy4 \
    --CreateTargetInstanceParameters.0.CopyPairId cvmcopypair-gd8gq26l \
    --CreateTargetInstanceParameters.0.RecoveryTime 2026-06-05 17:50:06
```

Output: 
```
{
    "Response": {
        "DrillPairIds": [
            "drillpair-f93za7wl"
        ],
        "RequestId": "121b01bd-33a0-4e26-86bf-3159968e49e1"
    }
}
```

