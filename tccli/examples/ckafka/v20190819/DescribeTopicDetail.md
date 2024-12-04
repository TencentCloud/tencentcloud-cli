**Example 1: 获取实例列表详情**



Input: 

```
tccli ckafka DescribeTopicDetail --cli-unfold-argument  \
    --InstanceId ckafka-xxooa0
```

Output: 
```
{
    "Response": {
        "RequestId": "071db315-27d5-4a7c-8bb3-e05c23e7a69c",
        "Result": {
            "TopicList": [
                {
                    "Config": {
                        "CleanUpPolicy": "delete",
                        "LogMsgTimestampType": null,
                        "MaxMessageBytes": 8388608,
                        "MinInsyncReplicas": 1,
                        "Retention": 259200000,
                        "RetentionBytes": null,
                        "SegmentBytes": null,
                        "SegmentMs": null,
                        "UncleanLeaderElectionEnable": 1
                    },
                    "CreateTime": 1716452124,
                    "EnableWhiteList": false,
                    "ForwardCosBucket": "",
                    "ForwardInterval": 0,
                    "ForwardStatus": 1,
                    "IpWhiteListCount": 0,
                    "Note": "",
                    "PartitionNum": 10,
                    "ReplicaNum": 2,
                    "RetentionTimeConfig": {
                        "Current": 4320,
                        "Expect": 4320,
                        "ModTimeStamp": 1716452125000
                    },
                    "Status": 0,
                    "Tags": null,
                    "TopicId": "topic-4mi2t5w2",
                    "TopicName": "abc"
                },
                {
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
                    "EnableWhiteList": false,
                    "ForwardCosBucket": "",
                    "ForwardInterval": 0,
                    "ForwardStatus": 1,
                    "IpWhiteListCount": 0,
                    "Note": "",
                    "PartitionNum": 1,
                    "ReplicaNum": 2,
                    "RetentionTimeConfig": {
                        "Current": 1440,
                        "Expect": 1440,
                        "ModTimeStamp": 1720525149000
                    },
                    "Status": 0,
                    "Tags": null,
                    "TopicId": "topic-24gugwns",
                    "TopicName": "test-shilinlu"
                }
            ],
            "TotalCount": 2
        }
    }
}
```

