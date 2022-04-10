**Example 1: 获取Amqp队列列表**



Input: 

```
tccli tdmq DescribeAMQPQueues --cli-unfold-argument  \
    --VHostId test \
    --ClusterId amqp-dsadasd \
    --Limit 1 \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "Queues": [
            {
                "Remark": "xx",
                "Name": "test",
                "AutoDelete": true,
                "DestBindedNum": 1,
                "UpdateTime": 1,
                "DeadLetterExchange": "xx",
                "Tps": 1,
                "TopicName": "xx",
                "DeadLetterRoutingKey": "xx",
                "OnlineConsumerNum": 1,
                "CreateTime": 156851400000,
                "AccumulativeMsgNum": 1
            }
        ],
        "RequestId": "0604a303-6d5f-40e6-9dfe-6c4ddd8fe2df"
    }
}
```

