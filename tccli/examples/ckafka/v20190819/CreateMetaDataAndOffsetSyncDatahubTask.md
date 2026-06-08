**Example 1: 创建连接器任务-元数据、消息数据、位点同步**



Input: 

```
tccli ckafka CreateMetaDataAndOffsetSyncDatahubTask --cli-unfold-argument  \
    --TaskName MetaDataAndOffsetSyncDatahubTask \
    --SourceResourceId resource-y9n3a2n6 \
    --TargetResourceId resource-y9n33bb6 \
    --Description taskDescription \
    --OffsetType latest \
    --TopicList bbbb14 \
    --Prefix topic1 \
    --Separator .
```

Output: 
```
{
    "Response": {
        "Result": {
            "DatahubId": "mock-data-hub-id",
            "TaskId": "task-y9jb7mq4"
        },
        "RequestId": "57934d4b-bed1-47ee-9b0d-4f913ba29bc3"
    }
}
```

