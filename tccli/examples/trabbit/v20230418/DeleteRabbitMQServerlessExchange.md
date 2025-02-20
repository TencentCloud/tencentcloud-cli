**Example 1: 成功**



Input: 

```
tccli trabbit DeleteRabbitMQServerlessExchange --cli-unfold-argument  \
    --InstanceId amqp-slrlpeddnr \
    --VirtualHost testVhost \
    --ExchangeName testExchange
```

Output: 
```
{
    "Response": {
        "ExchangeName": "testExchange",
        "RequestId": "a8f28d5e-a7e2-4b0b-afa0-2fba09c077a0"
    }
}
```

