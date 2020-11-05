**Example 1: Creating a log topic**



Input: 

```
tccli cdn CreateClsLogTopic --cli-unfold-argument  \
    --Channel cdn\
    --TopicName test\
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

