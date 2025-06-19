**Example 1: 查询RabbitMQ队列列表**

查询当前 vhost 下所有 queue

Input: 

```
tccli tdmq DescribeRabbitMQQueues --cli-unfold-argument  \
    --InstanceId amqp-2ppxx4rq \
    --VirtualHost testVhost
```

Output: 
```
{
    "Response": {
        "RequestId": "a8f28d5e-a7e2-4b0b-afa0-2fba09c077a0",
        "QueueInfoList": [
            {
                "QueueName": "prod.queue",
                "Remark": null,
                "QueueType": "classic",
                "ConsumerDetail": {
                    "ConsumersNumber": 1
                },
                "MessageHeapCount": 0,
                "MessageRateIn": 0,
                "MessageRateOut": 0
            }
        ],
        "TotalCount": 1
    }
}
```

