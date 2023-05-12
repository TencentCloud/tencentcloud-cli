**Example 1: Topic 流量排行**



Input: 

```
tccli ckafka DescribeTopicFlowRanking --cli-unfold-argument  \
    --InstanceId xx \
    --BeginDate 2020-09-22T00:00:00+00:00 \
    --EndDate 2020-09-22T00:00:00+00:00 \
    --RankingType xx
```

Output: 
```
{
    "Response": {
        "Result": {
            "TopicFlow": [
                {
                    "MessageHeap": 1,
                    "TopicId": "xx",
                    "PartitionNum": 1,
                    "TopicTraffic": "xx",
                    "ReplicaNum": 1,
                    "TopicName": "xx"
                },
                {
                    "MessageHeap": 1,
                    "TopicId": "xx",
                    "PartitionNum": 1,
                    "TopicTraffic": "xx",
                    "ReplicaNum": 1,
                    "TopicName": "xx"
                },
                {
                    "MessageHeap": 1,
                    "TopicId": "xx",
                    "PartitionNum": 1,
                    "TopicTraffic": "xx",
                    "ReplicaNum": 1,
                    "TopicName": "xx"
                },
                {
                    "MessageHeap": 1,
                    "TopicId": "xx",
                    "PartitionNum": 1,
                    "TopicTraffic": "xx",
                    "ReplicaNum": 1,
                    "TopicName": "xx"
                },
                {
                    "MessageHeap": 1,
                    "TopicId": "xx",
                    "PartitionNum": 1,
                    "TopicTraffic": "xx",
                    "ReplicaNum": 1,
                    "TopicName": "xx"
                },
                {
                    "MessageHeap": 1,
                    "TopicId": "xx",
                    "PartitionNum": 1,
                    "TopicTraffic": "xx",
                    "ReplicaNum": 1,
                    "TopicName": "xx"
                },
                {
                    "MessageHeap": 1,
                    "TopicId": "xx",
                    "PartitionNum": 1,
                    "TopicTraffic": "xx",
                    "ReplicaNum": 1,
                    "TopicName": "xx"
                },
                {
                    "MessageHeap": 1,
                    "TopicId": "xx",
                    "PartitionNum": 1,
                    "TopicTraffic": "xx",
                    "ReplicaNum": 1,
                    "TopicName": "xx"
                },
                {
                    "MessageHeap": 1,
                    "TopicId": "xx",
                    "PartitionNum": 1,
                    "TopicTraffic": "xx",
                    "ReplicaNum": 1,
                    "TopicName": "xx"
                },
                {
                    "MessageHeap": 1,
                    "TopicId": "xx",
                    "PartitionNum": 1,
                    "TopicTraffic": "xx",
                    "ReplicaNum": 1,
                    "TopicName": "xx"
                }
            ],
            "ConsumeSpeed": [
                {
                    "Speed": 1,
                    "ConsumerGroupName": "xx"
                },
                {
                    "Speed": 1,
                    "ConsumerGroupName": "xx"
                },
                {
                    "Speed": 1,
                    "ConsumerGroupName": "xx"
                },
                {
                    "Speed": 1,
                    "ConsumerGroupName": "xx"
                },
                {
                    "Speed": 1,
                    "ConsumerGroupName": "xx"
                },
                {
                    "Speed": 1,
                    "ConsumerGroupName": "xx"
                },
                {
                    "Speed": 1,
                    "ConsumerGroupName": "xx"
                },
                {
                    "Speed": 1,
                    "ConsumerGroupName": "xx"
                },
                {
                    "Speed": 1,
                    "ConsumerGroupName": "xx"
                }
            ]
        },
        "RequestId": "xx"
    }
}
```

