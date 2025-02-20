**Example 1: 成功**

成功

Input: 

```
tccli trabbit CreateRabbitMQServerlessExchange --cli-unfold-argument  \
    --InstanceId amqp-slmejnrgtz \
    --VirtualHost vhost1 \
    --ExchangeName exchange2 \
    --ExchangeType fanout \
    --Remark 测试交换机 \
    --Durable True
```

Output: 
```
{
    "Response": {
        "ExchangeName": "exchange2",
        "RequestId": "01f525e3-fc29-498e-a801-741cee1aed9e"
    }
}
```

