**Example 1: 创建主题**



Input: 

```
tccli ckafka CreateTopic --cli-unfold-argument  \
    --InstanceId xxx \
    --TopicName xxx \
    --PartitionNum 1 \
    --ReplicaNum 2
```

Output: 
```
{
    "Response": {
        "Result": {
            "TopicId": "topic-k766ruye"
        },
        "RequestId": "1305a410-b030-476d-acdf-eba0dfd5323b"
    }
}
```

