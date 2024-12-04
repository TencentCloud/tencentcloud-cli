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
            "TopicName": "mytopic",
            "TopicId": "topic-test"
        },
        "RequestId": "84770b4b-df34-4ccf-8e22-41d3b1d0fe0d"
    }
}
```

