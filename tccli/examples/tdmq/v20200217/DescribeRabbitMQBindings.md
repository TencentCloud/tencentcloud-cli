**Example 1: 查询RabbitMQ路由关系列表**



Input: 

```
tccli tdmq DescribeRabbitMQBindings --cli-unfold-argument  \
    --InstanceId amqp-44w9928j \
    --VirtualHost tdmq_data
```

Output: 
```
{
    "Response": {
        "BindingInfoList": [
            {
                "BindingId": 127469,
                "VirtualHost": "tdmq_data",
                "Source": "test-exchange",
                "DestinationType": "queue",
                "Destination": "test-queue",
                "RoutingKey": "test-rk",
                "SourceExchangeType": "direct",
                "CreateTime": "2022-12-16 11:19:56",
                "ModifyTime": "2022-12-16 11:19:56"
            }
        ],
        "TotalCount": 1,
        "RequestId": "a8f28d5e-a7e2-4b0b-afa0-2fba09c077a0"
    }
}
```

