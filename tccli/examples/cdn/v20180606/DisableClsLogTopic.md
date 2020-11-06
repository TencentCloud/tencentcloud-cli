**Example 1: 停止日志主题投递**



Input: 

```
tccli cdn DisableClsLogTopic --cli-unfold-argument  \
    --Channel cdn \
    --LogsetId 6d04373b-ba59-4a4f-a96e-9fe53b59a536 \
    --TopicId d2256449-c6ff-421b-93ef-aa3a7dde2de2
```

Output: 
```
{
    "Response": {
        "RequestId": "57460798-8723-45e3-9c75-a0599ef9143a"
    }
}
```

