**Example 1: Topic 未同步详情**



Input: 

```
tccli ckafka DescribeTopicSyncReplica --cli-unfold-argument  \
    --InstanceId xx \
    --TopicName xxx \
    --Offset 0 \
    --Limit 10 \
    --OutOfSyncReplicaOnly True
```

Output: 
```
{
    "Response": {
        "Result": {
            "TotalCount": 1,
            "TopicInSyncReplicaList": [
                {
                    "Partition": "xxxx",
                    "Leader": 1,
                    "Replica": "110,3551,2315",
                    "InSyncReplica": "100,5526",
                    "BeginOffset": 10,
                    "EndOffset": 10,
                    "MessageCount": 1,
                    "OutOfSyncReplica": "120,51"
                }
            ]
        },
        "RequestId": "xx"
    }
}
```

