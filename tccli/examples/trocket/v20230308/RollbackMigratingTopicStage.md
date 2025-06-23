**Example 1: 回滚迁移主题的切流状态**



Input: 

```
tccli trocket RollbackMigratingTopicStage --cli-unfold-argument  \
    --TaskId 02f6c31a-9707-4244-8dd3-35ad868ef92a \
    --TopicName TopicTest \
    --Namespace 
```

Output: 
```
{
    "Error": null,
    "RequestId": null,
    "Response": {
        "RequestId": "02f6c31a-9707-4244-8dd3-35ad868ef92a"
    }
}
```

