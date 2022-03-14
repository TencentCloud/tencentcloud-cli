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
            "TopicId": "xx",
            "PartitionNum": 3,
            "AclRuleList": [
                {
                    "Comment": "xx",
                    "PatternType": "xx",
                    "UpdateTimeStamp": "xx",
                    "InstanceId": "xx",
                    "Pattern": "xx",
                    "ResourceType": "xx",
                    "AclList": "xx",
                    "PatternTypeTitle": "xx",
                    "IsApplied": 0,
                    "RuleName": "xx",
                    "TopicCount": 0,
                    "CreateTimeStamp": "xx",
                    "TopicName": "xx"
                }
            ],
            "Note": "xx",
            "IpWhiteList": [
                "xx"
            ],
            "EnableAclRule": 0,
            "QuotaConfig": {
                "QuotaConsumerByteRate": 0,
                "QuotaProducerByteRate": 0
            },
            "Partitions": [
                {
                    "Partition": 0,
                    "IsrNum": 2,
                    "LeaderStatus": 0,
                    "ReplicaNum": 2
                },
                {
                    "Partition": 1,
                    "IsrNum": 2,
                    "LeaderStatus": 0,
                    "ReplicaNum": 2
                },
                {
                    "Partition": 2,
                    "IsrNum": 2,
                    "LeaderStatus": 0,
                    "ReplicaNum": 2
                }
            ],
            "Config": {
                "UncleanLeaderElectionEnable": 0,
                "MinInsyncReplicas": 0,
                "SegmentMs": 0,
                "CleanUpPolicy": "xx",
                "SegmentBytes": 0,
                "RetentionBytes": 0,
                "MaxMessageBytes": 0,
                "Retention": 300000000
            },
            "CreateTime": 111,
            "EnableWhiteList": 0
        },
        "RequestId": "xx"
    }
}
```

