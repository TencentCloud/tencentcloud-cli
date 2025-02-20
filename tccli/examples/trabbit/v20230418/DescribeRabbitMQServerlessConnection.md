**Example 1: 查询RabbitMQ连接列表**



Input: 

```
tccli trabbit DescribeRabbitMQServerlessConnection --cli-unfold-argument  \
    --InstanceId amqp-44w9928j \
    --VirtualHost testVhost
```

Output: 
```
{
    "Response": {
        "RequestId": "dsfsdfs",
        "Connections": [],
        "TotalCount": 0
    }
}
```

