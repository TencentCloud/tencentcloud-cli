**Example 1: 创建物理机双节点**



Input: 

```
tccli sqlserver CreateDBInstances --cli-unfold-argument  \
    --Zone ap-guangzhou-2 \
    --Memory 4 \
    --Storage 100 \
    --InstanceChargeType PREPAID \
    --ProjectId 0 \
    --GoodsNum 1 \
    --DBVersion 2019 \
    --SubnetId subnet-gdy95gfs \
    --VpcId vpc-3xq2t5al \
    --Period 1 \
    --AutoRenewFlag 1 \
    --AutoVoucher 0 \
    --SecurityGroupList sg-6axwo3lz \
    --Weekly 1 2 3 4 5 6 7 \
    --StartTime 03:00 \
    --Span 4 \
    --MultiZones False \
    --ResourceTags.0.TagKey env \
    --ResourceTags.0.TagValue prod \
    --TimeZone China Standard Time \
    --Collation Chinese_PRC_CI_AS \
    --MultiNodes False \
    --AvailabilityStrategy Sync
```

Output: 
```
{
    "Response": {
        "DealNames": [
            "20260511A1B2C3"
        ],
        "DealName": "20260511A1B2C3",
        "RequestId": "8a4c9f2e-1234-5678-9abc-def012345678"
    }
}
```

