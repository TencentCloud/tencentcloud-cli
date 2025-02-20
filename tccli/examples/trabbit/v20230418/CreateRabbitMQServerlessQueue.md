**Example 1: 创建RabbitMQ队列**

创建RabbitMQ队列

Input: 

```
tccli trabbit CreateRabbitMQServerlessQueue --cli-unfold-argument  \
    --InstanceId amqp-slmejnrgtz \
    --VirtualHost vhost1 \
    --QueueName queue1 \
    --QueueType vhost1 \
    --Remark 测试队列
```

Output: 
```
{
    "Response": {
        "QueueName": "queue1",
        "RequestId": "941a7f2b-26f7-413f-b91f-341678cd00f6"
    }
}
```

