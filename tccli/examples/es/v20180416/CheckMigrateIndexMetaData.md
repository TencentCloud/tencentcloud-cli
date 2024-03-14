**Example 1: 检查cos迁移索引元数据**



Input: 

```
tccli es CheckMigrateIndexMetaData --cli-unfold-argument  \
    --CosBucket xxx \
    --BasePath xxx \
    --ServerlessId xxx \
    --Snapshot xxx \
    --ClusterInstanceId xxx \
    --CommonIndexArr xxx \
    --DataStreamArr xxx
```

Output: 
```
{
    "Response": {
        "MappingTimeFieldCheckFailedIndexArr": [
            "xxx"
        ],
        "MappingTimeTypeCheckFailedIndexArr": [
            "xxx"
        ],
        "SettingCheckFailedIndexArr": [
            "xxx"
        ],
        "RequestId": "xxx"
    }
}
```

