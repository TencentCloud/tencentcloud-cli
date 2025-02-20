**Example 1: 成功**

成功

Input: 

```
tccli trabbit DeleteRabbitMQServerlessQueue --cli-unfold-argument  \
    --InstanceId amqp-slmejnrgtz \
    --VirtualHost vhost1 \
    --QueueName queue1
```

Output: 
```
{
    "Response": {
        "QueueName": "queue1",
        "RequestId": "7df3c05e-80eb-4d92-b6af-760940b4a2ca"
    }
}
```

