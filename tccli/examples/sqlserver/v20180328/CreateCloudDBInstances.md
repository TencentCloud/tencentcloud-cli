**Example 1: 创建实例**

创建基于通用型云盘版的双机高可用实例。

Input: 

```
tccli sqlserver CreateCloudDBInstances --cli-unfold-argument  \
    --Zone ap-guangzhou-3 \
    --InstanceChargeType PREPAID \
    --ProjectId 0 \
    --Memory 4 \
    --Storage 200 \
    --GoodsNum 1 \
    --SubnetId subnet-15y3y4eo \
    --VpcId vpc-hqxhp43z \
    --Period 1 \
    --DBVersion 2008R2 \
    --AutoRenewFlag 0 \
    --SecurityGroupList sg-7hb0hisl \
    --Weekly 1 2 \
    --StartTime 01:00 \
    --Span 1 \
    --MultiZones True \
    --ResourceTags.0.TagKey env \
    --ResourceTags.0.TagValue product \
    --Cpu 2 \
    --MachineType CLOUD_BSSD \
    --Collation Chinese_PRC_CI_AS \
    --TimeZone China Standard Time
```

Output: 
```
{
    "Response": {
        "DealName": "202301231",
        "RequestId": "61999983-b0af-4889-b067-xxxxxxxxx"
    }
}
```

