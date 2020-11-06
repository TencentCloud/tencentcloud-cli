**Example 1: 创建日志主题**



Input: 

```
tccli cdn CreateClsLogTopic --cli-unfold-argument  \
    --Channel cdn \
    --TopicName test \
    --LogsetId 57460798-8723-45e3-9c75-a0599ef9143a
```

Output: 
```
{
    "Response": {
        "RequestId": "57460798-8723-45e3-9c75-a0599ef9143a",
        "TopicId": "123-456-789"
    }
}
```

