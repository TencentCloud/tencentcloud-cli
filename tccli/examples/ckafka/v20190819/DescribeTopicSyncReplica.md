**Example 1: Topic 未同步详情**



Input: 

```
tccli ckafka DescribeTopicSyncReplica --cli-unfold-argument  \
    --InstanceId abc \
    --TopicName abc \
    --Offset 1 \
    --Limit 0 \
    --OutOfSyncReplicaOnly True
```

Output: 
```
{
    "Response": {
        "Result": {
            "TopicInSyncReplicaList": [
                {
                    "Partition": "abc",
                    "Leader": 1,
                    "Replica": "abc",
                    "InSyncReplica": "abc",
                    "BeginOffset": 1,
                    "EndOffset": 1,
                    "MessageCount": 1,
                    "OutOfSyncReplica": "abc"
                }
            ],
            "TotalCount": 1
        },
        "RequestId": "abc"
    }
}
```

