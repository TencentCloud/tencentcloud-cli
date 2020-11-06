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
            "CreateTime": "1970-01-19 09:47:17",
            "Note": "",
            "PartitionNum": 3,
            "EnableWhiteList": 0,
            "IpWhiteList": [],
            "Config": {
                "Retention": 300000000
            },
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

