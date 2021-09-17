**Example 1: 获取主题属性**



Input: 

```
tccli ckafka DescribeTopicAttributes --cli-unfold-argument  \
    --InstanceId xxx \
    --TopicName xxx
```

Output: 
```
{
    "Response": {
        "Result": {
            "TopicId": "inter-topic-d7a2f7fq",
            "CreateTime": 111,
            "Note": "",
            "PartitionNum": 3,
            "EnableWhiteList": 0,
            "EnableAclRule": 0,
            "IpWhiteList": [],
            "Config": {
                "UncleanLeaderElectionEnable": 0,
                "MinInsyncReplicas": 0,
                "SegmentMs": 0,
                "CleanUpPolicy": "xx",
                "SegmentBytes": 0,
                "MaxMessageBytes": 0,
                "Retention": 300000000
            },
            "AclRuleList": [
                {
                    "Comment": "xx",
                    "PatternType": "xx",
                    "UpdateTimeStamp": "xx",
                    "InstanceId": "xx",
                    "Pattern": "xx",
                    "ResourceType": "xx",
                    "AclList": "xx",
                    "IsApplied": 0,
                    "RuleName": "xx",
                    "TopicCount": 0,
                    "CreateTimeStamp": "xx",
                    "TopicName": "xx"
                }
            ],
            "Partitions": [
                {
                    "Partition": 0,
                    "LeaderStatus": 0,
                    "IsrNum": 2,
                    "ReplicaNum": 2
                },
                {
                    "Partition": 1,
                    "LeaderStatus": 0,
                    "IsrNum": 2,
                    "ReplicaNum": 2
                },
                {
                    "Partition": 2,
                    "LeaderStatus": 0,
                    "IsrNum": 2,
                    "ReplicaNum": 2
                }
            ]
        },
        "RequestId": "b660ef69-993b-4760-a599-995cadb56bbe"
    }
}
```

