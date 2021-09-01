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
                    "TopicName": "test",
                    "TopicId": "inter-topic-d7a2f7fq",
                    "PartitionNum": 3,
                    "ReplicaNum": 2,
                    "Note": "",
                    "CreateTime": 1561637447,
                    "EnableWhiteList": false,
                    "IpWhiteListCount": 0,
                    "ForwardCosBucket": "",
                    "ForwardStatus": 1,
                    "ForwardInterval": 0,
                    "Config": {
                        "Retention": 300000000
                    },
                    "RetentionTimeConfig": {
                        "Expect": 1440,
                        "Current": 480,
                        "ModTimeStamp": 1561637447
                    }
                }
            ],
            "TotalCount": 12
        },
        "RequestId": "98fdae03-9bc2-4c2e-b429-0a96cca7144b"
    }
}
```

