**Example 1: 创建连接器-元数据同步任务**



Input: 

```
tccli ckafka CreateMetaSyncDatahubTask --cli-unfold-argument  \
    --TaskName CreateMetaSyncDatahubTask \
    --SourceResourceId resource-y9n9pr46 \
    --TargetResourceId resource-y9n947b6 \
    --Tags.0.TagKey 创建人 \
    --Tags.0.TagValue 王蕊
```

Output: 
```
{
    "Response": {
        "Result": {
            "DatahubId": "mock-data-hub-id",
            "TaskId": "task-y9jb22m4"
        },
        "RequestId": "91eb38c2-9487-489e-9562-25a32d4fb8e7"
    }
}
```

