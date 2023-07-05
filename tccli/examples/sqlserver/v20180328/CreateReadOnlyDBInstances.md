**Example 1: 创建只读实例**

创建只读实例

Input: 

```
tccli sqlserver CreateReadOnlyDBInstances --cli-unfold-argument  \
    --ReadOnlyGroupMaxDelayTime 10 \
    --VpcId vpc-3xq2t5al \
    --GoodsNum 1 \
    --Zone ap-guangzhou-2 \
    --InstanceId mssql-6upluvd5 \
    --Period 1 \
    --Storage 10 \
    --ReadOnlyGroupIsOfflineDelay 1 \
    --ReadOnlyGroupMinInGroup 1 \
    --ReadOnlyGroupName default_name \
    --Collation Chinese_PRC_CI_AS \
    --ReadOnlyGroupType 2 \
    --InstanceChargeType POSTPAID \
    --Memory 2 \
    --SubnetId subnet-gdy95gfs \
    --TimeZone China Standard Time \
    --ReadOnlyGroupForcedUpgrade 1
```

Output: 
```
{
    "Response": {
        "DealNames": [
            "20200722117963"
        ],
        "RequestId": "0509b6b8-8906-479f-9489-10620ec6d4ce"
    }
}
```

