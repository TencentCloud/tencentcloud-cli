**Example 1: 迁移主题安全检查**



Input: 

```
tccli trocket DoHealthCheckOnMigratingTopic --cli-unfold-argument  \
    --TaskId abc \
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
        "RequestId": "abc"
    }
}
```

