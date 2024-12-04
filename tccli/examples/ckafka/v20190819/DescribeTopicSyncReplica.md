**Example 1: Topic 未同步详情**



Input: 

```
tccli ckafka DescribeTopicSyncReplica --cli-unfold-argument  \
    --InstanceId ckafka-test \
    --TopicName topic-test \
    --Offset 1 \
    --Limit 0 \
    --OutOfSyncReplicaOnly True
```

Output: 
```
{
    "Response": {
        "RequestId": "3faffeb7-6e6b-4689-8a00-4d5e5f9e9f22",
        "Result": {
            "TopicInSyncReplicaList": [
                {
                    "BeginOffset": 0,
                    "EndOffset": 0,
                    "InSyncReplica": "150032,150033",
                    "Leader": 150032,
                    "MessageCount": 0,
                    "OutOfSyncReplica": "",
                    "Partition": "partition-0",
                    "Replica": "150032,150033"
                },
                {
                    "BeginOffset": 1,
                    "EndOffset": 3,
                    "InSyncReplica": "150033,150034",
                    "Leader": 150033,
                    "MessageCount": 2,
                    "OutOfSyncReplica": "",
                    "Partition": "partition-1",
                    "Replica": "150033,150034"
                },
                {
                    "BeginOffset": 0,
                    "EndOffset": 0,
                    "InSyncReplica": "150034,150035",
                    "Leader": 150034,
                    "MessageCount": 0,
                    "OutOfSyncReplica": "",
                    "Partition": "partition-2",
                    "Replica": "150034,150035"
                },
                {
                    "BeginOffset": 0,
                    "EndOffset": 0,
                    "InSyncReplica": "150035,150032",
                    "Leader": 150035,
                    "MessageCount": 0,
                    "OutOfSyncReplica": "",
                    "Partition": "partition-3",
                    "Replica": "150035,150032"
                },
                {
                    "BeginOffset": 0,
                    "EndOffset": 0,
                    "InSyncReplica": "150032,150033",
                    "Leader": 150032,
                    "MessageCount": 0,
                    "OutOfSyncReplica": "",
                    "Partition": "partition-4",
                    "Replica": "150032,150033"
                },
                {
                    "BeginOffset": 0,
                    "EndOffset": 0,
                    "InSyncReplica": "150033,150034",
                    "Leader": 150033,
                    "MessageCount": 0,
                    "OutOfSyncReplica": "",
                    "Partition": "partition-5",
                    "Replica": "150033,150034"
                },
                {
                    "BeginOffset": 0,
                    "EndOffset": 0,
                    "InSyncReplica": "150034,150035",
                    "Leader": 150034,
                    "MessageCount": 0,
                    "OutOfSyncReplica": "",
                    "Partition": "partition-6",
                    "Replica": "150034,150035"
                },
                {
                    "BeginOffset": 0,
                    "EndOffset": 0,
                    "InSyncReplica": "150035,150032",
                    "Leader": 150035,
                    "MessageCount": 0,
                    "OutOfSyncReplica": "",
                    "Partition": "partition-7",
                    "Replica": "150035,150032"
                },
                {
                    "BeginOffset": 0,
                    "EndOffset": 0,
                    "InSyncReplica": "150032,150033",
                    "Leader": 150032,
                    "MessageCount": 0,
                    "OutOfSyncReplica": "",
                    "Partition": "partition-8",
                    "Replica": "150032,150033"
                },
                {
                    "BeginOffset": 0,
                    "EndOffset": 0,
                    "InSyncReplica": "150033,150034",
                    "Leader": 150033,
                    "MessageCount": 0,
                    "OutOfSyncReplica": "",
                    "Partition": "partition-9",
                    "Replica": "150033,150034"
                }
            ],
            "TotalCount": 10
        }
    }
}
```

