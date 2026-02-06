**Example 1: 查询实例变配类型示例**



Input: 

```
tccli ckafka DescribeModifyType --cli-unfold-argument  \
    --InstanceId ckafka-6er88krk \
    --BandWidth 320 \
    --DiskSize 1000 \
    --DiskType CLOUD_PREMIUM \
    --Partition 1200 \
    --Topic 120 \
    --Type sp_ckafka_profession
```

Output: 
```
{
    "Response": {
        "Result": {
            "ModifyType": 1,
            "MigrateFlag": true,
            "MigrateCostTime": 17066
        },
        "RequestId": "7118b7f95-43de-4d27-8sdadsa-9999999a"
    }
}
```

