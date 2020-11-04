**Example 1: 创建只读实例**



Input: 

```
tccli sqlserver CreateReadOnlyDBInstances --cli-unfold-argument  \
    --InstanceId mssql-6upluvd5\
    --Zone ap-guangzhou-2\
    --ReadOnlyGroupType 2\
    --ReadOnlyGroupForcedUpgrade 1\
    --ReadOnlyGroupName default_name\
    --ReadOnlyGroupIsOfflineDelay 1\
    --ReadOnlyGroupMaxDelayTime 10\
    --ReadOnlyGroupMinInGroup 1\
    --InstanceChargeType POSTPAID\
    --Memory 2\
    --Storage 10\
    --GoodsNum 1\
    --SubnetId subnet-gdy95gfs\
    --VpcId vpc-3xq2t5al\
    --Period 1
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

