**Example 1: 创建连接器-元数据、消息同步任务**



Input: 

```
tccli ckafka CreateMetaAndDataSyncDatahubTask --cli-unfold-argument  \
    --TaskName CreateMetaAndDataSyncDatahubTask \
    --SourceResourceId resource-y9n3a2n6 \
    --TargetResourceId resource-y9n33bb6 \
    --OffsetType latest \
    --TopicList bbbb14 \
    --Prefix topic1 \
    --Separator . \
    --Description task1
```

Output: 
```
{
    "Response": {
        "Result": {
            "DatahubId": "mock-data-hub-id",
            "TaskId": "task-y9jb79mn"
        },
        "RequestId": "d928539a-f1c8-45c6-ba2c-0bcecfa6e431"
    }
}
```

