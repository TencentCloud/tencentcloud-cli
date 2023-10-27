**Example 1: 查询RabbitMQ队列列表**

查询当前 vhost 下所有 queue

Input: 

```
tccli tdmq DescribeRabbitMQQueues --cli-unfold-argument  \
    --InstanceId amqp-44w9928j \
    --VirtualHost test
```

Output: 
```
{
    "Response": {
        "RequestId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "QueueInfoList": [
            {
                "QueueName": "queue.name",
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

