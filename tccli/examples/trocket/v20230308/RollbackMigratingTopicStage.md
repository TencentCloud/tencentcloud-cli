**Example 1: 回滚迁移主题的切流状态**



Input: 

```
tccli trocket RollbackMigratingTopicStage --cli-unfold-argument  \
    --TaskId taskId \
    --TopicName TopicTest \
    --Namespace 
```

Output: 
```
{
    "Response": {
        "RequestId": "abc"
    }
}
```

