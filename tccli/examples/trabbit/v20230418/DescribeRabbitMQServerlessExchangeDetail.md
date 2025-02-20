**Example 1: 查看Exchange详细信息**



Input: 

```
tccli trabbit DescribeRabbitMQServerlessExchangeDetail --cli-unfold-argument  \
    --InstanceId amqp-slfxemauoa \
    --VirtualHost test_vhost3213 \
    --ExchangeName test_exchange
```

Output: 
```
{
    "Response": {
        "RequestId": "e4d30e41-d8c5-4651-81f6-ee286c909030",
        "ExchangeName": "test_exchange",
        "Remark": "",
        "Durable": false,
        "AutoDelete": false,
        "Internal": false,
        "AlternateExchange": "",
        "ExchangeType": "direct",
        "VirtualHost": "test_vhost3213",
        "ExchangeCreator": "user",
        "Arguments": ""
    }
}
```

