**Example 1: 批量设置主题属性**

批量设置主题属性

Input: 

```
tccli ckafka BatchModifyTopicAttributes --cli-unfold-argument  \
    --InstanceId ckafka-test \
    --Topic.0.TopicName topic-test \
    --Topic.0.PartitionNum 0 \
    --Topic.0.Note abc \
    --Topic.0.ReplicaNum 0 \
    --Topic.0.CleanUpPolicy policy \
    --Topic.0.MinInsyncReplicas 0 \
    --Topic.0.UncleanLeaderElectionEnable True \
    --Topic.0.RetentionMs 0 \
    --Topic.0.RetentionBytes 0 \
    --Topic.0.SegmentMs 0 \
    --Topic.0.MaxMessageBytes 0
```

Output: 
```
{
    "Response": {
        "Result": [
            {
                "InstanceId": "ckafka-jam3ao99",
                "TopicName": "topic-test",
                "ReturnCode": "20018",
                "Message": "get topic information fail"
            },
            {
                "InstanceId": "ckafka-jam3ao99",
                "TopicName": "topic-test1",
                "ReturnCode": "20018",
                "Message": "get topic information fail"
            }
        ],
        "RequestId": "qwer0001"
    }
}
```

