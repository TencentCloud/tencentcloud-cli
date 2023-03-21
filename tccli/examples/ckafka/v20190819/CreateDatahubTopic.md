**Example 1: 创建主题**



Input: 

```
tccli ckafka CreateDatahubTopic --cli-unfold-argument  \
    --Name xxx \
    --PartitionNum 1 \
    --RetentionMs 3600000
```

Output: 
```
{
    "Response": {
        "Result": {
            "TopicName": "xx"
        },
        "RequestId": "xx"
    }
}
```

