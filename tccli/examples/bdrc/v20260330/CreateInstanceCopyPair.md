**Example 1: 创建cvm复制对**



Input: 

```
tccli bdrc CreateInstanceCopyPair --cli-unfold-argument  \
    --ProtectGroupId pg-awh08zgp \
    --CreateTargetInstanceParameters.0.SourceInstanceId ins-103kuwr2 \
    --CreateTargetInstanceParameters.0.InstanceChargeType POSTPAID_BY_HOUR \
    --CreateTargetInstanceParameters.0.Placement.Zone ap-guangzhou-3 \
    --CreateTargetInstanceParameters.0.ImageId img-l8og963d \
    --CreateTargetInstanceParameters.0.SystemDisk.DiskType CLOUD_PREMIUM \
    --CreateTargetInstanceParameters.0.SystemDisk.DiskSize 50 \
    --CreateTargetInstanceParameters.0.InstanceType S2.MEDIUM2 \
    --CreateTargetInstanceParameters.0.VirtualPrivateCloud.VpcId vpc-ap4fkwyt \
    --CreateTargetInstanceParameters.0.VirtualPrivateCloud.SubnetId subnet-kw0s0e5u \
    --CreateTargetInstanceParameters.0.LoginSettings.Password Tencent@123 \
    --InstanceCopyPairName CopyPair1 \
    --RecoveryPointObjective 15
```

Output: 
```
{
    "Response": {
        "CopyPairIds": [
            "cvmcopypair-9wfdmidr"
        ],
        "RequestId": "b0afa241-f75b-4048-9230-e0c82f9f4d25"
    }
}
```

