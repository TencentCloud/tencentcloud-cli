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
            "TopicId": "abc",
            "CreateTime": 0,
            "Note": "abc",
            "PartitionNum": 0,
            "EnableWhiteList": 0,
            "IpWhiteList": [
                "abc"
            ],
            "Config": {
                "Retention": 0,
                "MinInsyncReplicas": 0,
                "CleanUpPolicy": "abc",
                "SegmentMs": 0,
                "UncleanLeaderElectionEnable": 0,
                "SegmentBytes": 0,
                "MaxMessageBytes": 0,
                "RetentionBytes": 0
            },
            "Partitions": [
                {
                    "Partition": 0,
                    "LeaderStatus": 0,
                    "IsrNum": 0,
                    "ReplicaNum": 0
                }
            ],
            "EnableAclRule": 0,
            "AclRuleList": [
                {
                    "RuleName": "abc",
                    "InstanceId": "abc",
                    "PatternType": "abc",
                    "Pattern": "abc",
                    "ResourceType": "abc",
                    "AclList": "abc",
                    "CreateTimeStamp": "abc",
                    "IsApplied": 0,
                    "UpdateTimeStamp": "abc",
                    "Comment": "abc",
                    "TopicName": "abc",
                    "TopicCount": 0,
                    "PatternTypeTitle": "abc"
                }
            ],
            "QuotaConfig": {
                "QuotaProducerByteRate": 0,
                "QuotaConsumerByteRate": 0
            },
            "ReplicaNum": 0
        },
        "RequestId": "abc"
    }
}
```

