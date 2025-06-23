**Example 1: 将主题移出迁移任务**



Input: 

```
tccli trocket RemoveMigratingTopic --cli-unfold-argument  \
    --TaskId 02f6c31a-9707-4244-8dd3-35ad868ef92a \
    --Namespace  \
    --TopicName topic-a
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

