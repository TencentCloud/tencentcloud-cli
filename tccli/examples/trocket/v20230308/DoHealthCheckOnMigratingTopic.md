**Example 1: 迁移主题安全检查**



Input: 

```
tccli trocket DoHealthCheckOnMigratingTopic --cli-unfold-argument  \
    --TaskId 02f6c31a-9707-4244-8dd3-35ad868ef92a \
    --TopicName Test \
    --IgnoreCheck True \
    --Namespace 
```

Output: 
```
{
    "Response": {
        "Passed": true,
        "Reason": "",
        "RequestId": "02f6c31a-9707-4244-8dd3-35ad868ef92a"
    }
}
```

