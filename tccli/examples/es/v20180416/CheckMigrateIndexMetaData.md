**Example 1: 检查cos迁移索引元数据**



Input: 

```
tccli es CheckMigrateIndexMetaData --cli-unfold-argument  \
    --CosBucket user-cos \
    --BasePath dir/ \
    --ServerlessId index-feafagg \
    --Snapshot snapshot \
    --ClusterInstanceId es-feafegg \
    --CommonIndexArr index \
    --DataStreamArr index
```

Output: 
```
{
    "Response": {
        "MappingTimeFieldCheckFailedIndexArr": [
            "index"
        ],
        "MappingTimeTypeCheckFailedIndexArr": [
            "index"
        ],
        "SettingCheckFailedIndexArr": [
            "index"
        ],
        "RequestId": "40f4f780-9969-42f9-8bd9-ccf0d1f2591a"
    }
}
```

