**Example 1: 示例**



Input: 

```
tccli tdmq CreateCmqTopic --cli-unfold-argument  \
    --TopicName testtopic
```

Output: 
```
{
    "Response": {
        "RequestId": "ae412902-bb35-4237-955d-3e1f9901e0cc",
        "TopicId": "cmqt-7jwedr3jqb54"
    }
}
```

**Example 2: 创建主题**



Input: 

```
tccli tdmq CreateCmqTopic --cli-unfold-argument  \
    --TopicName ConnTopic
```

Output: 
```
{
    "Response": {
        "TopicId": "topic-gzz05csc",
        "RequestId": "3e0dff9d-9ed5-47c3-beb2-a42c1d69e1cc"
    }
}
```

