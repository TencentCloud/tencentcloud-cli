**Example 1: 修改RabbitMQ队列**



Input: 

```
tccli trabbit ModifyRabbitMQServerlessQueue --cli-unfold-argument  \
    --InstanceId amqp-44w9928j \
    --VirtualHost testVhost \
    --QueueName testQueueName \
    --Remark newRemark
```

Output: 
```
{
    "Response": {
        "RequestId": "vcbdasdasdsadsa",
        "QueueName": "cc"
    }
}
```

