**Example 1: 新购基础版实例**



Input: 

```
tccli sqlserver CreateBasicDBInstances --cli-unfold-argument  \
    --Zone ap-guangzhou-2 \
    --Cpu 2 \
    --Memory 4 \
    --Storage 500 \
    --MachineType CLOUD_HSSD \
    --VpcId vpc-3xq2t5al \
    --SubnetId subnet-gdy95gfs \
    --InstanceChargeType PREPAID \
    --ProjectId 0 \
    --GoodsNum 1 \
    --DBVersion 2019 \
    --Period 1 \
    --AutoRenewFlag 1 \
    --AutoVoucher 0 \
    --SecurityGroupList sg-6axwo3lz \
    --Weekly 1 2 3 4 5 6 7 \
    --StartTime 03:00 \
    --Span 4 \
    --ResourceTags.0.TagKey env \
    --ResourceTags.0.TagValue prod \
    --TimeZone China Standard Time \
    --Collation Chinese_PRC_CI_AS \
    --DiskEncryptFlag 0 \
    --ThroughputPerformance 100
```

Output: 
```
{
    "Response": {
        "DealName": "20260511A1B2C3",
        "RequestId": "8a4c9f2e-1234-5678-9abc-def012345678"
    }
}
```

