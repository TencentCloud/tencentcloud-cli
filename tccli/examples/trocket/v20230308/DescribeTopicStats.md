**Example 1: 查询主题队列消费详情**

查询主题队列消费详情

Input: 

```
tccli trocket DescribeTopicStats --cli-unfold-argument  \
    --Topic topic-976839 \
    --InstanceId rmq-16o4n24npr \
    --GroupId group-2026-05-28-405103 \
    --Offset 0 \
    --Limit 10
```

Output: 
```
{
    "Response": {
        "Data": [
            {
                "BrokerName": "rmqbroker-cd-16o4n24npr-0",
                "BrokerOffset": 1,
                "CommitOffset": 1,
                "LastUpdateTimestamp": 1779948561234,
                "MessageCount": 0,
                "QueueId": 0
            }
        ],
        "TotalCount": 18,
        "RequestId": "383962ae-e1d9-4e25-8117-a9556ccecf07"
    }
}
```

