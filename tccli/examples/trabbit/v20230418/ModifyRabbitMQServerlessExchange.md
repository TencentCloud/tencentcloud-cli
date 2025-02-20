**Example 1: 修改RabbitMQ exchange**



Input: 

```
tccli trabbit ModifyRabbitMQServerlessExchange --cli-unfold-argument  \
    --InstanceId amqp-44w9928j \
    --VirtualHost testVhost \
    --ExchangeName testExchange \
    --Remark newRemark
```

Output: 
```
{
    "Response": {
        "RequestId": "request1",
        "ExchangeName": "testExchange"
    }
}
```

