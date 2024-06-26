**Example 1: 创建主题**



Input: 

```
tccli ckafka CreateDatahubTopic --cli-unfold-argument  \
    --Name 12345-test \
    --PartitionNum 1 \
    --RetentionMs 3600000
```

Output: 
```
{
    "Response": {
        "Result": {
            "TopicName": "abc",
            "TopicId": "abc"
        },
        "RequestId": "abc"
    }
}
```

