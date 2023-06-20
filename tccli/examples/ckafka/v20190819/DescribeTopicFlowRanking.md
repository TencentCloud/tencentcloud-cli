**Example 1: Topic 流量排行**

检查当前实例的主题流量top 情况

Input: 

```
tccli ckafka DescribeTopicFlowRanking --cli-unfold-argument  \
    --InstanceId ckafka-3inxiic \
    --BeginDate 2020-09-22T00:00:00+00:00 \
    --EndDate 2020-09-22T00:00:00+00:00 \
    --RankingType PRO
```

Output: 
```
{
    "Response": {
        "Result": {
            "TopicFlow": [
                {
                    "TopicId": "abc",
                    "TopicName": "abc",
                    "PartitionNum": 1,
                    "ReplicaNum": 1,
                    "TopicTraffic": "abc",
                    "MessageHeap": 1
                }
            ],
            "ConsumeSpeed": [
                {
                    "ConsumerGroupName": "abc",
                    "Speed": 1
                }
            ],
            "TopicMessageHeap": [
                {
                    "TopicId": "abc",
                    "TopicName": "abc",
                    "PartitionNum": 1,
                    "ReplicaNum": 1,
                    "TopicTraffic": "abc",
                    "MessageHeap": 1
                }
            ],
            "BrokerIp": [
                "abc"
            ],
            "BrokerTopicData": [
                {
                    "TopicName": "abc",
                    "TopicId": "abc",
                    "DataSize": 1
                }
            ]
        },
        "RequestId": "abc"
    }
}
```

