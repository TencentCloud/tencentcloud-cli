**Example 1: 批量设置主题属性**

批量设置主题属性

Input: 

```
tccli ckafka BatchModifyTopicAttributes --cli-unfold-argument  \
    --InstanceId ckafka-o99zq5mv \
    --Topic.0.TopicName test_leader \
    --Topic.0.RetentionMs 3600000 \
    --Topic.0.SegmentMs 86400000 \
    --Topic.0.MaxMessageBytes 1024 \
    --Topic.0.RetentionBytes 1099511627776 \
    --Topic.0.LogMsgTimestampType None
```

Output: 
```
{
    "Response": {
        "RequestId": "cb00bc01-cda1-40b9-9c39-edad90b802d6",
        "Result": [
            {
                "InstanceId": "ckafka-o99zq5mv",
                "Message": "ok[apply success]",
                "ReturnCode": "0",
                "TopicName": "test_leader"
            }
        ]
    }
}
```

