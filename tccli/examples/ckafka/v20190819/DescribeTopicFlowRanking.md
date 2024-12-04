**Example 1: Topic 流量排行**

检查当前实例的主题流量top 情况

Input: 

```
tccli ckafka DescribeTopicFlowRanking --cli-unfold-argument  \
    --InstanceId ckafka-vv7wpp93 \
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
                    "TopicName": "test-bing-v1w",
                    "TopicId": "topic-1jcib81g",
                    "PartitionNum": 10,
                    "ReplicaNum": 2,
                    "TopicTraffic": "0.00",
                    "MessageHeap": 3135
                },
                {
                    "TopicName": "alert-go-s1",
                    "TopicId": "topic-o8gy2gta",
                    "PartitionNum": 3,
                    "ReplicaNum": 2,
                    "TopicTraffic": "0.00",
                    "MessageHeap": 0
                },
                {
                    "TopicName": "alter-go-s2",
                    "TopicId": "topic-d6t7j7vc",
                    "PartitionNum": 10,
                    "ReplicaNum": 2,
                    "TopicTraffic": "0.00",
                    "MessageHeap": 0
                }
            ],
            "TopicMessageHeap": [
                {
                    "TopicName": "test-bing-v1w",
                    "TopicId": "topic-1jcib81g",
                    "PartitionNum": 10,
                    "ReplicaNum": 2,
                    "TopicTraffic": "0.00",
                    "MessageHeap": 3135
                },
                {
                    "TopicName": "alert-go-s1",
                    "TopicId": "topic-o8gy2gta",
                    "PartitionNum": 3,
                    "ReplicaNum": 2,
                    "TopicTraffic": "0.00",
                    "MessageHeap": 0
                },
                {
                    "TopicName": "alter-go-s2",
                    "TopicId": "topic-d6t7j7vc",
                    "PartitionNum": 10,
                    "ReplicaNum": 2,
                    "TopicTraffic": "0.00",
                    "MessageHeap": 0
                }
            ],
            "ConsumeSpeed": [],
            "BrokerIp": [
                "10.0.156.208",
                "10.0.207.248",
                "10.0.207.249",
                "10.0.156.205"
            ],
            "BrokerTopicData": [],
            "BrokerTopicFlowData": []
        },
        "RequestId": "6c6d04b5-fa2f-4b4c-913a-2bd4ee111aa4"
    }
}
```

