**Example 1: 获取主题属性**



Input: 

```
tccli ckafka DescribeTopicAttributes --cli-unfold-argument  \
    --InstanceId ckafka-na37x9qa \
    --TopicName test-sh
```

Output: 
```
{
    "Response": {
        "RequestId": "2631ff19-2dd4-41a6-9391-c7543dc22c8a",
        "Result": {
            "AclRuleList": [],
            "Config": {
                "CleanUpPolicy": "delete",
                "LogMsgTimestampType": null,
                "MaxMessageBytes": 8388608,
                "MinInsyncReplicas": 1,
                "Retention": 86400000,
                "RetentionBytes": null,
                "SegmentBytes": null,
                "SegmentMs": null,
                "UncleanLeaderElectionEnable": 1
            },
            "CreateTime": 1720525148,
            "EnableAclRule": 0,
            "EnableWhiteList": 0,
            "IpWhiteList": [],
            "Note": "",
            "PartitionNum": 1,
            "Partitions": [
                {
                    "IsrNum": 2,
                    "LeaderStatus": 0,
                    "Partition": 0,
                    "ReplicaNum": 2
                }
            ],
            "QuotaConfig": {
                "QuotaConsumerByteRate": null,
                "QuotaProducerByteRate": null
            },
            "ReplicaNum": 2,
            "TopicId": "topic-24gugwns"
        }
    }
}
```

