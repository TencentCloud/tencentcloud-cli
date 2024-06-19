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
        "Result": {
            "TopicList": [
                {
                    "TopicName": "abc",
                    "TopicId": "abc",
                    "PartitionNum": 0,
                    "ReplicaNum": 0,
                    "Note": "abc",
                    "CreateTime": 0,
                    "EnableWhiteList": true,
                    "IpWhiteListCount": 0,
                    "ForwardCosBucket": "abc",
                    "ForwardStatus": 0,
                    "ForwardInterval": 0,
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
                    "RetentionTimeConfig": {
                        "Expect": 0,
                        "Current": 0,
                        "ModTimeStamp": 0
                    },
                    "Status": 0,
                    "Tags": [
                        {
                            "TagKey": "abc",
                            "TagValue": "abc"
                        }
                    ]
                }
            ],
            "TotalCount": 0
        },
        "RequestId": "abc"
    }
}
```

